# -*- coding: utf-8 -*-
{
    "name": "bi_merge_purchase_order",

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
        "security/ir.model.access.csv",
        "views/action_manual_vendor_bill.xml",
        "views/create_invoice_merge.xml",
        "wizards/merge_purchase_wizard.xml"
    ],
}