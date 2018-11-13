from subprocess import Popen, PIPE
from PIL import Image


def stream(video):
    i = 0
    p = Popen(['ffmpeg', '-y', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-r', '24', '-i', '-', '-vcodec', 'mpeg4', '-vf',
               'format=yuv420p', '-video_size', '480x640', 'http://localhost:8090/feed1.ffm'], stdin=PIPE)
    while video.isOpened():
        i = i + 1
        ret, frame = video.read()
        if ret:
            im = Image.fromarray(frame)
            im.save(p.stdin, 'JPEG')
        else:
            break

# ffmpeg combines opencv frames to the video and streams it to ffserver
# ffserver is a streaming server for both audio and video. It supports several live feeds,
# streaming from files and time shifting on live feeds.
# isntall ffserver, ffmpeg
# put ffserver.conf to /etc/ffserver.conf
# run ffserver
