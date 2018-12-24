$(document).ready(function() {
    $(".load-result").bind("click", function(event) {
        event.preventDefault();
        $.get("/table/",function(data) {
            alert("Запрос выполнен");
            $("#result").html(data);
        });
    });

});
