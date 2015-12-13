

$('#form_anadir_elemento').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    validateNewProduct();
    anadir_elemento();
});

function anadir_elemento() {
    console.log("Estamos adentro de anadir_elemento")
    var precio =document.getElementById("precio_form").value;
    var x = document.getElementById("producto").selectedIndex;
    var producto =  document.getElementsByTagName("option")[x].value;
    console.log(precio)
    console.log(producto)
    $("#myModal").modal('hide');
    $.ajax({
        url  : "../anadirElementoCarta",
        type : "POST",
        data : { producto : producto, precio : precio },

        success : function(json) {
            $('#precio_form').val('')
            console.log(json);
            console.log("success");
        },

        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

function validateNewProduct() {
  var x = document.getElementById("precio_form").value
  var y = document.getElementById("producto").selectedIndex;
  if(y == 0){
    alert("Debe seleccionar algún alemento");
  }
  else if(x == null || x == ""){
    alert("El campo precio no puede ir vació");
  }
  else{
    return false;
  }
}

function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}