유튜브 유틸리티

## 공통

요구사항:

1. 파이썬 3 설치
2. `pip install selenium`
3. 브라우저 종류 및 버전에 맞는 드라이버를 다운로드
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

(Windows인 경우) [FFmpe 설치](https://www.wikihow.com/Install-FFmpeg-on-Windows)

사용법:

다음 명령을 실행하고, 프롬프트에서 itag를 입력

```
$ python youtube_video_download.py <다운로드하려는 영상의 ID>
```

예:

```
$ youtube_video_download ARnG-7ca258
<Stream: itag="315" mime_type="video/webm" res="2160p" fps="60fps" vcodec="vp9" progressive="False" type="video">
<Stream: itag="308" mime_type="video/webm" res="1440p" fps="60fps" vcodec="vp9" progressive="False" type="video">
<Stream: itag="299" mime_type="video/mp4" res="1080p" fps="60fps" vcodec="avc1.64002a" progressive="False" type="video">
...
select itag:315
 ↳ |███                                                               | 4.0%
```
