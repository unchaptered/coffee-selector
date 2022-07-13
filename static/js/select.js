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
    let cake = $("#cake").val("value");
    let apple = $("#apple").val("value");
    let strength = $("#strength").val("value");
    let milk = $("#milk").val("value");
    let size = $("#size").val("value");

    $.ajax({
        type: "POST",
        url: "/result",
        data: {cake_give: cake, apple_give: apple, strength_give: strength, milk_give: milk, size_give: size},
        success: function (response) {
            alert(response['msg'])
        }
    })
}