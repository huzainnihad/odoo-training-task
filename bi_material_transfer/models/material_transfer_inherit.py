from odoo import models, fields


class MaterialTransferInherit(models.Model):
    _inherit="stock.picking"

    material_transfer_id = fields.Many2one('bi.material.transfer')
