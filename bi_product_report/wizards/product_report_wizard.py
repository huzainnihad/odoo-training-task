# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError



class productReportWizard(models.TransientModel):
    _name = 'product.report.wizard'
    _description = 'product Report Wizard'

    product = fields.Many2many('product.product', string="Product")
    product_category = fields.Many2many('product.category', string="Product Category")
    
    date_from = fields.Date(required=True,)
    date_to = fields.Date(required=True,)
    
    def action_product_report(self):
        data = {
            'product_detail': self.product.ids,
            'product_category2': self.product_category.ids,
            'from_dates': self.date_from,
            'to_dates': self.date_to,
            }

        return self.env.ref('bi_product_report.product_report_excel').report_action(self, data=data)






       








        # if self.product.id not in self.product_category:
        #     raise UserError(_("you have already created the vendor bill."))