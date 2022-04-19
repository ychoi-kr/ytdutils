import sys
import os
from os.path import splitext
import re

from pytube import YouTube
from pytube.cli import on_progress

import ffmpeg


save_dir = "."


def download(video_id):
    url = "https://www.youtube.com/watch?v=" + video_id
    yt = YouTube(url, on_progress_callback=on_progress)
    
    for stream in yt.streams.filter(only_video=True):
        print(stream)

    itag = input("select itag:")
    video = yt.streams.get_by_itag(itag).download()
    video_only = splitext(video)[0] + "(video only)" + splitext(video)[1]
    os.rename(video, video_only)
    
    audio = yt.streams.filter(only_audio=True).order_by("abr").desc().first().download(save_dir)
    audio_only = splitext(audio)[0] + "(audio only)" + splitext(audio)[1]
    os.rename(audio, audio_only)
    return audio_only, video_only, video 


def mix(audio, video, av):
    audio_stream = ffmpeg.input(audio)
    video_stream = ffmpeg.input(video)
    
    ffmpeg.output(audio_stream, video_stream, av).run()


def main(video_id):
    audio, video, av = download(video_id)
    mix(audio, video, av)


if __name__ == '__main__':
    m = re.match(r"https://www.youtube.com/watch[?]v=([A-za-z0-9\-]{11})\\w*", sys.argv[1])
    if m:
        video_id = m.group(1)
    else:
        video_id = sys.argv[1]
    main(video_id)

