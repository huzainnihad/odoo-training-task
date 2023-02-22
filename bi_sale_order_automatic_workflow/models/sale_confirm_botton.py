# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder,self).action_confirm()
        picking_ids = self.picking_ids
        for line in picking_ids:
            for move in picking_ids.move_ids_without_package:
                move.quantity_done=move.product_uom_qty
        line.button_validate()
        invoice_id=self._create_invoices()
        self.invoice_ids.action_post()
        payment_method_line_id = self.env['account.payment.method.line'].search([('name', '=', 'Manual')])[0]
        journal_id =self.env['account.journal'].search([('name', '=', 'Bank')])
        vals=self.env['account.payment'].create({
            'date': self.date_order,
            'amount': self.amount_total,
            'payment_type': "inbound",
            'partner_type': "customer", 
            'ref': invoice_id.ref,
            'journal_id': journal_id.id,
            'currency_id': self.currency_id.id,
            'partner_id': self.partner_id.id,
            'partner_bank_id': invoice_id.partner_bank_id.id,
            'payment_method_line_id': payment_method_line_id.id,
            })
        invoice_id.payment_state="paid"
        vals.action_post()
        return res

