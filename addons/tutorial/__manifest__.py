{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Jorge Alberto Quiroz Sierra",
    'category': 'Category',
    'description': """
    ODOO Tutorial for documentation and learning better techniques
    """,
    'images': ['static/description/icon.png'],
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property.xml',
        'views/menu.xml',
        # 'views/mymodule_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'license': 'GPL-3'
}