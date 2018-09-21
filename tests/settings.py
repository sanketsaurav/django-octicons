#!/usr/bin/env python
# -*- coding: utf-8 -*-


SECRET_KEY = 'hunter2'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

INSTALLED_APPS = [
    'octicons.apps.OcticonsConfig'
]
