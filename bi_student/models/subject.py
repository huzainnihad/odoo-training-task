# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BiSubject(models.Model):
    _name = 'bi.subject'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Subject'
    _rec_name = 'stud_subject'
    
    stud_subject = fields.Char(string="Subject")
    max_mark = fields.Integer(string="Max Mark")
