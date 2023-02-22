# -*- coding: utf-8 -*-
{
    "name": "bi_product_report",

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
    "version": "0.1",
    "depends": ["base","stock","product"],
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        "wizards/product_report_wizard.xml",
        "reports/product_report.xml"
    ],
}