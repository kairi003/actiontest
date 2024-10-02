import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import os
import requests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# クレデンシャルファイルのパス
credentials_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
SCOPES = ["https://www.googleapis.com/auth/calendar"]
CALENDAR_ID = "11156d75f2d2f07e20adc131ffc8dd5d467edda9114a6c28f357b03e16578ca2@group.calendar.google.com"

# クレデンシャルをロード
credentials, project = google.auth.load_credentials_from_file(
    credentials_path, scopes=SCOPES)

# アクセストークンをリクエスト
credentials.refresh(Request())

# アクセストークンを取得
access_token = credentials.token
tokeninfo_url = "https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=" + access_token
headers = {"Authorization": "Bearer " + access_token}
resp = requests.get(tokeninfo_url, headers=headers)
print(resp.json())

try:
    service = build("calendar", "v3", credentials=credentials)
    events_result = service.events().list(
        calendarId=CALENDAR_ID, maxResults=3).execute()
    events = events_result.get("items", [])
    print(events)

except HttpError as error:
    print(f"An error occurred: {error}")
