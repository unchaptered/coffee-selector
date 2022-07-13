$(document).ready(function () {
    show_nespresso()
})

function show_nespresso() {
    $.ajax({
        type: "GET",
        url: "/nespresso",
        data: {},
        success: function (response) {
            console.log('success')
        }
    })
}


function save_nespresso() {
    let name = localStorage.getItem('name');
    let cake = $("#cake option:selected").val();
    let apple = $("#apple option:selected").val();
    let strength = $("#strength option:selected").val();
    let milk = $("#milk option:selected").val();
    let size =  $("#size option:selected").val();
    console.log(name)
    $.ajax({
        type: "POST",
        url: "/nespresso",
        data: {name:name,cake_give: cake, apple_give: apple, strength_give: strength, milk_give:milk, size_give:size},
        success: ({
            msg
        }) => {
            window.alert(msg);
            location.href = `/result?name=`+name
        }
    })
}