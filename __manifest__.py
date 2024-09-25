# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': 'RecruitGo',
    'version': '1.0',
    'summary': 'Manage Recruitment',
    'description': """
        This module manages import stages with the following stages:
        - New
        - Hr Approval
        - Admin Approval
        - Done
        - Refuse
        - Cancelled
    """,
    'author': '',
    'category': 'Recruitment',
    'depends': ['base', 'hr', 'hr_recruitment', 'hr_holidays'],
    'data': [
        'security/hr_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'wizard/job_refuse_wizard_view.xml',
        'views/job_hire_view.xml',
        'views/hr_leave_view.xml',
        'views/recruitego_menu.xml',
    ],
    
    'installable': True,
    'application': True,
}
