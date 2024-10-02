import datetime
import json
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.events.owned"]
CALENDAR_ID = "11156d75f2d2f07e20adc131ffc8dd5d467edda9114a6c28f357b03e16578ca2@group.calendar.google.com"

def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  service_account_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
  creds = service_account.Credentials.from_service_account_file(service_account_path)

  try:
    service = build("calendar", "v3", credentials=creds)
    events_result = service.events().list(calendarId=CALENDAR_ID, maxResults=3).execute()
    events = events_result.get("items", [])
    print(events)

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()
