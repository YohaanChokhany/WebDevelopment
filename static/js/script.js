$(document).ready(function(){
    $.material.init();
    $(document).on("submit", "#paper-info", function(e){
      e.preventDefault();
      var form = $("#paper-info").serialize();
      $.ajax({
        url: '/get-mcq-answers',
        type: 'POST',
        data: form,
        success: function(res){
          getAnswers(res)
        }
      });
    });
  });