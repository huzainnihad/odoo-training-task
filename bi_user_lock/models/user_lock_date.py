# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import UserError

class BiUserLock(models.Model):
    _name = 'bi.user.lock'
    _description = 'bi user lock'
    _rec_name = "date"

    date = fields.Date(string="Date", required=True)
    lock_date = fields.Boolean(string="Lock Date")

#purchase order user lock date
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def create(self,vals):
        purchase_date = vals['date_order']
        purchase_order_date = fields.Date.from_string(purchase_date)
        purchase_user_lock_date = self.env['bi.user.lock'].search([('lock_date', '=', True)],order='date desc')[0]
        if purchase_user_lock_date.date > purchase_order_date:
            raise UserError(_("your cannot create purchase order before user lock date"))
        res = super(PurchaseOrder, self).create(vals)
        return res    

#sale order user lock date
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def create(self,vals):
        sale_date = vals['date_order']
        sale_order_date = fields.Date.from_string(sale_date)
        sale_user_lock_date = self.env['bi.user.lock'].search([('lock_date', '=', True)],order='date desc')[0]
        if sale_user_lock_date.date > sale_order_date:
            raise UserError(_("your cannot create sale order before user lock date"))
        res = super(SaleOrder, self).create(vals)
        return res
    
#Invoicing Sale user lock date

# class Invoicing(models.Model):
#     _inherit = 'account.move'

#     def create(self,vals):
#         account_date = vals['invoice_date']
#         account_invoice_date = fields.Date.from_string(account_date)
#         account_user_lock_date = self.env['bi.user.lock'].search([('lock_date', '=', True)],order='date desc')[0]
#         if account_user_lock_date.date > account_invoice_date:
#             raise UserError(_("your cannot create invoice before user lock date"))
#         res = super(Invoicing, self).create(vals)
#         return res

    


