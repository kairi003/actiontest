from google.oauth2 import service_account
import google.auth.transport.requests
import google.auth.credentials
from google.oauth2 import credentials

# 鍵ファイルのパスを指定
SERVICE_ACCOUNT_FILE = 'sa.json'

# 使用するスコープを指定（例：Cloud Storage）
SCOPES = ['https://www.googleapis.com/auth/calendar.events.owned']

# サービスアカウントの認証情報を取得
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

credentials.from_service_account_info
# リクエストオブジェクトを作成
request = google.auth.transport.requests.Request()

# アクセストークンを取得
credentials.refresh(request)
access_token = credentials.token

# アクセストークンを表示
print(access_token, end='')
