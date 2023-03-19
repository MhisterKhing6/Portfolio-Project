$(function () {
    $(".VIP1").on("click", function () {
        $.ajax({
            type: "get",
            datatype: 'jsonp',
            url: "http://0.0.0.0:5000/purchase/VIP1",
            success: function (response) {
                if (response.Status === 1)
                    alert("Success");
                else if (response.Status == 3)
                    alert("You already own this shop");
                else if (response.Status == 4)
                    alert("You already own a bigger shop");
                else
                    alert("Balance Low deposite to purchase");
                location.reload();

            }
        });
    });


    $(".VIP2").on("click", function () {
        $.ajax({
            type: "get",
            datatype: 'jsonp',
            url: "http://0.0.0.0:5000/purchase/VIP2",
            success: function (response) {
                if (response.Status === 1)
                    alert("Success");
                else if (response.Status == 3)
                    alert("You already own this shop");
                else if (response.Status == 4)
                    alert("You already own a bigger shop");
                else
                    alert("Balance Low deposite to purchase");
                location.reload();


            }
        });
    });

    $(".VIP3").on("click", function () {
        $.ajax({
            type: "get",
            datatype: 'jsonp',
            url: "http://0.0.0.0:5000/purchase/VIP3",
            success: function (response) {
                if (response.Status === 1)
                    alert("Success");
                else if (response.Status == 3)
                    alert("You already own this shop");
                else if (response.Status == 4)
                    alert("You already own a bigger shop");
                else
                    alert("Balance Low deposite to purchase");
                location.reload();

            }

        });

    });

});