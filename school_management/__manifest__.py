# -*- coding: utf-8 -*-
{
    'name': "School Management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    'category': 'School',
    'version': '16.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'portal', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/school_security.xml',
        'data/data.xml',
        'report/student_report.xml',
        'views/school_student_view.xml',
        'views/school_teacher_view.xml',
        'views/school_subject_view.xml',
        'views/school_class_view.xml',
        'views/school_exam.xml',
        'views/school_exam_result.xml',
        'wizard/set_class_view.xml',
    ],
}
