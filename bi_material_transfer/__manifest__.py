# -*- coding: utf-8 -*-
{
    "name": "Material Transfer",

    "summary": """Material Transfer""",

    "description": """Material Transfer""",

    "author": "Material Transfer",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Material transfer",
    "sequence": -100,
    "application":True,
    "version": "0.1",
    "depends": ["base","product","stock"],
    "data": [
        "security/ir.model.access.csv",
        "security/pick_security.xml",
        "data/data.xml",
        "views/menu.xml",
        "views/material_transfer.xml",
        "views/material_transfer_inherit.xml",
        
    ],
}