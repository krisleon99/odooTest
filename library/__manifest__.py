# -*- coding: utf-8 -*-
{
    'name':        "Library Management",

    'summary':
                   """
                   Library management
                   """,

    'description': """
        Manage a Library 
    """,

    'author':      "Unam",
    'website':     "http://www.unam.com",

    # for the full list
    'category':    'Library',
    'version':     '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'uom'],

    # always loaded
    'data':        [
        "security/ir.model.access.csv",
        "views/book_views.xml",
        "views/partner_views.xml",
        "views/rental_views.xml",
        "views/menu_views.xml",
    ],
    # only loaded in demonstration mode
    'demo':        [
        "data/library_data.xml",
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
