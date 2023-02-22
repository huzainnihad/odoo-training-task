from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, timedelta

class SaleOrderBlockSuper(models.Model):
    _inherit = 'sale.order'
    


    @api.model
    def action_confirm(self):
        today = datetime.now()
        res = super(SaleOrderBlockSuper,self).action_confirm()
        # to get field from res config setting
        blockingdays = int(self.env['ir.config_parameter'].sudo().get_param('bi_sale_order_block.sale_order_block'))
        # blockingdaysint = int(blockingdays)
        if self.confirmation_date:
            if self.confirmation_date <= today - timedelta(days=blockingdays):
                raise UserError(_("you can't confirm last sale order"))
        return res