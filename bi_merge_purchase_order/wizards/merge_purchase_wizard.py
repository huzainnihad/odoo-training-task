# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date
from odoo.exceptions import UserError


class MergePurchaseWizard(models.TransientModel):
    _name = 'merge.purchase.wizard'
    _description = 'Merge Purchase Wizard'

    purchase_order_ids = fields.Many2many('purchase.order', string="Orders")
    
    
    def action_merge_purchase(self):
        orders = self.purchase_order_ids
        today = date.today()
    
        for order in orders:
            if order.create_invoice:
                raise UserError(_("you have already created the vendor bill."))
            order.create_invoice = True
            picking_ids = order.picking_ids
            for line in picking_ids.move_ids_without_package:
                line.quantity_done=line.product_uom_qty 
            picking_ids.button_validate()

        purchase_order_lines = []
        product_ids = []
        invoive_lines_values = []

        for order in orders:
            for line in order.order_line:
                purchase_order_lines.append(line.id)

        purchase_line = self.env['purchase.order.line'].search([("id", "in", purchase_order_lines)])

        for line in purchase_line:
            if line.id in purchase_line.ids:
                line_ids = purchase_line.filtered(lambda m: m.product_id.id == line.product_id.id)
                quantity = 0
                for qty in line_ids:
                    quantity += qty.product_uom_qty

                if line.product_id.id not in product_ids:
                    vals = (0, 0, {
                            'product_id':line.product_id.id,
                            'name':line.name,
                            'quantity':quantity,
                            'price_unit':line.price_unit
                        })
                    product_ids.append(line.product_id.id)
                    invoive_lines_values.append(vals)

        invoice_record = self.env['account.move'].create({
            'move_type':'in_invoice',
            'partner_id': orders.partner_id.id,
            'invoice_date':today,
            'currency_id':orders.currency_id.id,
            'invoice_line_ids':invoive_lines_values
        })
        invoice_record.action_post()
        

            


    
