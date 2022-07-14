# Coffee-selector

![](./preview.jpeg)

> [사이트 방문하기](http://coffe-selector.shop/) - coffee-selector.shop <br>
> [유투브 영상 보기](https://youtu.be/PZmnmWDcpUE) - www.youtube.com/watch?v=PZmnmWDcpUE

- 제목 : '캡슐커피 취향저격'
- 설명 : 강도, 산미, 취향등에 선택에 따라 캡슐커피를 추천해주는 사이트
- 일정표 : [취향저격 커피추천 - git projects](https://github.com/users/unchaptered/projects/5)
- 서버 저장소 : [Coffee Selector - git repository](https://github.com/unchaptered/coffee-selector)
- 크롤링 저장소 : [Coffe Selector Selenium - git repository](https://github.com/unchaptered/coffee-selector-selenium)
- 기술 문서
    - Github 사용법
    - Github 커밋 규칙
    - Jinja2 설명
    - Troulbe 이슈 리스트
        - Git 사용 어려움
        - Git pull 할 때마다, Python 인터프리터 연결이 해제되는 경우
        - Nespresso 사이트 크롤링 거부
        - 팀원들 간에 특정 변수가 달라져야 했던 이유
        - MongoDB Atlas 함수가 작동하지 않았던 경우
        - PyJwt.decode 가 AWS 에서만 에러가 일으키는 경우
    - Javascript 함수 설명
        - swithcer 함수
        - prototpye 이란
        - destructuring 이란
    - Pyhton 구현 설명
        - Authentication
- 프로젝트 기간 : `2022-07-11` ~ `2022-07-14` (4일 간)

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
│ ├ layout
│ └ pages
├ src/modules
├ database.py
└ app.py
```

<hr>

## 모듈 리스트

| 모듈명 | 설명 |
| :----- | :--- |
| flask | 프레임워크 |
| Jinja2 | 탬플릿 엔진 |
| python-dotenv | 환경변수 출력 모듈 |
| PyJWT | JWT 토큰 모듈 |
| Bcrypt-Flask | 비밀번호 암호화 모듈(단방향) |

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