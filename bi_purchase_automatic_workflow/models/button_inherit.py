from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_create_payment_button():
        pass