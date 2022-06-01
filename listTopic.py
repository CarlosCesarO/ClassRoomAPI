# -*- coding: utf-8 -*-
from __future__ import print_function
from logging import NullHandler
from pprint import pprint


import os.path

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from quickstart import main


def listtopic(course_id):
    creds = main()
    list = []
    try:
        service = build('classroom', 'v1', credentials=creds)

        listtopics = service.courses().topics().list(courseId=course_id).execute()
        if len(listtopics) == 0:
            return print ("O curso não tem tópicos")
        for i in listtopics['topic']:
            list.append(i['topicId'])
        return list

    except HttpError as error:
        print('An error occurred: %s' % error)

