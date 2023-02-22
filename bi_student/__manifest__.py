# -*- coding: utf-8 -*-
{
    "name": "Student management system",

    "summary": "Student management system",
    "description":"Student managemnet system",

    "author": "school management",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Student",
    "version": "15.0",
    "application":True,
    "auto_install":False,
    "depends": ["base","sale","mail","bi_purchase_report"],
    "data": [
        "security/ir.model.access.csv",
        "data/mail_template_data.xml",
        "data/cron.xml",
        "views/menu.xml",
        "views/stud_view.xml",
        "views/appoinment_view.xml",
        "views/female_stud_view.xml",
        "views/male_stud_view.xml",
        "views/subject_view.xml",
        "reports/report.xml",
        "reports/student_card.xml",
    ],
}