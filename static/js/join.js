let isValidName = false;
let isValidPassword = false;
let isValidPasswordConfirm = false;

$(document).ready(
    () => {
        // 초기값 설정
        $('#name').addClass(invalidColor);
        $('#password').addClass(invalidColor);
        $('#passwordConfirm').addClass(invalidColor);

        const validationMessage = 'form-validate-messenger';
        const validationTargets = new Set(['이름', '비밀번호', '비밀번호 확인']);

        // 이름 유효성 검사 후, key값에 해당하는 대상의 클래스에 `붉은 색상` 제어
        $('#name').keyup( ({ originalEvent: { target: { value: name } } }) => {

            isValidName = validateName(name);
            classSwitcher(isValidName, 'name');
            setSwitcher(isValidName, 'name', validationTargets);
            updateValidateMessage(validationMessage, validationTargets);

        });
        // 비밀번호 유효성 검사 후, key값에 해당하는 대상의 클래스에 `붉은 색상` 제어
        $('#password').keyup( ({ originalEvent: { target: { value: pw } } }) => {

            isValidPassword = validatePassword(pw);
            classSwitcher(isValidPassword, 'password');
            setSwitcher(isValidPassword, 'password', validationTargets);
            updateValidateMessage(validationMessage, validationTargets);

        });
        // 비밀번호 유효성 검사 후, key값에 해당하는 대상의 클래스에 `붉은 색상` 제어
        $('#passwordConfirm').keyup( ({ originalEvent: { target: { value: pw } } }) => {
            
            isValidPasswordConfirm = isValidPassword && validatePasswordConfirm(pw, $('#password').val());
            console.log(isValidPasswordConfirm);
            classSwitcher(isValidPassword && isValidPasswordConfirm, 'passwordConfirm');
            setSwitcher(isValidPassword && isValidPasswordConfirm, 'passwordConfirm', validationTargets);
            updateValidateMessage(validationMessage, validationTargets);

        });

        

    }
)

const postJoin = _ => {

    const name = $('#name').val().toString();
    const password = $('#password').val().toString();
    const passwordConfirm = $('#passwordConfirm').val().toString();

    if ( !validateName(name)) return window.alert('이름은 3자 ~ 10자 사이의 문자열로 정해야 합니다.');
    else if ( !validatePassword(password)) return window.alert('비밀번호는 3자 ~ 30자 사이의 문자열로 정해야 합니다.');
    else if ( !validatePasswordConfirm(password, passwordConfirm) ) return window.alert('두 비밀번호가 일치하지 않습니다.');

    $.ajax({
        type: 'POST',
        url: '/api/join',
        data: {
            name: $('#name').val(),
            password:  $('#password').val()
        },
        success: ({
            isSuccess,
            message,
            result: { name, password }
        }) => {
            window.alert(`${name} 으로 회원가입이 완료되었습니다. `);
            location.href = `/login?name=${name}`
        }
    });
    
}