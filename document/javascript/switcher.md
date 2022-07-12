# Switcher 란 무엇인가?

본 문서에는 다음의 내용이 포함되었습니다.

- [ 1 ] 왜 이 코드를 작성했는가?
- [ 2 ] 어떠한 방식으로 코드를 구성했는가?
- [ 3 ] 프로젝트에서의 실제 코드는 어떠한가?

    - [ 3.A ] 구현하고 싶었던 부분
    - [ 3.B ] 설계 및 구현

        - [ 3.B.가 ] Valid / Invalid

        - [ 3.B.나 ] 이름 / 비밀번호 / 비밀번호 확인

        - [ 3.B.다 ] 최종적인 코드 형태
- [ 4 ] 결론

> 이러한 기법이 최선 - 최악의 기법인지는 모르겠으나, if-else 보다 볻기 좋아서 사용하는 방법입니다.

<br>
<hr>
<br>

## 1. 왜 이 코드를 작성했는가?

특정한 기능 구현의 경우 N 개 이상의 분기점이 발생됩니다.

이러한 분기점을 switch 문이나 if - else 문으로 나누는 것이 별로라고 생각했습니다.

그 이유는 다음과 같은데

1. 코드가 길어지고 난잡하다.
2. 분기점 별로 사용되는 변수의 종류와 수가 달라질 수 있다.

<br>
<hr>
<br>

## 2. 어떠한 방식으로 코드를 구성했는가?

따라서 이러한 문제점을 해결하기 위해서 Switcher 라고 하는 프로로타입 객체를 만들어 사용하였습니다.

```javascript
const request_1번 = {
    mode: 'guest'
}
const request_2번 = {
    mode: 'user',
    name: 'unchaptered',
    password: 'hello',
}
const request_3번 = {
    mode: 'admin',
    privateKey: 'asmfklmaslkdfmaklfd'
}

const switcher = {
    /* 여기서 guest: 가 아니라 'guest' 인 것은 다음과 같은 이유입니다.
        guest 로 할 경우 : switcher.guest, -.user 등으로 호출 가능하나, 함수 형으로 호출함으로써 매개변수 전달이 불가능합니다.
        'guest' 로 할 경우 : switcher.'guest' 가 불가능해지지만, 함수 형으로 호출함으로써 매개변수 전달이 가능해집니다.
    */
    'guest': ({ ...params }) => 익명_로그인_함수(params)
    'user': ({ ...params }) => 유저_로그인_함수(params)
    'password': ({ ...params }) => 관리자_로그인_함수(params)
}

// 예시1
switcher['guest'](넘겨받은_변수들)
switcher['user'](넘겨받은_변수들)

// 분기점 예시 : 아래 친구가 mode 의 값에 따라서 다른 함수로 연결해주고 값을 반환받는다.
switcher[mode](params)
```

<br>
<hr>
<br>

## 3. 프로젝트에서의 실제 코드는 어떠한가?

프로젝트에서는 다음과 같이 두 개의 Switcher 함수를 구현했습니다.

- static/js/controller/dom.controller.js
- static/js/validator/form.validator.js

이 중에서 유효성 검사와 관련된 내용을 설명해보겠습니다.

> - [Local 환경에서 파일 열기](../../static/js/validator/form.validaor.js)
> - [Origin 환경에서 파일 열기]()

### 3.A. 구현하고 싶었던 부분

1. 유효하지 않은 값 전달 시, 붉은 색으로 표기
    > Bootstrap 의 [일반적인 Input 태그](https://getbootstrap.com/docs/5.0/forms/form-control/#readonly-plain-text) 의 경우 클릭하면, `input:focus`, 테두리가 파랑색으로 변합니다.
    > 이 색깔을 붉은 색으로 변경시키고 싶었습니다.
2. 3 가지 케이스, `이름, 비밀번호, 비밀번호 확인`, 에 따라서  DOM 을 id 값으로 찾아서 붉은색으로 표시할 수 있는 확장성 있는 함수 구현
3. 2 가지 케이스, `Valid(유효) / Invalid(유효하지 않음)`, 에 따라서 $('#ID') 가 가지고 있는 removeClass 와 addClass 를 호출

즉, 6가지에 해당하는 기능을 최대한 줄이고 싶었습니다.

### 3.B. 설계 및 구현

1. Valid / Invalid
2. 이름 / 비밀번호 / 비밀번호 확인

#### 3.B.가. Valid / Invalid

if-else 를 통해서 첫 번째 분기처리.

```javascript
const classSwitcher = (isValid, target) => {
    if (isValid) // 유효하기 때문에, 붉은 색을 표기하는 클래스를 제거
    else // 유효하지 않기 때문에, 붉은 색을 표시하는 클래스를 추가
}
```

#### 3.B.나. 이름 / 비밀번호 / 비밀번호 확인

```javascript
const switcher = {
    'name': () => // #name 을 id로 가지는 <Input/>의 클래스를 삭제
    'password': () => // #password 를 id로 가지는 <Input/>의 클래스를 삭제
    'passwordConfirm': () => // #passwordConfirm 을 id 로 가지는 <Input/>의 클래스를 삭제
}

switcher[target]();
```

#### 3.B.다. 최종적인 코드 형태

```javascript
// 유효성 검사에 따라 분기 처리 함수
const classSwitcher = (isValid, target) => {
    if (isValid) classRemover(target);
    else classApplier(target);
}

// 클래스 제거용 함수
const classRemover = (target) => {
    const switcher = {
        'name': () => $('#name').removeClass(invalidColor),
        'password': () => $('#password').removeClass(invalidColor),
        'passwordConfirm': () => $('#passwordConfirm').removeClass(invalidColor)
    }
    switcher[target]();
}

// 클래스 추가/반영용 함수
const classApplier = (target) => {
    const switcher = {
        'name': () => $('#name').addClass(invalidColor),
        'password': () => $('#password').addClass(invalidColor),
        'passwordConfirm': () => $('#passwordConfirm').addClass(invalidColor),
    }
    switcher[target]();
}
```

<br>
<hr>
<br>

## 4. 결론

결과적으로 switch 구문을 없앨 수 있었으나, **직관적이지 않은 점** 이 거슬립니다.