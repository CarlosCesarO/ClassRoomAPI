from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from quickstart import main
# from deleteCourse import deletecourse

def listCourse():
    try:
        list = []
        creds = main()
        service = build('classroom', 'v1', credentials=creds)

        results = service.courses().list(pageSize=10).execute()
        courses = results.get('courses', [])
        
        if not courses:
            print('Nenhum curso encontrado.')

        else:
            for course in courses:
                list.append(course.get('id'))
                return list


    except HttpError as error:
        print('An error occurred: %s' % error)


