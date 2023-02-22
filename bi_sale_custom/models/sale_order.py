from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    remark = fields.Char()
    confirmation_date = fields.Datetime()



class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    remark = fields.Char()

    @api.onchange('product_id')
    def _onchange_product_id_remark(self):
        if self.order_id.remark:
            self.remark = self.order_id.remark
