from odoo import models

class SaleOrderTemplate(models.AbstractModel):
    _name = 'report.bi_sale_order_import.sale_order_template'
    _inherit = 'report.report_xlsx.abstract'
    
    def generate_xlsx_report(self, workbook, data, students):
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

        row = 0
        col = 0
        sheet.merge_range(row, col, row, col + 4, 'Sale Order Import', format_2)
        row += 1
        sheet.merge_range(row, col, row, col + 4, 'Sale,Bassam infotech kallai',format_1)
        row += 1

        sheet.write(row,col,'Product',format_2)
        sheet.write(row,col + 1,'Quantity',format_2)
        sheet.write(row,col + 2,'Unit Price',format_2)
        sheet.write(row,col + 3,'Tax',format_2)
        sheet.write(row,col + 4,'Sub Total',format_2)
        
    