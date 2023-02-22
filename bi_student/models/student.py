# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BiStudent(models.Model):
    _name = 'bi.student'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Student Management'
    _rec_name = 'stud_name'

    stud_name = fields.Char()
    stud_age = fields.Integer()
    stud_gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
    stud_reference = fields.Selection([('minor','Minor'),('major','Major')])
    stud_result = fields.Selection([('pass','Pass'),('fail','Fail')],compute='_compute_mark')
    stud_mark = fields.Float()
    link = fields.Char()
    password = fields.Char()
    message = fields.Char()
    email = fields.Char()
    increment = fields.Integer()

    state= fields.Selection([('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Status")
    
    stud_sub_line_ids = fields.One2many('bi.subject.lines','subject_id', string="Subject Lines")

    sale_id = fields.Many2one("sale.order")
    customer_name = fields.Text(compute="_customer_name")
    order_date = fields.Char(compute="_order_date")
    payment_terms = fields.Char(compute="_payment_terms")
    # connection from the sale details xml in lines
    product_details_ids = fields.One2many('bi.sale.order.line','product_sale_id',string="connection")



    # schedular cron
    def test_cron_job(self):
        records = self.env['bi.student'].search([])
        for rec in records:
                rec.increment += 1
        
        for rec in records:
                template = self.env.ref('bi_student.student_mail_template')
                template.send_mail(rec.id ,force_send=True)


    def action_approve(self):
        for rec in self:
            #odoo search method
            students =  self.env['bi.student'].search([])
            print('students.......',students)
            # search method AND
            female_stud = self.env['bi.student'].search([('stud_gender','=','female'),
                                                        ('stud_age','<=',10)]) 
            print('female students below age 10.....',female_stud)

            male_stud = self.env['bi.student'].search([('stud_gender','=','male')]) 
            print('male students.....',male_stud)
            # search method OR
            male_stud_or = self.env['bi.student'].search([ ('stud_gender','=','male'),
                                                        ('stud_age', '>=', 10)]) 
            print('male students above 10.....',male_stud_or)

            #search_count method
            student_count = self.env['bi.student'].search_count([])
            print("students count....",student_count)

            male_stud_count = self.env['bi.student'].search_count([ ('stud_gender','=','male')]) 
            print('male students count.....',male_stud_count)

            female_stud_count = self.env['bi.student'].search_count([('stud_gender','=','female')]) 
            print('female students count.....',female_stud_count)

            other_stud = student_count - (female_stud_count + male_stud_count)
            print('other student count....',other_stud)

        self.write({"state":"confirmed"})

    # send email template
    def action_send_mail(self):
        self.ensure_one()
        template = self.env.ref('bi_student.student_mail_template')
        template.send_mail(self.id ,force_send=True)
            

    def action_done(self):
        self.write({"state":"done"})

    def action_cancel(self):
        self.write({"state":"cancel"})

    @api.onchange('stud_age')
    def _onchange_stud_ref(self):
        if self.stud_age >= 18:
            self.write({"stud_reference":"major"})
        else:
            self.write({"stud_reference":"minor"})

    @api.depends('stud_mark')
    def _compute_mark(self):
        for rec in self:
            if rec.stud_mark >= 40:
                rec.write({"stud_result":"pass"})
            else:
                rec.write({"stud_result":"fail"})


    @api.depends('sale_id')
    def _customer_name(self):
        if self.sale_id:
            self.customer_name = self.sale_id.partner_id.name
        else:
            self.customer_name='0'
    
    @api.depends('sale_id')
    def _order_date(self):
        if self.sale_id:
            self.order_date = self.sale_id.date_order
        else:
            self.order_date='0'

    @api.depends('sale_id')
    def _payment_terms(self):
        if self.sale_id:
            self.payment_terms = self.sale_id.payment_term_id.name
        else:
            self.payment_terms='0'

    @api.onchange('sale_id')
    def onchange_sale_id(self):
        lines = self.sale_id.order_line
        # sum_price = sum(lines.mapped('price_unit'))
        for line in lines:
            # if sum_price <= 1000:
                self.write({
                    "product_details_ids": [(0,0, {
                                        "product":line.product_id.id,
                                        "quantity":line.product_uom_qty,
                                        "unit_price":line.price_unit,
                                        "subtotal":line.price_subtotal
                    })]
                                        
                })
    






class BiSubject(models.Model):
    _name = 'bi.subject.lines'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Subject'
    _rec_name = 'stud_subject'
    

    stud_sub_name = fields.Many2one('bi.subject', string="Subject")
    stud_subject = fields.Char(string="Subject")
    mark = fields.Integer(string="Mark")
    subject_id = fields.Many2one('bi.student', string='Subject')

# class BiSaleOrderLine(models.Model):
#     _name = 'bi.sale.order.line'
#     _inherit = ['mail.thread','mail.activity.mixin']
#     _description = 'Sale Order Line'

#     product = fields.Char(string="Product")
#     quantity = fields.Integer(string="Quantity")
#     unit_price = fields.Integer(string="Unit Price")
#     subtotal = fields.Integer(string="Subtotal")
    


