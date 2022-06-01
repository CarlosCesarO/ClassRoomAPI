# -*- coding: utf-8 -*-
from __future__ import print_function

import os.path

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from quickstart import main

def deleteMaterials(course_id,id):
    creds = main()
    try:
        service = build('classroom', 'v1', credentials=creds)

        course = service.courses().courseWorkMaterials().delete(courseId=course_id,id=id).execute()


    except HttpError as error:
        print('An error occurred: %s' % error)


