# -*- coding: utf-8 -*-
from __future__ import print_function

import os.path

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from quickstart import main


def create_topic(courseid,nametopic):
    creds = main()
    try:
        service = build('classroom', 'v1', credentials=creds)

        materials = {'name': (nametopic)}
        topic = service.courses().topics().create(courseId=courseid,body=materials).execute()
        return topic.get('topicId')


    except HttpError as error:
        print('An error occurred: %s' % error)

