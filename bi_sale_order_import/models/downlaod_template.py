from odoo import models, fields, api, _

class DownlaodTemplate(models.Model):
    _inherit = "sale.order"

    def action_download_template(self):
       return self.env.ref('bi_sale_order_import.sale_order_downlaod_template').report_action(self)

    def import_wizard(self):
        return{
            "name": _("Import Lines"),
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "sale.import.wizard",
            "context": {"default_active_id": self.id},
            "target": "new",
        }


