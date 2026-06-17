{
    'name': 'Helpdesk Team Hierarchy',
    'version': '19.0.1.0.0',
    'category': 'Helpdesk',
    'summary': 'Add parent/child hierarchy to Helpdesk Teams',
    'depends': ['helpdesk','base', 'web_hierarchy',],
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_team_views.xml',

    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
