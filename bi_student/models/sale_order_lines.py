# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BiSubjectSaleOrderLine(models.Model):
    _name = 'bi.sale.order.line'
    _description = 'Sale Order'
    
    product = fields.Many2one('product.template', string="Product")
    quantity = fields.Integer(string="Quantity")
    unit_price = fields.Integer(string="Unit Price")
    subtotal = fields.Integer(string="Subtotal")
    #connection to the sale order
    product_sale_id = fields.Many2one('bi.student',string="lines")
