import tkinter as tk
from google.oauth2 import service_account
from googleapiclient.discovery import build
import webbrowser
import random

# Set up API credentials
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
#How to create your service account file(json) tutorial: https://www.youtube.com/watch?v=rWcLDax-VmM
SERVICE_ACCOUNT_FILE = 'Check_the_video_above_to_see_how_to_create'

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Set up API client
youtube = build('youtube', 'v3', credentials=creds)

def get_random_comment():
    # Retrieve comments for the video
    video_id = video_id_entry.get()
    comments = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText'
    ).execute()

    # Randomly select a comment
    comment = random.choice(comments['items'])

    # Extract commenter name and comment text
    commenter_name = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
    comment_text = comment['snippet']['topLevelComment']['snippet']['textDisplay']

    # Update the labels with the selected comment
    commenter_name_label.config(text=f'Commenter: {commenter_name}')
    comment_text_label.config(text=f'Comment: {comment_text}')

    # Store the commenter channel ID
    commenter_channel_id = comment['snippet']['topLevelComment']['snippet']['authorChannelId']['value']
    
    # Enable the "View Profile" button
    view_profile_button.config(state=tk.NORMAL, command=lambda: view_commenter_profile(commenter_channel_id))

def view_commenter_profile(channel_id):
    # Open the commenter's YouTube channel in the default web browser
    webbrowser.open(f'https://www.youtube.com/channel/{channel_id}')

# Create main window
root = tk.Tk()
root.title('Random YouTube Comment Viewer')

# Create widgets
video_id_label = tk.Label(root, text='Enter the video ID:')
video_id_entry = tk.Entry(root)
get_comment_button = tk.Button(root, text='Get Random Comment', command=get_random_comment)
commenter_name_label = tk.Label(root, text='')
comment_text_label = tk.Label(root, text='')
view_profile_button = tk.Button(root, text='View Profile', state=tk.DISABLED)

# Add widgets to window
video_id_label.pack()
video_id_entry.pack()
get_comment_button.pack()
commenter_name_label.pack()
comment_text_label.pack()
view_profile_button.pack()

# Run the main loop
root.mainloop()
