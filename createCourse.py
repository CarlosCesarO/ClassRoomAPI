# -*- coding: utf-8 -*-
from __future__ import print_function

import os.path

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from quickstart import main

def createcourse(name):
    creds = main()
    try:
        service = build('classroom', 'v1', credentials=creds)

        course = {
            'name': (name),
            'section': 'Curriculos Inculcar',  
            'ownerId': 'me',
            'courseState': 'ACTIVE'
        }
        course = service.courses().create(body=course).execute()
        return course.get('id')


    except HttpError as error:
        print('An error occurred: %s' % error)

