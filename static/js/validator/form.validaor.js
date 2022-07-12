const invalidColor = 'wrong_validate';

/**
 * 이름 유효성 검사,
 * 
 * 호이스팅으로 인해서 최상단 글로벌 함수로 위치됨
 * 
 * @param {*} `n` 문자, 숫자, 특수문자 가능
 * @returns `true` : 유효성 검사 통과
 */
 const validateName = (n) => n.length >= 3 && n.length <= 10;

 /**
  * 비밀번호 유효성 검사,
  * 
  * 호이스팅으로 인해서 최상단 글로벌 함수로 위치됨
  * 
  * @param {*} `n` 문자, 숫자, 특수문자 가능
  * @returns `true` : 유효성 검사 통과
  */
 const validatePassword = (p) => p.length >= 3 && p.length <= 30;
 
 /**
  * 복수의 비밀번호 유효성 검사,
  * 
  * 호이스팅으로 인해서 최상단 글로벌 함수로 위치됨
  * 
  * @param {*} p 문자, 숫자, 특수문자 가능
  * @param {*} p2 문자, 숫자, 특수문자 가능
  * @returns `true` : 유효성 검사 통과
  */
 const validatePasswordConfirm = (p, p2) => p === p2;
 
 
 const classSwitcher = (isValid, target) => {
     if (isValid) classRemover(target);
     else classApplier(target);
 }
 const classRemover = (target) => {
     const switcher = {
         'name': () => $('#name').removeClass(invalidColor),
         'password': () => $('#password').removeClass(invalidColor),
         'passwordConfirm': () => $('#passwordConfirm').removeClass(invalidColor),
     }
     switcher[target]();
 }
 const classApplier = (target) => {
     const switcher = {
         'name': () => $('#name').addClass(invalidColor),
         'password': () => $('#password').addClass(invalidColor),
         'passwordConfirm': () => $('#passwordConfirm').addClass(invalidColor),
     }
     switcher[target]();
 }