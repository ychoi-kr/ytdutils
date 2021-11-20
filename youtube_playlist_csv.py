#!/usr/bin/python

import argparse
from youtube import YouTube


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("playlist_id")
    args = parser.parse_args()
    
    yt = YouTube()

    for row in yt.playlist(args.playlist_id):
        dquo = "\""
        print(','.join(map(lambda x: dquo + x + dquo, row)))
    
    yt.quit()
