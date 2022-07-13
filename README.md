# Coffee-selector

- 제목 : '캡슐커피 취향저격'
- 설명 : 강도, 산미, 취향등에 선택에 따라 캡슐커피를 추천해주는 사이트
- 저장소 : https://github.com/unchaptered/coffee-selector
- 작업표 : https://github.com/users/unchaptered/projects/5
- 기술문서 : README.md 최하단의 기술문서 리스트를 참고해주세요.

<hr>

## 기여자

1. SilverTree 
2. crystal025 
3. JeungHoSub 
4. unchaptered

<hr>

## 폴더 구조

```cmd
root
├ static
│ ├ css
│ └ js
├ templates
│ ├ components
│ └ pages
└ app.py
```

<hr>

## 모듈 리스트

| 모듈명 | 설명 |
| :----- | :--- |
| flask | 프레임워크 |
| Jinja2 | 탬플릿 엔진 |
| python-dotenv | 환경변수 출력 모듈 |
| pymongo, dnspython | MongoDB 커넥터 |
| requests, bs4 | 크롤링용 모듈 |
| PyJWT | JWT 토큰 모듈 |

<hr>

## CDN 링크 모음

1. Bootstrap CSS
2. JQUery, Pooper, BootStrap JS

```javascript
<!-- Bootstrap CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
    crossorigin="anonymous">

<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
    integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
    crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
    integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
    crossorigin="anonymous"></script>
```

<hr>

## 문서들

- ./src/static/static.md / 정적 파일 설명
- ./src/templates/jinja2.md / 탬플릿 엔진 문법 설명
- ./env.py / 환경변수 설정 설명