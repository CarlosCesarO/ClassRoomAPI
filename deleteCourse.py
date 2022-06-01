from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from quickstart import main

def deletecourse(id):
    creds = main()
    try:
        service = build('classroom', 'v1', credentials=creds)

        # Call the Classroom API
        results = service.courses().list(pageSize=10).execute()
        courses = results.get('courses', [])

        service.courses().delete(id=id).execute()
        
    except HttpError as error:
        print('An error occurred: %s' % error)

