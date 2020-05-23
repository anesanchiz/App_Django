
//FUNCION FETCH PEDIDOS

let loadBtn = document.getElementById("loadBtn1");

loadBtn.addEventListener("click", (event) => {
  cargarJson();
});

function cargarJson() {

  fetch('http://127.0.0.1:8000/miApp/pedidosjs')
    .then((response) => response.json())
    .then((json) => {
    console.log(json);


    var porNum=document.getElementById("num").value;

      console.log(porNum)

      let rango = document.createElement('p');
      rango.innerHTML = "El listado de pedidos es de 0 a "+ json.length
      console.log(rango)

      let cElement = document.getElementById("codigo");
      cElement.textContent = "Fecha:  "+`${json[porNum].fecha}`;

      let qElement = document.getElementById("precio");
      qElement.textContent = "Precio:  "+`${json[porNum].precio_total}`+"€";


    });
}

//FUNCION UPLOAD FILE

$(function(){
        $("#form-upload").on("submit", function(e){
            e.preventDefault();
            var f = $(this);
            var formData = new FormData(document.getElementById("form-upload"));
            formData.append("dato", "valor");

            $.ajax({
                url: "recibe.php",
                type: "post",
                dataType: "html",
                data: formData,
                cache: false,
                contentType: false,
	     processData: false
            })
                .done(function(res){
                    $("#mensaje").html("Respuesta: " + res);
                });
        });
    });
