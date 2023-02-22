# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class PurchaseAuto(models.Model):
    _inherit = "purchase.order"

    def button_confirm(self):
        res = super(PurchaseAuto,self).button_confirm()
        pick_ids = self.picking_ids
        for data in pick_ids:
            for line in pick_ids.move_ids_without_package:
                line.quantity_done = line.product_uom_qty
        data.button_validate()
        self.action_create_invoice()
        self.invoice_ids.invoice_date = datetime.now()
        self.invoice_ids.action_post()
        payment_method_line_id = self.env['account.payment.method.line'].search([('name', '=', 'Manual')])[0]
        journal_id =self.env['account.journal'].search([('name', '=', 'Bank')])
        vals=self.env['account.payment'].create({
            'date': self.date_order,
            'amount': self.amount_total,
            'payment_type': "outbound",
            'partner_type': "supplier", 
            'ref': self.partner_ref,
            'journal_id': journal_id.id,
            'currency_id': self.currency_id.id,
            'partner_id': self.partner_id.id,
            'partner_bank_id': self.invoice_ids.partner_bank_id.id,
            'payment_method_line_id': payment_method_line_id.id,
            })
        self.invoice_ids.payment_state="paid"
        vals.action_post()
        return res
