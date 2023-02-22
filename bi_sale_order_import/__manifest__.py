# -*- coding: utf-8 -*-
{
    "name": "bi_sale_order_import",

    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.odoo.com""",

    "description": """
        Long description of module's purpose
    """,

    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Uncategorized",
    "sequence": -100,
    "version": "0.1",
    "external_dependecies":{"python":("xlsxwriter", "xlrd")},
    "depends": ["base","sale","report_xlsx"],
    "data": [
        "security/ir.model.access.csv",
        "wizards/import_wizard.xml",
        "views/downlaod_template_button.xml",
        "reports/sale_template.xml",
        
    ],
}