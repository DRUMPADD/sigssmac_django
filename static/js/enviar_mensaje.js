$(document).ready(function () {
    $("#enviar").submit(function (e) {
        e.preventDefault();
        var datos_formulario = $(this).serializeArray();

        $.ajax({
            type: "POST",
            url: $("#btn_enviar").attr("ajax-data-target"),
            data: datos_formulario,
            success: function (response) {
                $("#enviar").trigger("reset");
                swal("Cotización enviada", response.msg, "success");
            }
        });
    })
});