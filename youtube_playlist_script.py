#!/usr/bin/python

import argparse
from youtube import YouTube


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("playlist_id")
    args = parser.parse_args()
    
    yt = YouTube()
    yt.playlist_script(args.playlist_id)
    yt.quit()
