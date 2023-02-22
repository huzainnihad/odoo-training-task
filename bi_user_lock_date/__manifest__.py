# -*- coding: utf-8 -*-
{
    'name': 'bi_user_lock_date',
    'version': '0.1',
    'category': '',
    'description': """A module to verify the Assets Bundle mechanism.""",
    'maintainer': 'Odoo SA',
    'depends': ['base','stock','mrp'],
    'installable': True,
    'data': [
        "security/ir.model.access.csv",
        "views/menu_user_lock_date.xml",
        # "views/menu.xml",
    ],
}
