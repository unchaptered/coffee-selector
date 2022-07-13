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
        let cake = $('#cake').val()
        let apple = $('#apple').val()
        let strength = $('#strength').val()
        let milk = $('#milk').val()
        let size = $('#size').val()


        $.ajax({
            type: "POST",
            url: "/nespresso",
            data: {cake_give: cake, apple_give: apple, strength_give: strength, milk_give:milk, size_give:size},
            success: function (response) {
                alert(response['msg'])
            }
        })
    }