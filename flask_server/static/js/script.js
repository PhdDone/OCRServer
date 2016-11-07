// hide buttons
$("#retry").hide()
$("#results").hide()

$(function() {

  // sanity check
  console.log("dom is ready!");
    console.log($('#file')[0]);
    console.log(document.getElementById('file-picker'));
  // event handler for form submission
  $('#post-form').on('submit', function(event){
    $("#results").hide()
    //value = $('input[name="image_url"]').val();
      console.log($('#post-form')[0])
      //var input = document.getElementById('file-picker').files[0];
    //console.log(input)
    formdata = new FormData($('#post-form')[0]); 
    $.ajax({
      type: "POST",
      url: "/v1/ocr",
      contentType: false,
      processData: false,
      data : formdata,
      success: function(result) {
        console.log(result);
        $("#post-form").hide()
        $("#retry").show()
        $("#results").show()
        $("#results").html("<h3>Image</h3><img class='img-responsive' src='/ocr/" + result["filename"]+ "'" + 
          " style='max-width: 400px;'><br><h3>Results</h3><div class='well'>"+
          result["output"]+"</div>");
      },
      error: function(error) {
        console.log(error);
      }
    });
  });

  // Start search over, clear all existing inputs & results
  $('#retry').on('click', function(){
    $("input").val('').show();
    $("#post-form").show()
    $("#retry").hide()
    $('#results').html('');
  });


});