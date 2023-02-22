# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class bi_sale_order_automatic_workflow(models.Model):
#     _name = 'bi_sale_order_automatic_workflow.bi_sale_order_automatic_workflow'
#     _description = 'bi_sale_order_automatic_workflow.bi_sale_order_automatic_workflow'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
