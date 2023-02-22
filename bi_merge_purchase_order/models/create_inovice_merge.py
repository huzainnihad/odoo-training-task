from odoo import models, fields, api, _
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    create_invoice = fields.Boolean(string="Invoice Create", default=False)

    def action_create_vendor_bill(self):
        partner=[]
        status =[]
        for purchase_order in self:
            partner.append(purchase_order.partner_id)
            status.append(purchase_order.state)
        total_vendor_bill = len(partner)
        for i in range(total_vendor_bill):
            if partner[0]!=partner[i]:
                raise UserError(_("You have entered an different purchase order"))
            if status[0]!=status[i]:
                raise UserError(_("Check your status"))


        return{ 
                'res_model':'merge.purchase.wizard',
                'view_mode':'form',
                'type':'ir.actions.act_window',
                'target':'new',
                'context':{'default_purchase_order_ids':self.ids}
            }