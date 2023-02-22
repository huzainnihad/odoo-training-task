# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class bi_purchase_report(models.Model):
#     _name = 'bi_purchase_report.bi_purchase_report'
#     _description = 'bi_purchase_report.bi_purchase_report'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
