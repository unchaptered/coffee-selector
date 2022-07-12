# Prototype 이란 무엇인가?

JS 에는 크게 두 부류의 데이터 타입이 있습니다.

1. Primitive 타입 (숫자, 문자 등의 단일 데이터를 저장하기 위한 형태.)
2. References 타입 (단수 혹은 복수의 데이터 묶음을 저장하기 위한 형태.)

```javascript
const num = 3;              // 기본형 / Primitive 타입


const user = {              // 참조형 - References 타입
    age: 100,
    name: 'unchaptered'
}
```

이 중에서 참조형 타입으로서 생성된 친구를 `프로토타입` 이라고 이해하시면 됩니다.
