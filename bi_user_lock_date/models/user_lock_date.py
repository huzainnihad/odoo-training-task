# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import datetime
from odoo.exceptions import UserError


class UserLockDate(models.Model):
    _name = "user.lock.date"
    _description = "user lock date"
    _rec_name = "date"

    date = fields.Date(string="Date", required=True)
    lock_date = fields.Boolean(string="Lock Date", default=False)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self,vals):
        user_lock = self.env['user.lock.date'].search([('lock_date', '=', True)], order='date desc')[0]
        stock_date = vals['scheduled_date']
        stock_date_prod =  fields.Date.from_string(stock_date)
        if user_lock.date > stock_date_prod:
            raise UserError(_("your cannot tranfers products before user lock date"))
        res = super(StockPicking, self).create(vals)
        return res
    
    # def write(self,vals):
    #     user_lock = self.env['user.lock.date'].search([('lock_date', '=', True)], order='date desc')[0]
    #     stock_date = vals['scheduled_date']
    #     stock_date_prod =  fields.Date.from_string(stock_date)
    #     if user_lock.date > stock_date_prod:
    #         raise UserError(_("your cannot tranfers products before user lock date"))
    #     res = super(StockPicking, self).create(vals)
    #     return res
    
class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.model
    def create(self,vals):
        user_lock = self.env['user.lock.date'].search([('lock_date', '=', True)], order='date desc')[0]
        manufacturing_date = vals['date_planned_start']
        manufacturing_date_product =  fields.Date.from_string(manufacturing_date)
        if user_lock.date > manufacturing_date_product:
            raise UserError(_("your cannot manufacture before user lock date"))
        res = super(MrpProduction, self).create(vals)
        return res

    def write(self,vals):
        user_lock = self.env['user.lock.date'].search([('lock_date', '=', True)], order='date desc')[0]
        manufacturing_date = vals['date_planned_start']
        manufacturing_date_product =  fields.Date.from_string(manufacturing_date)
        if user_lock.date > manufacturing_date_product:
            raise UserError(_("your cannot manufacture before user lock date"))
        res = super(MrpProduction, self).create(vals)
        return res
