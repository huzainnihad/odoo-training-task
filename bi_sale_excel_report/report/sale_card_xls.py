from odoo import models


class SaleCardXlsx(models.AbstractModel):
    _name = 'report.bi_sale_excel_report.report_sale_card_xls'
    _inherit = 'report.report_xlsx.abstract'

   
    def generate_xlsx_report(self, workbook, data, sale):

        domain =[]

        if data.get('from_dates'):
            domain.append(('date_order', '>=', data.get('from_dates')))
        if data.get('to_dates'):
            domain.append(('date_order', '<=', data.get('to_dates')))
        if data.get('sale_orders'):
            domain.append(('id', '=', data.get('sale_orders')))
 
        sale_orders = self.env['sale.order'].search(domain)
        date_from = data.get('from_dates')
        date_to = data.get('to_dates')

        sheet = workbook.add_worksheet('Sale Order')
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold':True, 'align': 'center', 'bg_color':'#bdc3c7'})
        format_2 = workbook.add_format({'align': 'center', 'bold':True,'bg_color':'#9a7d0a'})
        format_3 = workbook.add_format({'align': 'center'})
        format_4 = workbook.add_format({'align': 'center','bold':True})

    
        sheet.set_column('A:A',16)
        sheet.set_column('B:B',25)
        sheet.set_column('C:C',19)
        sheet.set_column('D:D',14)
        sheet.set_column('E:E',12)
        sheet.set_column('F:F',12)
        sheet.set_column('G:G',14)
        sheet.set_column('H:H',14)
        sheet.set_column('I:I',16)


        row = 0
        col = 0
        sheet.merge_range(row, col, row, col + 8, 'Sale,Bassam infotech kallai',format_1)
        row += 1
        sheet.merge_range(row, col, row , col + 8,  date_from + '  To  ' + date_to,  format_4)
        row += 1

        sheet.write(row,col,'Sale Order Name',format_2)
        sheet.write(row,col + 1,'Customer Name',format_2)
        sheet.write(row,col + 2,'Product',format_2)
        sheet.write(row,col + 3,'Date',format_2)
        # sheet.write(row,col + 4,'Model Year',format_2)
        sheet.write(row,col + 5,'Quantity',format_2)
        sheet.write(row,col + 6,'Unit Price',format_2)
        sheet.write(row,col + 7,'Tax',format_2)
        sheet.write(row,col + 8,'Sub Total',format_2)
        
        for sale in sale_orders:
            row += 1
            sheet.write(row,col,sale.name,format_3)
            sheet.write(row,col + 1,sale.partner_id.name,format_3)
            sheet.write(row,col + 3,sale.date_order.strftime("%m/%d/%Y"),format_3)
            total = 0
            for line in sale.order_line:
                sheet.write(row,col + 2,line.product_id.name,format_3)
                sheet.write(row,col + 5,line.product_uom_qty,format_3)
                # sheet.write(row,col + 4,line.model_year,format_3)
                sheet.write(row,col + 6,line.price_unit,format_3)
                sheet.write(row,col + 8,line.price_subtotal,format_3)
                total += line.price_subtotal
                temp = row
                for tax in line.tax_id:
                    sheet.write(row,col + 7,tax.name,format_3)
                    temp = temp + 1
                row += 1
        sheet.write(row,col + 7,'Total',format_2)
        sheet.write(row,col + 8,total,format_2)
            

  