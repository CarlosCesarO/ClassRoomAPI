# -*- coding: utf-8 -*-
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from quickstart import main

def includeArchives(name):
    list = []
    archives = get_archives(name)
    if archives == 0:
        return 0
    if archives != None:
        for i in archives:
            list.append({"driveFile": {"driveFile": {"id": str(i)}}})
        return list

def getIdfolder(name):
    creds = main()
    service = build('drive', 'v3', credentials=creds)
    name = "name = '"+name+"'"
    response = service.files().list(spaces='drive', q=name).execute()
    for file in response.get('files', []):
        idfolder = file.get('id')
        return idfolder

def get_archives(name):

    creds = main()
    try:
        idfolder = getIdfolder(name)
        service = build('drive', 'v3', credentials=creds)
        if idfolder == None:
            return 0
        idfolder = "'"+idfolder+"' in parents and trashed=false"

        archive = service.files().list(q=idfolder).execute()
        archives = []

        if len(archive.get('files')) != 0:
            for i in archive.get('files'):
                archives.append((i.get('id')))
            return archives
        else:
            print('Não tem a pasta ou os arquivos na pasta '+name)

    except HttpError as error:
        print('An error occurred: %s' % error)

