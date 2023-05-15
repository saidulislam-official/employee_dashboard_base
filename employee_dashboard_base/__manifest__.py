# -*- coding: utf-8 -*-
{
    'name': "Employee Dashboard Base",
    'summary': "Employee Dashboard",
    'version': '13.0.1',
    'description': """Employee Dashboard""",
    'author': "Saidul Islam",
    'website': "http://www.yourcompany.com",
    'category': "HR",
    "depends": ['hr'],
    "data": [
        'views/dashboard_view.xml',
         'views/web_asset_backend_template.xml',

    ],
    "qweb": [
        "static/src/xml/dashboard.xml",
    ],

    "installable": True,
    "application": True,
}
