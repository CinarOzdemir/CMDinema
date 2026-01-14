# Introducing: CMDinema
<img width="704" height="384" alt="Gemini_Generated_Image_vtkv4vvtkv4vvtkv" src="https://github.com/user-attachments/assets/a0a48084-139e-449a-862b-9c5ab835181b" />

A video player that runs entirely in the terminal. It converts each frame to ASCII art and displays it like that.

## See it in Action:

[![YouTube](https://github.com/user-attachments/assets/fd10dabb-bc57-4623-80a3-5ac6878a905f)](https://www.youtube.com/watch?v=bEEgs1xJj1k)

## Features:
1) Instant play (No waiting for the video to load; the frames are generated as the video plays)
2) Dynamic resolution (The resolution of the video is calculated based on the size of the terminal. Zoom in or out for different resolutions)
3) Live feed (When no source is given, the camera is used as input. Protip: Try it with OBS Virtual-Cam)
4) Simple (No GUI, no problem)

## How to use
1) Install opencv
```
pip install opencv-python
```
2) Run it (If no path is given, the webcam will be used as the source)
```
python grayscale_player.py [video_path]
```

## New features I might add later (have a go yourself)
1) Colored video
2) Audio playback
3) Frame-skipping
4) Faster computing for higher resolution
5) Turn it into an application and make it the default
