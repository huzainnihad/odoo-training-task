# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BiAppointment(models.Model):
    _name = 'bi.appointment'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Lecture Appointment'
    _rec_name = 'stud_id'


    stud_id = fields.Many2one('bi.student', string="Students")

    appointment_time = fields.Datetime(string='Appoitment Time')
    booking_date = fields.Date(string="Booking Date")

    @api.onchange('stud_id')
    def action_test(self):
        print("Button clicked !!!!!!!!!")
   
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
