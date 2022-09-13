# DiscordVideoBait
This simple script concatenates a 0.1 second image right before a video, useful for creating those "Discord bait videos".

#WINDOWS ONLY#

### HOW TO USE ###

Open command prompt and go to the location of the script.

Example:
python baiter.py -b (image_path) (video_path) "Will concatenate your image at the beginning of the video"<br />
python baiter.py -b (image_path) (video_path) -o filename.webm "Will save the output file as filename.webm, this argument is optional and the program will save your file as output.webm if not given"<br />

### REQUIREMENTS ###

pip install moviepy
or
pip3 install moviepy
