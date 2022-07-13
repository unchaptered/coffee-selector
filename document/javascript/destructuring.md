# Spread & Destructuring

> 데이터의 묶음 혹은 특이함 구현하는 형태들이 주로 `참조-References Type` 이며, 이러한 친구들은 `프로토타입-Prototype` 으로 생성됩니다.
>
> prototype.md 참고 [Local 환경이라면 Ctrl + 클릭!](./prototype.md)

이러한 객체는 다른 변수에 재할당 하면, 두 친구가 같은 속성을 공유하게 됩니다.

```javascript
const obj = {
    name: 'hello'
}

const obj2 = obj;
obj2.name = 'oi';

console.log(obj.name)       // oi
console.log(obj2.name)      // oi
```

따라서 이러한 친구들은 별도의 방법으로 복사를 하게 됩니다.
그 중에서, `함수를 제외한 값` 들만 복사할 경우 다음과 같이 복사할 수 있습니다.

```javascript
const obj2 = { ...obj }
```

저기서 연달아 써져있는 점 세개를 `스프레드 문법, Spread Syntax` 라고 부르며, 이를 통해서 문제를 해결할 수 있습니다.

나중에 학습 중에 테스트해보시면, 속도도 빠릅니다.