# -*- coding: utf-8 -*-
{
    "name": "bi_comment_resolution_sheet",

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
    "depends": ["base","purchase"],
    "data": [
        # "security/ir.model.access.csv",
        "views/views.xml",
        "reports/paper_format.xml",
        "reports/report_action.xml",
        "reports/template.xml",
        "reports/report_action_2.xml",
        "reports/template_2.xml",
    ],
}