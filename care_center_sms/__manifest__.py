# -*- coding: utf-8 -*-
{
    'name': "care_center_sms",

    'summary': """
        SMS for Care Center.""",

    'description': """
        Depends on https://www.odoo.com/apps/modules/10.0/sms_frame/.
    """,

    'author': "Dave Burkholder <dave@thinkwelldesigns.com>",
    'website': "http://www.thinkwelldesigns.com",

    'category': 'Tools',
    'version': '0.1',

    'depends': [
        'sms_frame',
        'care_center',
        'care_center_contacts',
        'project',
    ],

    'data': [
        'views/sms_frame.xml',
        'views/care_center.xml',
        'views/contacts.xml',
        'views/project_task.xml',
    ],
}
