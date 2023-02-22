# -*- coding: utf-8 -*-
{
    "name": "bi_sale_order_block",

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
    "sequence":-99,
    "version": "0.1",
    "depends": ["base","sale","stock"],
    "data": [
        # "security/ir.model.access.csv",
        "views/views.xml",
        "views/sale_order_block.xml",
        "views/inventory_order_block.xml",
    ],
}