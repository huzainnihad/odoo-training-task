# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductOrderLine(models.Model):
    _name = 'bi.product.order.line'
    _description = 'Product Line'
    
    product = fields.Many2one('product.product')
    quantity = fields.Integer()
    available_qty = fields.Integer()
    transfer_qty = fields.Integer()
    #connection 
    product_materialtransfer_id = fields.Many2one('bi.material.transfer',string="lines")

    # To get onhand qty in available qty
    @api.onchange('product')
    def onchange_product(self):
        self.available_qty=self.product.with_context({'location':self.product_materialtransfer_id.source_location.id}).qty_available

