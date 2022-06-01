from quickstart import main
from googleapiclient.discovery import build
from getCourseId import get_course_id


def notif(courseId):

    creds = main()

    service = build('classroom', 'v1', credentials=creds)

    texto = 'Olá, tudo bem? \n\n Ajude-nos com uma rápida pesquisa sobre como você, professor de ministério infantil, tem utilizado o Inculcar em sua igreja. É apenas uma pergunta, 10 segundos para responder\n\n https://forms.gle/eK7ew6N4yf8sPfkt6 \n\nDesde já, agradecemos. :D'
    
    body =  {
            "text": texto
            }

    service.courses().announcements().create(courseId=courseId,body=body).execute()


list = get_course_id()

for i in list:
    notif(i[0])
    print ('Item postado em '+ i[0])