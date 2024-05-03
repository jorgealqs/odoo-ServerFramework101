{
    'name': "OWL tutorial odoo",
    'version': '1.0',
    'depends': ['base'],
    'summaryt':"OWL tutorial odoo",
    'sequence':-1,
    'author': "Jorge Alberto Quiroz Sierra",
    'category': 'OWL',
    'description': """
    Odoo OWL tutorial for beginneers
    """,
    'depends': ['base', 'web'],
    'images': [
        # 'static/description/icon.png'
    ],
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list.xml',
        'views/menu.xml',

    ],
    'assets': {
        'web.assets_backend':[
            'owl_youtube/static/src/components/**/*',
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
