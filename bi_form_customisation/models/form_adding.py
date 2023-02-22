from odoo import models, fields, api

class FormAdding(models.Model):
    _inherit = "product.template"

    model_year = fields.Char()
    


class FormAddingSale(models.Model):
    _inherit = "sale.order.line"

    model_year = fields.Char()

    @api.onchange('product_id')
    def _onchange_product_id_modelyear(self):
        if self.product_id:
            self.model_year = self.product_id.model_year

class AddingLine(models.Model):
    _inherit = "sale.order"

    link = fields.Char(default="https://www.bassaminfotech.com")