# -*- coding: utf-8 -*-
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from quickstart import main
from getArchive import includeArchives
from curriculos import list

def getSaladeAula(lessons,numberlesson,topicid,nomeTopico):
                    for i in lessons:
                        if i.get('title') == "Sala de Aula "+nomeTopico+" "+str(numberlesson):
                            list = includeArchives("Sala de Aula "+nomeTopico+" "+str(numberlesson))
                            i['materials']=list
                            i['topicId']=topicid
                            return i

def getRoteiroAtiv(lessons,numberlesson,topicid,nomeTopico):
                    for i in lessons:
                        if i.get('title') == "Roteiro e Atividades "+nomeTopico+" "+str(numberlesson):
                            list = includeArchives("Roteiro e Atividades "+nomeTopico+" "+str(numberlesson))
                            i['materials']=list
                            i['topicId']=topicid
                            return i

def getVideoaula(lessons,numberlesson,topicid,nomeTopico):
                    for i in lessons:
                        if i.get('title') == "Videoaula "+nomeTopico+" "+str(numberlesson):
                            list = includeArchives("Videoaula "+nomeTopico+" "+str(numberlesson))
                            i['materials']=list
                            i['topicId']=topicid
                            return i

def getDevocionais(lessons,numberlesson,topicid,nomeTopico):
                    for i in lessons:
                        if i.get('title') == "Devocionais "+nomeTopico+" "+str(numberlesson):
                            list = includeArchives("Devocionais "+nomeTopico+" "+str(numberlesson))
                            i['materials']=list
                            i['topicId']=topicid
                            return i


def getImagensdeApoio(lessons,numberlesson,topicid,nomeTopico):
                    for i in lessons:
                        if i.get('title') == "Imagens de Apoio "+nomeTopico+" "+str(numberlesson):
                            list = includeArchives("Imagens de Apoio "+nomeTopico+" "+str(numberlesson))
                            i['materials']=list
                            i['topicId']=topicid
                            return i

def getIntro(lessons,numberlesson,topicid,nomeTopico):
                    for i in lessons:
                        if i.get('title') == "Introdução "+nomeTopico+" "+str(numberlesson):
                            list = includeArchives("Introdução "+nomeTopico+" "+str(numberlesson))
                            i['materials']=list
                            i['topicId']=topicid
                            return i

def getPanoram(lessons,numberlesson,topicid,nomeTopico):
                    for i in lessons:
                        if i.get('title') == "Panorama "+nomeTopico+" "+str(numberlesson):
                            list = includeArchives("Panorama "+nomeTopico+" "+str(numberlesson))
                            i['materials']=list
                            i['topicId']=topicid
                            return i

def getNonCurriculum(lessons,numberlesson,topicid,nomeTopico):
                    for i in lessons:
                        if i.get('title') == "Linha do Tempo "+nomeTopico+" "+str(numberlesson): #MUDE PARA A PALAVRA QUE ACHAR MELHOR, SO LEMBRE DE CRIAR A PASTA IGUAL
                            list = includeArchives("Linha do Tempo "+nomeTopico+" "+str(numberlesson)) #MUDE PARA A PALAVRA QUE ACHAR MELHOR, SO LEMBRE DE CRIAR A PASTA IGUAL
                            i['materials']=list
                            i['topicId']=topicid
                            return i

def create_saladeaula(lessons,course_id,numberlesson,topicid,nomeTopico):

    creds = main()

    try:
        service = build('classroom', 'v1', credentials=creds)
        materials = getSaladeAula(lessons,numberlesson, topicid, nomeTopico)
        material = service.courses().courseWorkMaterials().create(courseId=course_id,body=materials).execute()

    except HttpError as error:
        print('Preencha os dados para "Sala de Aula '+nomeTopico+' '+str(numberlesson)+'"')

def create_roteiroativ(lessons,course_id,numberlesson,topicid,nomeTopico):

    creds = main()

    try:
        service = build('classroom', 'v1', credentials=creds)
        materials = getRoteiroAtiv(lessons,numberlesson, topicid, nomeTopico)
        material = service.courses().courseWorkMaterials().create(courseId=course_id,body=materials).execute()

    except HttpError as error:
        print('Preencha os dados para "Roteiro e Atividades '+nomeTopico+' '+str(numberlesson)+'"')
    
def create_videoaula(lessons,course_id,numberlesson,topicid,nomeTopico):

    creds = main()

    try:
        service = build('classroom', 'v1', credentials=creds)
        materials = getVideoaula(lessons,numberlesson, topicid, nomeTopico)
        material = service.courses().courseWorkMaterials().create(courseId=course_id,body=materials).execute()


    except HttpError as error:
        print('Preencha os dados para "Videoaula '+nomeTopico+' '+str(numberlesson)+'"')

def create_imagensdeapoio(lessons,course_id,numberlesson,topicid,nomeTopico):

    creds = main()

    try:
        service = build('classroom', 'v1', credentials=creds)
        materials = getImagensdeApoio(lessons,numberlesson, topicid, nomeTopico)
        material = service.courses().courseWorkMaterials().create(courseId=course_id,body=materials).execute()

    except HttpError as error:
        print('Preencha os dados para "Imagens de apoio '+nomeTopico+' '+str(numberlesson)+'"')

def create_devocionais(lessons,course_id,numberlesson,topicid,nomeTopico):

    creds = main()

    try:
        service = build('classroom', 'v1', credentials=creds)
        materials = getDevocionais(lessons,numberlesson, topicid, nomeTopico)
        material = service.courses().courseWorkMaterials().create(courseId=course_id,body=materials).execute()

    except HttpError as error:
        print('Preencha os dados para "Devocionais '+nomeTopico+' '+str(numberlesson)+'"')

def create_intro(lessons,course_id,numberlesson,topicid,nomeTopico):

    creds = main()

    try:
        service = build('classroom', 'v1', credentials=creds)
        materials = getIntro(lessons,numberlesson,topicid, nomeTopico)
        material = service.courses().courseWorkMaterials().create(courseId=course_id,body=materials).execute()

    except HttpError as error:
        print('Preencha os dados para "Introdução '+nomeTopico+' '+str(numberlesson)+'"')

def create_panoram(lessons,course_id,numberlesson,topicid,nomeTopico):

    creds = main()

    try:
        service = build('classroom', 'v1', credentials=creds)
        materials = getPanoram(lessons,numberlesson,topicid, nomeTopico)
        material = service.courses().courseWorkMaterials().create(courseId=course_id,body=materials).execute()

    except HttpError as error:
        print('Preencha os dados para "Panorama '+nomeTopico+' '+str(numberlesson)+'"')

def create_noncurriculum(lessons,course_id,numberlesson,topicid,nomeTopico):

    creds = main()

    try:
        service = build('classroom', 'v1', credentials=creds)
        materials = getNonCurriculum(lessons,numberlesson,topicid, nomeTopico)
        material = service.courses().courseWorkMaterials().create(courseId=course_id,body=materials).execute()

    except HttpError as error:
        print('Preencha os dados para "Non Curriculum '+nomeTopico+' '+str(numberlesson)+'"')
