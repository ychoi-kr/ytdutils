#!/usr/bin/python

import argparse
from youtube import YouTube

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("video_id")
    args = parser.parse_args()

    yt = YouTube()
    print(yt.script(args.video_id))
    yt.quit()
