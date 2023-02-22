# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import xlrd
import base64


class SaleImportWizard(models.TransientModel):
    _name = 'sale.import.wizard'
    _description = 'model is used to import excel to lines'
    
    active_id = fields.Many2one("sale.order")
    file_attachment = fields.Binary(string="File Attachment", attachment=True)

    def creating_import_wizard(self):
        for record in self:
            if record.file_attachment:
                workbook = xlrd.open_workbook(file_contents=base64.decodestring(record.file_attachment))
                for sheet in workbook.sheets():
                    product_col = 0
                    qty_col = 1
                    unit_price_col = 2
                    # tax_col = 3
                    values = []
                    for row in range(3, sheet.nrows):
                        try:
                            product_id = self.env["product.product"].search(
                                [("default_code", "=", sheet.cell(row, product_col).value)]
                            )
                            if not product_id:
                                raise UserError(_("Product not found"))
                            product_qty = False
                            product_qty = sheet.cell(row, qty_col).value
                            unit_price = sheet.cell(row, unit_price_col).value
                            # tax = sheet.cell(row, tax_col).value
                            values.append(
                                (
                                    0,
                                    0,
                                    {
                                        "product_id": product_id.id,
                                        "product_uom_qty": product_qty,
                                        "price_unit" : unit_price,
                                        # "tax_id" : tax,
                                    },
                                )
                            )
                        except IndexError:
                            break
                    record.active_id.order_line = False
                    record.active_id.order_line = values

        
