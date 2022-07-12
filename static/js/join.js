const postJoin = _ => {

    const name = $('#name').val().toString();
    const password = $('#password').val().toString();
    const passwordConrfirm = $('#passwordConrfirm').val().toString();

    if ( ! (name.length >= 3 && name.length <= 10 ) )

        return window.alert('이름은 3자 ~ 10자 사이의 문자열로 정해야 합니다.');

    else if ( ! (password.length >= 3 && password.length <= 10 ) )

        return window.alert('비밀번호는 3자 ~ 30자 사이의 문자열로 정해야 합니다.');

    else if ( password !== passwordConrfirm )

        return window.alert('두 비밀번호가 일치하지 않습니다.');

    $.ajax({
        type: 'POST',
        url: '/api/join',
        data: {
            name: $('#name').val(),
            password:  $('#password').val()
        },
        success: (res) => {
            console.log(res);
        }
    });
    
}