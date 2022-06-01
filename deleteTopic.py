# -*- coding: utf-8 -*-
from __future__ import print_function

import os.path

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from quickstart import main

def deletetopic(course_id,topicId):
    creds = main()
    try:
        service = build('classroom', 'v1', credentials=creds)

        service.courses().topics().delete(courseId=course_id,id=topicId).execute()

    except HttpError as error:
        print('An error occurred: %s' % error)

