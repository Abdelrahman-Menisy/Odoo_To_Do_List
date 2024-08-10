{
    'name': 'To Do List',
    'version': '17.0.1.0',
    'author': 'Menisy',
    'category': 'Tools',
    'summary': 'Manage To-Do Lists',
    'description': 'Module for managing to-do lists with tasks and deadlines.',
    'depends': ['base',
                'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/main_menu.xml',
        'views/To_Do_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
        ],
    },
    'application': True
}
