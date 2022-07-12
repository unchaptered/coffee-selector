const setSwitcher = (isValid, target, set) => {

    if (isValid) setRemover(target, set);
    else setApplier(target, set);

 }

 const setRemover = (target, set) => {
    const switcher = {
        'name': () => set.delete('이름'),
        'password': () => set.delete('비밀번호'),
        'passwordConfirm': () => set.delete('비밀번호 확인')
    }
    switcher[target]();
 }

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
 * */
const updateValidateMessage = (originClassName, set) => {

    if (set.size === 0) $(`.${originClassName}`).text(`유효성 검사에 통과하였습니다.`);
    else $(`.${originClassName}`).text(`${[...set].join(', ')} 항목이 유효하지 않은 값입니다.`);
    
}