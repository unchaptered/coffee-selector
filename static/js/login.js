let isValidName = false;
let isValidPassword = false;

$(document).ready(
    () => {
        // 초기값 설정
        $('#name').addClass(invalidColor);
        $('#password').addClass(invalidColor);
        
        const validationMessage = 'form-validate-messenger';
        const validationTargets = new Set(['이름', '비밀번호']);

        $('#name').keyup(({ originalEvent: { target: { value: name } } }) => {

            console.log(`isValidName ${isValidName} isValidPassword ${isValidPassword}`);
            
            isValidName = validateName(name);
            classSwitcher(isValidName, 'name');
            classSwitcher(isValidName && isValidPassword, 'allConditions');
            setSwitcher(isValidName, 'name', validationTargets);
            updateValidateMessage(validationMessage, validationTargets);

        });
        $('#password').keyup(({ originalEvent: { target: { value: pw } } }) => {
            
            console.log(`isValidName ${isValidName} isValidPassword ${isValidPassword}`);

            isValidPassword = validatePassword(pw);
            classSwitcher(isValidPassword, 'password');
            classSwitcher(isValidName && isValidPassword, 'allConditions');
            setSwitcher(isValidPassword, 'password', validationTargets);
            updateValidateMessage(validationMessage, validationTargets);

        });

        updateValidateMessage(validationMessage, validationTargets);
    }
)

const postLogin = _ => {

    const name = $('#name').val().toString();
    const password = $('#password').val().toString();

    console.log(`버틐 클릭 : 유효성 검사 진행 ${name} / ${password}`);

    if ( !validateName(name)) return window.alert('이름은 3자 ~ 10자 사이의 문자열로 정해야 합니다.');
    else if ( !validatePassword(password)) return window.alert('비밀번호는 3자 ~ 30자 사이의 문자열로 정해야 합니다.');

    console.log(`버튼 클릭 : 유효성 검사 통과!`);

    $.ajax({
        type: 'POST',
        url: '/api/login',
        data: {
            name: $('#name').val(),
            password:  $('#password').val()
        },
        success: ({
            isSuccess,
            message,
            result: { name, password, accessToken }
        }) => {
            if (isSuccess) {
                console.log({
                    isSuccess,
                    message,
                    result: {
                        name, password, accessToken
                    }
                });
                
                window.alert(message);

                localStorage.setItem('name', name);
                localStorage.setItem('accessToken', accessToken);
                return location.href = `/nespresso?name=`+name;
            } else {
                return window.alert(message);
            }
        }
    });
    
}