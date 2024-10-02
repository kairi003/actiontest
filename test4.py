import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import os
import requests

# クレデンシャルファイルのパス
credentials_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
SCOPES = ["https://www.googleapis.com/auth/calendar.events.owned"]

# クレデンシャルをロード
credentials, project = google.auth.load_credentials_from_file(credentials_path, scopes=SCOPES)

# アクセストークンをリクエスト
credentials.refresh(Request())

# アクセストークンを取得
access_token = credentials.token
tokeninfo_url = "https://www.googleapis.com/oauth2/v3/tokeninfo?access_token=" + access_token
headers = { "Authorization": "Bearer " + access_token }
resp = requests.get(tokeninfo_url, headers=headers)
print(resp.json())
