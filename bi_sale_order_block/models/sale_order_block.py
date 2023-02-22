from odoo import models, fields, api

class SaleOrderBlock(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_order_block = fields.Integer(string="Sale Blocking Days",config_parameter='bi_sale_order_block.sale_order_block')

    stock_move = fields.Integer(string="Stock Move",config_parameter='bi_sale_order_block.stock_move')
   