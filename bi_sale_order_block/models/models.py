# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class bi_sale_order_block(models.Model):
#     _name = 'bi_sale_order_block.bi_sale_order_block'
#     _description = 'bi_sale_order_block.bi_sale_order_block'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
