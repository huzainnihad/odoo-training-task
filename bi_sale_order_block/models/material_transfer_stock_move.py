# from odoo import models, fields, api, _
# from odoo.exceptions import UserError
# from datetime import datetime, timedelta

# class MaterialTransferSuper(models.Model):
#     _inherit = 'bi.material.transfer'

#     @api.model
#     def action_transfer(self):
#         C_date = datetime.now()
#         res = super(MaterialTransferSuper,self).action_transfer()
#         stock_move_date = int(self.env['ir.config_parameter'].sudo().get_param('bi_sale_order_block.stock_move'))
#         if self.confirmation_date > C_date - timedelta(days=stock_move_date):
#             raise UserError(_("you can't confirm last sale order"))
#         return res
