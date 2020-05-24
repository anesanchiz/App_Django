
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
