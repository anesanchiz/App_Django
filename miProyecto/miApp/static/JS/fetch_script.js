
//FUNCION FETCH PEDIDOS
//A PARTIR DE LA VISTA DE PEDIDOS EN FORMATO JSON LA FUNCION RECOGE LA
// POSICION INTRODUCIDA POR EL INPUT TEXT Y SACA LOS DATOS DE DICHO PEDIDO

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

      let cElement = document.getElementById("fecha");
      cElement.textContent = "Fecha:  "+`${json[porNum].fecha}`;

      let qElement = document.getElementById("precio");
      qElement.textContent = "Precio:  "+`${json[porNum].precio_total}`+"€";


    });
}

let loadBtn3 = document.getElementById("loadBtn2");

loadBtn3.addEventListener("click", (event) => {
  cargarJson2();
});


//FUNCION QUE CARGA LA LISTA DE LOS CÓDIGOS DE PEDIDO DISPONIBLE PARA QUE
//EL USUARIO LOS INTRODUZCA EN EL TEXT INPUT DE AL LADO
function cargarJson2() {
  fetch('http://127.0.0.1:8000/miApp/pedidosjs')
    .then((response) => response.json())
    .then((json) => {
    console.log(json);

    ;
    for(i=0; i<json.length; i++){
      let ay = document.getElementById("ay")
      var lista
      lista += "<li>"+`${json[i].codigo}`+"</li>"
      ay.innerHTML=lista
}
    });
}
