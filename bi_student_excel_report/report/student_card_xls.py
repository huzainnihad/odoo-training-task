from odoo import models

class StudentCardXlsx(models.AbstractModel):
    _name = 'report.bi_student_excel_report.report_student_excel_id_card'
    _inherit = 'report.report_xlsx.abstract'
    
    def generate_xlsx_report(self, workbook, data, students):
        sheet = workbook.add_worksheet('Student Id Card')
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold':True, 'align': 'center', 'bg_color':'yellow'})
        format_2 = workbook.add_format({ 'align': 'center', })
        format_3 = workbook.add_format({'align': 'center',})
        row = -1
        col = 0
        for obj in students:
            row += 1
            sheet.merge_range(row, col, row + 1, col + 5, 'Student Details ' , format_1)
            row += 2
            sheet.merge_range(row, col,row, col + 5,'Name : ' + obj.stud_name , format_3)
            row += 1
            sheet.merge_range(row, col, row, col + 5, 'Age : ' + str(obj.stud_age) , format_3)
            row += 2
            sheet.merge_range(row, col, row, col + 2, 'Subject ', format_2)
            sheet.merge_range(row, col + 3, row, col + 5, 'Mark ', format_2)
            row += 1
            total = 0
        for line in obj.stud_sub_line_ids:
            sheet.merge_range(row, col, row, col + 2, line.stud_sub_name.stud_subject, format_2)
            sheet.merge_range(row, col + 3, row, col + 5, line.mark, format_2)
            row += 1
            total += line.mark
        sheet.merge_range(row, col, row, col + 2, 'Total ', format_2)
        # total_marks = sum(obj.stud_sub_line_ids.mapped('mark'))
        sheet.merge_range(row, col + 3, row, col + 5, total, format_2)



            
        


           