

function select_btn(user_name,cof_name) {
    console.log('check')
    console.log(user_name,cof_name)
    $.ajax({
        type: 'POST',
        url: '/api/result',
        data: {
            user_name:user_name
            ,cof_name:cof_name
        },
        success: function(response){
            console.log(response['message'])
            window.alert(user_name+`이 선택한 coffee `+ cof_name +`을 기록했습니다.`);
            window.location.href('/?name='+user_name)
        }
    });

}
