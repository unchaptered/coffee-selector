$(document).ready(function () {
    show_nespresso()
    save_nespresso()

})

function show_nespresso() {
    $.ajax({
        type: "GET",
        url: "/nespresso",
        data: {},
        success: function (response) {
            alert(response['msg'])
        }
    })
}

function save_nespresso() {
    let cake = $("#cake option:selected").val();
    let apple = $("#apple option:selected").val();
    let strength = $("#strength option:selected").val();
    let milk = $("#milk option:selected").val();
    let size = $("#size option:selected").val();

    $.ajax({
        type: "POST",
        url: "/nespresso",
        data: {cake_give: cake, apple_give: apple, strength_give: strength, milk_give: milk, size_give: size},
        success: function (response) {
            alert(response['msg'])
        }
    })
}