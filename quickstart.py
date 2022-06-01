# -*- coding: utf-8 -*-
from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account

scopes = [
'https://www.googleapis.com/auth/classroom.courses.readonly',
'https://www.googleapis.com/auth/classroom.courses',
'https://www.googleapis.com/auth/classroom.coursework.students',
'https://www.googleapis.com/auth/classroom.courseworkmaterials',
'https://www.googleapis.com/auth/classroom.topics.readonly',
'https://www.googleapis.com/auth/classroom.topics',
'https://www.googleapis.com/auth/classroom.rosters',
'https://www.googleapis.com/auth/classroom.profile.emails',
'https://www.googleapis.com/auth/classroom.profile.photos',
'https://www.googleapis.com/auth/drive',
'https://www.googleapis.com/auth/drive.file',
'https://www.googleapis.com/auth/drive.readonly',
'https://www.googleapis.com/auth/drive.metadata.readonly',
'https://www.googleapis.com/auth/drive.appdata',
'https://www.googleapis.com/auth/drive.metadata',
'https://www.googleapis.com/auth/drive.photos.readonly',
'https://www.googleapis.com/auth/classroom.announcements',
'https://www.googleapis.com/auth/spreadsheets.readonly', 
'https://www.googleapis.com/auth/spreadsheets',
]


#OAUTH2
def main():

    creds = None

    if os.path.exists('token.json'):

        creds = Credentials.from_authorized_user_file('token.json',scopes=scopes)

        return creds

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())



#SERVICE ACCOUNT
# def main():

#     creds = None

#     creds = service_account.Credentials.from_service_account_file('service-account.json', scopes=scopes,  subject='contato@projetobiblia.com.br')

#     return creds