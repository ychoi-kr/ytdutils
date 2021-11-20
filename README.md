유튜브 유틸리티

## 공통

요구사항:

1. 파이썬 3 설치
2. `pip install selenium`
3. 브라우저 종류 및 버전에 맞는 드라이버를 다운로드
    - 크롬: https://chromedriver.chromium.org/downloads


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
