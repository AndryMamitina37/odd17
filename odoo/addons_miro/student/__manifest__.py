# -*- coding: utf-8 -*-
{
    'name': 'Student Management',
    'version': '1.2',
    'summary': 'Module for managing students',
    'sequence': 1,
    'description': """
Student Management Module
=========================
This module helps manage students' information such as name, age, class, and enrollment date.
It is easy to use and allows you to organize and manage student data efficiently.
    """,
    'category': 'Education',
    'website': 'https://www.odoo.com/app/Student',
    'depends': ['base'],
    'data': [
        'security/student_security.xml',  # Security rules file
        'security/ir.model.access.csv',  # Access control list
        'views/student_view.xml',  # Main view file for the student model
    ],
    'demo': [
        'demo/student_demo.xml',  # Demo data file
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
