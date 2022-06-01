from quickstart import main
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SAMPLE_SPREADSHEET_ID = '1a0ZZ_Cq3VtnrBPofuUhSy1z_hIGiEtNm8etRxY0WYl8'
SAMPLE_RANGE_NAME = 'Página1!A1:Q'

creds = main()

def get_course_id():
    try:
            service = build('sheets', 'v4', credentials=creds)

            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=SAMPLE_RANGE_NAME).execute()
            response = result.get('values', [])
            return response

    except HttpError as err:
        print(err)
