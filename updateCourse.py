from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from quickstart import main

def update_course(course_id):

    creds = main()
    try:
        service = build('classroom', 'v1', credentials=creds)

        course = service.courses().get(id=course_id).execute()
        course['courseState'] = 'archived'
        course = service.courses().update(id=course_id, body=course).execute()

    except HttpError as error:
        print('An error occurred: %s' % error)
        return error
