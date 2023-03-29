from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set up API credentials
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
#How to create your service account file(json) tutorial: https://www.youtube.com/watch?v=rWcLDax-VmM
SERVICE_ACCOUNT_FILE = 'Check_the_video_above_to_see_how_to_create'

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Set up API client
youtube = build('youtube', 'v3', credentials=creds)

# Define video ID here
video_id = 'AKeUssuu3Is'

# Retrieve video statistics
response = youtube.videos().list(
        part='statistics',
        id=video_id
).execute()

# Extract view count from response
view_count = response['items'][0]['statistics']['viewCount']
print(f'The video with ID {video_id} has {view_count} views.')
