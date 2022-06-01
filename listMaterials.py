# -*- coding: utf-8 -*-
from __future__ import print_function
from pprint import pprint
import os.path
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from deleteMaterials import deleteMaterials
from quickstart import main

def listMaterials(course_id):
    list = []
    creds = main()
    try:
        service = build('classroom', 'v1', credentials=creds)

        listMaterials = service.courses().courseWorkMaterials().list(courseId=course_id).execute()
        if len(listMaterials) == 0:
            return print ("O curso não tem materiais")
        for i in listMaterials['courseWorkMaterial']:
            list.append(i['id'])
        return list           

    except HttpError as error:
        print('An error occurred: %s' % error)


