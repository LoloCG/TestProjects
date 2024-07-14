# https://www.youtube.com/watch?v=rtLZBKNExLQ
import yt_dlp

# Replace with the actual m3u8 URL you found
m3u8_url = ''  # Replace with actual m3u8 URL
referer = '' # Paste the URL of the tab that contains solely the video player
format = 'mkv'

# Define the options for yt_dlp
ydl_opts = {
    'format': 'best',
    'merge_output_format': format,
    'outtmpl': '%(title)s.%(ext)s',
    'referer': referer,
    'writeautomaticsub': True,  # Download automatic captions/subtitles if available.
    'subtitleslangs': ['en', 'esp']
}

# Create a YoutubeDL object with the options
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    # Download the video
    ydl.download([m3u8_url])
# ===== EXAMPLES =====
# --- VOE Server/jasminetesttry ---
'''
1. Click on the play icon of the video.
2. Right-click on the video, select "This Frame", then choose "Open Frame in New Tab".
3. Copy the URL from the address bar of the newly opened tab to use as the referer.
4. Press F12 to open the Developer Tools, and select the "Network" tab.
5. Reload the page by pressing F5 to show all network connections.
6. Look for a URL containing "m3u8" in the list of network requests, then copy this URL.
7. Paste the copied m3u8 URL into the m3u8_url variable in your script.
8. Run the script to download the video.
'''

'''
'format':

    'bestvideo': Downloads the best video-only format.
    'bestaudio': Downloads the best audio-only format.
    'worst': Downloads the lowest quality available.
    You can also specify formats explicitly, like 'mp4', 'webm', etc.

Video Formats:
    mp4
    webm
    flv
    3gp
    avi
    mkv

Audio Formats:
    mp3
    aac
    vorbis
    opus
    m4a
    wav
'''