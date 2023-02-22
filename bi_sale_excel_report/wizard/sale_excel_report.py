# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ExcelReportWizard(models.TransientModel):
    _name = 'sale.excel.report.wizard'
    _description = 'Sale Excel Report Wizard'
    
    sale_order_id = fields.Many2one('sale.order', string="Sale Order")
    date_from = fields.Date(required=True,)
    date_to = fields.Date(required=True,)
    
    def action_print_excel(self):
        data = {
            'sale_orders': self.sale_order_id.id,
            'from_dates': self.date_from,
            'to_dates': self.date_to,
                 
        }

        return self.env.ref('bi_sale_excel_report.report_sale_card_xls').report_action(self, data=data)
