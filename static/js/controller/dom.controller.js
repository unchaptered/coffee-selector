/**
 * isValid 인 경우
 *  true -> 특정 대상에 따라서 기준 `set(배열의 일종)` 의 값을 뺴기 위한 setRemover 을 호출합니다.
 *  false -> 특정 대상에 따라서 기준 `set(배열의 일종)` 에 값을 추가하기 위한 setApplier 을 호출합니다.
 * 
 * Set 은 자료구조의 일부로 중복되지 않은 배열의 특징을 가지고 있습니다.
 * 
 * @param {*} isValid boolean
 * @param {*} target string
 * @param {*} set Set
 */
const setSwitcher = (isValid, target, set) => {

    if (isValid) setRemover(target, set);
    else setApplier(target, set);

 }

 /**
  * 내부에 프로토타입 switcher 를 생성하고 이를 통해서 기준 `set(배열의 일종)` 에 정해진 값을 삭제합니다.
  * 
  * 프로타입에 대한 `간단한 내용`이 궁금하시다면, [~/document/prototype.md] 을 참고해주세요.
  * 
  * @param {*} `target` string
  * @param {*} `set` Set
  */
 const setRemover = (target, set) => {
    const switcher = {
        'name': () => set.delete('이름'),
        'password': () => set.delete('비밀번호'),
        'passwordConfirm': () => set.delete('비밀번호 확인')
    }
    switcher[target]();
 }

 
 /**
  * 내부에 프로토타입 switcher 를 생성하고 이를 통해서 기준 `set(배열의 일종)` 에 정해진 값을 추가합니다.
  * 
  * 프로타입에 대한 `간단한 내용`이 궁금하시다면, [~/document/prototype.md] 을 참고해주세요.
  * 
  * @param {*} `target` string
  * @param {*} `set` Set
  */
 const setApplier = (target, set) => {
    const switcher = {
        'name': (set) => set.add('이름'),
        'password': (set) => set.add('비밀번호'),
        'passwordConfirm': (set) => set.add('비밀번호 확인')
    }
    switcher[target](set);
 }


/**
 * originClass 를 대상으로 DOM ELement 를 탐색 후,
 * [...set].join(', ')을 한 후의 다음의 문자열로 내부값을 변경합니다.
 * 
 * 예1 : 이름, 비밀번호 등이 항목이 유효하지 않은 값입니다.
 * 
 * @param {*} `originClassName` string
 * @param {*} `set` Set
 * 
 * */
const updateValidateMessage = (originClassName, set) => {

    if (set.size === 0) $(`.${originClassName}`).text(`유효성 검사에 통과하였습니다.`);
    else $(`.${originClassName}`).text(`${[...set].join(', ')} 항목이 유효하지 않은 값입니다.`);
    
}