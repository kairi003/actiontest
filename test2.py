import os.path

from google.auth import load_credentials_from_file
from google.auth.credentials import TokenState
from google.auth.exceptions import GoogleAuthError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.events.owned"]
CALENDAR_ID = "11156d75f2d2f07e20adc131ffc8dd5d467edda9114a6c28f357b03e16578ca2@group.calendar.google.com"

def get_credentials():
    """Get the credentials for the Google Calendar API."""

    # For google-github-actions/auth
    if creds_path := os.environ.get("GOOGLE_GHA_CREDS_PATH"):
        creds, project_id = load_credentials_from_file(creds_path, scopes=SCOPES)
        creds.refresh(Request())
        return creds
    
    # For Local Development
    try:
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        if creds.token_state is TokenState.FRESH:
            # return the credentials if it is fresh
            return creds
        creds.refresh(Request())
    except (GoogleAuthError, FileNotFoundError):
        # If there are no (valid) credentials available, let the user log in.
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
        token.write(creds.to_json())
    return creds

def main():
  creds = get_credentials()

  try:
    service = build("calendar", "v3", credentials=creds)
    events_result = service.events().list(calendarId=CALENDAR_ID, maxResults=3).execute()
    events = events_result.get("items", [])
    print(events)

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()
