import sys
from pathlib import Path
import os

from pytube import YouTube
from pytube.cli import on_progress

import ffmpeg


save_dir = "."


def download(video_id):
    url = "https://www.youtube.com/watch?v=" + video_id
    yt = YouTube(url, on_progress_callback=on_progress)
    
    vfile = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(save_dir)
    title = Path(vfile).stem
    print("title", title)
    os.rename(vfile, title + "(video only).mp4")
    
    afile = yt.streams.filter(only_audio=True).order_by("abr").desc().first().download(save_dir)
    os.rename(afile, title + "(audio only).mp4")
    return title


def mix(title):
    video_stream = ffmpeg.input(title + "(video only).mp4")
    audio_stream = ffmpeg.input(title + "(audio only).mp4")
    ffmpeg.output(audio_stream, video_stream, title + '.mp4').run()


def main(video_id):
    title = download(video_id)
    mix(title)


if __name__ == '__main__':
    main(sys.argv[1])

