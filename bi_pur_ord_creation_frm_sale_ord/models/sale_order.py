from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    @api.model
    def create(self,vals):
        res = super(SaleOrder,self).create(vals)
        product_list=[]
        purchase=self.env['purchase.order'].create({
                    'partner_id':res.partner_id.id,
                    'currency_id': res.currency_id.id,
                    'company_id': res.company_id.id,
                    'date_order': res.date_order
                })
        lines=res.order_line
        for line in lines:
            product_list.append(line.product_id)
            # difference b/w sale order line quantity and on hand quantity of that product
            difference = line.product_uom_qty - line.product_id.qty_available
            if difference>0:
                self.env['purchase.order.line'].create({
                    'product_id': line.product_id.id,
                    'name': line.product_id.name,
                    'product_qty':difference,
                    'price_unit':line.price_unit,
                    'order_id': purchase.id,
                })     
        purchase.button_confirm()
        picking_id = purchase.picking_ids
        for each in picking_id:
            for rec in each.move_ids_without_package:
                rec.quantity_done = rec.product_uom_qty
            each.button_validate()
        return res
