유튜브 유틸리티

## 공통

요구사항:

1. 파이썬 3 설치
2. 일부 스크립트의 경우(youtube_playlist_csv.py, youtube_script.py, youtube_playlist_script.py)
   * `pip install selenium`
   * 브라우저 종류 및 버전에 맞는 드라이버를 다운로드
      - 크롬: https://chromedriver.chromium.org/downloads

주의: **코드 사용에 따른 모든 책임은 사용자에게 있습니다.**


## youtube_playlist_csv.py

재생목록을 CSV 형태로 출력합니다.

사용법:

```
youtube_playlist_csv <재생목록 ID>
```

예: `youtube_playlist_csv.py PLblu-CA4SK5If2K1rFjasO_Z4k1_Av80H`

CSV 파일을 생성하려면 리다이렉션을 이용하면 됩니다.

예: `youtube_playlist_csv.py PLblu-CA4SK5If2K1rFjasO_Z4k1_Av80H > playlist.csv`


## youtube_script.py

영상의 자막을 출력합니다.

사용법:

```
youtube_script.py <영상 ID>
```

예: `youtube_script.py mk8lP7WLQ9E`


## youtube_playlist_script.py

재생목록에 있는 모든 영상의 자막을 출력합니다.

사용법:

```
youtube_playlist_script.py <재생목록 ID>
```

예: `youtube_playlist_script.py PLblu-CA4SK5If2K1rFjasO_Z4k1_Av80H`


## youtube_video_download.py

유튜브 영상을 다운로드합니다. 고해상도(4K) 영상을 다운로드하기 위해서는 영상과 음성 파일을 각각 다운로드한 후에 합치는 과정이 필요한데, 이를 자동화한 것입니다.

요구사항:

```
$ pip install ffmpeg-python
$ pip install pytube
```

(Windows인 경우) [FFmpeg 설치](https://www.wikihow.com/Install-FFmpeg-on-Windows)

사용법:

다음 명령을 실행하고, 프롬프트에서 itag를 입력

```
$ python youtube_video_download.py <다운로드하려는 영상의 ID>
```

예:

(스크립트 실행)

```
$ youtube_video_download ARnG-7ca258
<Stream: itag="315" mime_type="video/webm" res="2160p" fps="60fps" vcodec="vp9" progressive="False" type="video">
<Stream: itag="308" mime_type="video/webm" res="1440p" fps="60fps" vcodec="vp9" progressive="False" type="video">
<Stream: itag="299" mime_type="video/mp4" res="1080p" fps="60fps" vcodec="avc1.64002a" progressive="False" type="video">
...
select itag:
```

(itag를 입력하면 영상과 음성 파일 다운로드 시작)

```
select itag:315
 ↳ |███                                                               | 4.0%
```

(다운로드 완료 후 인코딩 시작. 시간이 오래 걸릴 수 있음에 유의.)

```
Output #0, webm, to 'D:\Videos\[생활 속 운동] 자전거 한강 라이딩 - 오즈모 포켓 4K 60fps.webm':
  Metadata:
    encoder         : Lavf59.20.101
  Stream #0:0(eng): Audio: opus, 48000 Hz, stereo, flt, 96 kb/s (default)
    Metadata:
      encoder         : Lavc59.25.101 libopus
  Stream #0:1(eng): Video: vp9, yuv420p(tv, bt709, progressive), 3840x2160 [SAR 1:1 DAR 16:9], q=2-31, 59.94 fps, 1k tbn (default)
    Metadata:
      encoder         : Lavc59.25.101 libvpx-vp9
    Side data:
      cpb: bitrate max/min/avg: 0/0/0 buffer size: 0 vbv_delay: N/A
frame=  573 fps=4.6 q=27.0 size=   14592kB time=00:00:09.18 bitrate=13020.1kbits/s speed=0.0731x
```

