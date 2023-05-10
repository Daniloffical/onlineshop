$(document).ready(function () {
    $("#form").submit(function(){
      const csrf = $('#form input[name="csrfmiddlewaretoken"]')
      $(".modal_window").hide();
      console.log($(".url_get").val())
      $.ajax({
        url: $(".url_get").val(),
        type: 'POST',
        data: {
          csrfmiddlewaretoken: csrf.val(),
          name:$("#form_name").val(),
          reply:$("#form_reply").val(),
        },
        success: function(response){
          alert(1)
        }
      })
    })
});

