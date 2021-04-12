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
    'depends':     ['base'],

    # always loaded
    'data':        [
        "security/ir.model.access.csv",
        # "data/library_data.xml",
    ],
    # only loaded in demonstration mode
    'demo':        [],
}
