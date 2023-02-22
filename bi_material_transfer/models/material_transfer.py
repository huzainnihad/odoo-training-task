# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class MaterialTransfer(models.Model):
    _name = 'bi.material.transfer'
    _description = 'Material Transfer'
    _rec_name = 'name'

    name = fields.Char(required=True, copy=False, readonly=True, default=lambda self:_('New'))
    operation_type = fields.Many2one('stock.picking.type')
    source_location = fields.Many2one('stock.location')
    destination_location = fields.Many2one('stock.location')
    date = fields.Date(string="Date")
    confirmation_date = fields.Date(string="Confirmation Date")
    product_line_ids = fields.One2many('bi.product.order.line','product_materialtransfer_id', string="Product Lines")
    stock_picking_id = fields.Many2one('stock.picking')
    picking_count = fields.Integer() #to show picking count
    state= fields.Selection([('draft', 'Draft'),
            ('ready', 'Ready'),
            ('approve', 'Approve'),
            ('done', 'Done')], default='draft', string="Status")

    #sequence for Material Transfer
    @api.model
    def create(self, vals):
        if vals.get('name',_('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('material.transfer') or _('New')
        res = super(MaterialTransfer, self).create(vals)
        return res

    def action_transfer(self):

        if self.source_location == self.destination_location:
            raise UserError(_("You have entered the source location and destination same. Please try again after changing locations "))
        
        lines = self.product_line_ids
        for line in lines:
            line.available_qty-=line.quantity
            line.transfer_qty=line.quantity

            if line.available_qty<line.quantity:
                raise UserError(_("You entered quantity is more than onhand quantity or available quantity"))

        transfer=self.env['stock.picking'].create({
        'picking_type_id':self.operation_type.id,
        'location_id':self.source_location.id,
        'location_dest_id':self.destination_location.id,
        'material_transfer_id':self.id,
        })
        for line in lines:
            move = self.env['stock.move'].create({
                'name': line.product.name,
                'location_id': self.source_location.id,
                'location_dest_id': self.destination_location.id,
                'product_id': line.product.id,
                'product_uom': line.product.uom_id.id,
                'product_uom_qty': line.quantity,
                'quantity_done': line.quantity,
                'picking_id':transfer.id,
                
            })
            move._action_assign()
        self.stock_picking_id = transfer.id
        transfer.button_validate()
        self.picking_count = self.picking_count + 1 #to show picking count
        self.write({"state":"done"})

    def action_view_picking(self):
        return{
                'type':'ir.actions.act_window',
                'name':'Picking',
                'view_mode':'list,form',
                'res_model':'stock.picking',
                'res_id':self.stock_picking_id.id,
                'domain': [('material_transfer_id', '=', self.id )]
        }

    def action_ready(self):
        self.write({"state":"ready"})

    def action_approve(self):
        self.write({"state":"approve"})
    
    def action_done(self):
        self.write({"state":"draft"})






     