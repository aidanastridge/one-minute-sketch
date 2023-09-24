#This script as of right now only captures a random frame out of a downloaded video.
#I will be creating an app that can take a video from youtube that shows a random frame for a minute.
#Intended for electronic music videos

import os
import random
import cv2
from pytube import YouTube
from PIL import Image
from PIL import ImageShow

# Replace with the URL of the YouTube video you want to capture a frame from
video_url = "https://www.youtube.com/watch?v="

# Define the output directory where the video will be downloaded
output_dir = "downloaded_videos"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Download the YouTube video
yt = YouTube(video_url)
video_stream = yt.streams.filter(file_extension="mp4", res="720p").first()
video_filename = os.path.join(output_dir, yt.title + ".mp4")
video_stream.download(output_path=output_dir)

# Open the downloaded video and capture a random frame
cap = cv2.VideoCapture(video_filename)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
random_frame_number = random.randint(0, frame_count - 1)

# Set the frame number to the random frame
cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame_number)

# Read the frame
ret, frame = cap.read()

if ret:
    # Save the random frame as an image
    random_frame_filename = os.path.join(output_dir, "random_frame.png")
    cv2.imwrite(random_frame_filename, frame)
    print(f"Random frame saved as {random_frame_filename}")
else:
    print("Error capturing random frame")

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()

# Open the image
image_path = "./downloaded_videos/random_frame.png"  # Replace with the path to your image file
image = Image.open(image_path)

# Display the image using the default image viewer
ImageShow.show(image)
