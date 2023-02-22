# -*- coding: utf-8 -*-
{
    "name": "bi_student_excel_report",

    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.odoo.com""",

  

    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["base","report_xlsx","bi_student"],
    "data": [
        # "security/ir.model.access.csv",
        "report/xls_report.xml",
    ],
}
