{
    'name': "Care Center",

    'summary': """
        Odoo Help Desk & Ticketing System inspired by osTicket,
        and various other Odoo modules.""",

    'author': "Thinkwell Designs",
    'website': "http://www.thinkwelldesigns.com",

    'category': 'Support',
    'version': '11.0.1.0.0',

    'depends': [
        'base_automation',
        'utm',
        'note',
        'calendar',
        'crm_phonecall',
        'project',
        'support_team',
    ],

    'data': [
        # 'security/ir.model.access.csv',
        'data/utm.xml',
        'views/fetchmail_server.xml',
        'views/res_config_settings.xml',
        'views/project_task.xml',
        'views/base_automation',
        'views/care_center.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
