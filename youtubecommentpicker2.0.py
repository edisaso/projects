import tkinter as tk
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import webbrowser
import re

# Set up API credentials
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
DEVELOPER_KEY = '-----------'

# Set up API client
youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=DEVELOPER_KEY)

def get_random_comment():
    # Retrieve video ID from input field
    video_url = video_id_entry.get()
    video_id = extract_video_id(video_url)
    
    try:
        # Retrieve comments for the video
        comments = get_video_comments(video_id)
        
        # Choose a random comment
        random_comment = choose_random_comment(comments)
        
        # Update the UI to show the commenter and comment
        commenter_label.config(text=f'Commenter: {random_comment["authorDisplayName"]}')
        comment_label.config(text=f'Comment: {random_comment["textDisplay"]}')
        
        # Store the commenter channel ID for opening the profile later
        global commenter_channel_id
        commenter_channel_id = random_comment['authorChannelId']['value']
        
    except HttpError as error:
        print(f'An error occurred: {error}')
        commenter_label.config(text='Error occurred while retrieving comments.')
        comment_label.config(text='')

def open_commenter_profile():
    # Open the profile of the commenter in a web browser
    webbrowser.open(f'https://www.youtube.com/channel/{commenter_channel_id}')

def extract_video_id(url):
    # Extract video ID from YouTube URL
    video_id_regex = r'(?<=v=)[^&#]+'
    return re.search(video_id_regex, url).group(0)

def get_video_comments(video_id):
    # Retrieve comments for the video
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText'
    ).execute()

    comments = []
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append(comment)

    return comments

def choose_random_comment(comments):
    # Choose a random comment from the list of comments
    import random
    return random.choice(comments)

# Create main window
root = tk.Tk()
root.title('Random YouTube Comment Picker')

# Create widgets
video_id_label = tk.Label(root, text='Enter the YouTube video URL:')
video_id_entry = tk.Entry(root)
get_comment_button = tk.Button(root, text='Get Random Comment', command=get_random_comment)
commenter_label = tk.Label(root, text='')
comment_label = tk.Label(root, text='')
open_profile_button = tk.Button(root, text='Open Commenter Profile', command=open_commenter_profile)

# Add widgets to window
video_id_label.pack()
video_id_entry.pack()
get_comment_button.pack()
commenter_label.pack()
comment_label.pack()
open_profile_button.pack()

# Run the main loop
root.mainloop()
