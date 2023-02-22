from odoo import models, _
from odoo.exceptions import UserError
from datetime import datetime, date


class SaleCardXlsx(models.AbstractModel):
    _name = 'report.bi_product_report.product_report_excel'
    _inherit = 'report.report_xlsx.abstract'

   
    def generate_xlsx_report(self, workbook, data, sale):

        domain =[]

        prod_detail = data.get('product_detail')
        prod_category = data.get('product_category2')
        
        if prod_detail:
            if prod_detail != prod_category:
                raise UserError(_("You entered product and product category not matching."))
        if prod_detail:
            domain.append(('id', '=', prod_detail))
        if prod_category:
            domain.append(('categ_id', '=', prod_category))
        products = self.env['product.product'].search(domain)

        date_fro = data.get('from_dates')
        date_to = data.get('to_dates')
        if date_fro > date_to:
            raise UserError(_("invalid date"))

        sheet = workbook.add_worksheet('Sale Order')
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold':True, 'align': 'center', 'bg_color':'#bdc3c7'})
        format_2 = workbook.add_format({'align': 'center', 'bold':True,'bg_color':'#9a7d0a'})
        format_3 = workbook.add_format({'align': 'center'})
        format_4 = workbook.add_format({'align': 'left','bold':True})

    
        sheet.set_column('A:A',20)
        sheet.set_column('B:B',25)
        sheet.set_column('C:C',19)
        sheet.set_column('D:D',16)
        sheet.set_column('E:E',12)
        sheet.set_column('F:F',25)
        sheet.set_column('G:G',14)
        sheet.set_column('H:H',14)


        row = 0
        col = 0
        sheet.merge_range(row, col, row, col + 7, 'Product Detail Report',format_1)
        row += 1
        sheet.merge_range(row, col, row, col + 3,'From :      ' + date_fro , format_4)
        sheet.merge_range(row, col + 4, row, col + 7,'To :      '+ date_to , format_4)
        row += 1

        sheet.write(row,col,'Product Name',format_2)
        sheet.write(row,col + 1,'Product Category',format_2)
        sheet.write(row,col + 2,'Opening Stock',format_2)
        sheet.write(row,col + 3,'Delivered Stock',format_2)
        sheet.write(row,col + 4,'Invoice Qty',format_2)
        sheet.write(row,col + 5,'Sale Qty or Reseverd Qty',format_2)
        sheet.write(row,col + 6,'Purchase Stock',format_2)
        sheet.write(row,col + 7,'Closed stock',format_2) 
        row += 1

        for prod in products:
            sale_order_ids = self.env['sale.order'].search([('date_order', '>=', date_fro), ('date_order', '<=', date_to)])
            sale_order_lines = sale_order_ids.mapped("order_line")
            qty_delivered = sum(sale_order_lines.filtered(lambda x:x.product_id == prod).mapped("qty_delivered"))
            qty_invoiced = sum(sale_order_lines.filtered(lambda x:x.product_id == prod).mapped("qty_invoiced"))
            # for getting the sale qty
            out_going_move_id = self.env['stock.move'].search([('product_id', '=', prod.id),
                ('picking_id.picking_type_code', '=', 'outgoing'),
                ('create_date', '>=', date_fro),
                ('create_date', '<=', date_to),
                ])
            qty_sale = sum(out_going_move_id.mapped("forecast_availability"))
            # for getting the purchase stock
            incoming_move_id = self.env['stock.move'].search([('product_id', '=', prod.id),
                ('picking_id.picking_type_code', '=', 'outgoing'),
                ('create_date', '>=', date_fro),
                ('create_date', '<=', date_to),
                ])
            qty_purchase = sum(incoming_move_id.mapped("reserved_availability"))
            opening_stock = prod.with_context({'to_date':date_fro}).qty_available
            closing_stock = prod.with_context({'to_date':date_to}).qty_available
            for cat in prod_category:
                if prod.categ_id.id == cat:
                    sheet.write(row,col,prod.name,format_3)
                    sheet.write(row,col + 1,prod.categ_id.name,format_3)
                    sheet.write(row,col + 2,opening_stock,format_3)
                    sheet.write(row,col + 3,qty_delivered,format_3)
                    sheet.write(row,col + 4,qty_invoiced,format_3)
                    sheet.write(row,col + 5,qty_sale,format_3)
                    sheet.write(row,col + 6,qty_purchase,format_3)
                    sheet.write(row,col + 7,closing_stock,format_3)       
            row += 1         
       

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
  
