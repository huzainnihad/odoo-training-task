# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class bi_material_transfer(models.Model):
#     _name = 'bi_material_transfer.bi_material_transfer'
#     _description = 'bi_material_transfer.bi_material_transfer'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
