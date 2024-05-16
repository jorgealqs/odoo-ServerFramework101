{
    'name': "Web Framework Odoo",
    'version': '1.0',
    'summary':"OWL tutorial odoo",
    'sequence':-2,
    'author': "Jorge Alberto Quiroz Sierra",
    'category': 'OWL',
    'description': """
    Discover the web framework
    """,
    'depends': ['base', 'web'],
    'images': [
        # 'static/description/icon.png'
    ],
    # data files always loaded at installation
    'data': [
        # 'security/ir.model.access.csv',
        'views/action_menu.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend':[
            # 'awesome_owl/static/src/components/utils.js',
            'awesome_owl/static/src/components/**/*',
        ]
    },
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'license': 'GPL-3',
    'installable': True,
    'application': True,
}
