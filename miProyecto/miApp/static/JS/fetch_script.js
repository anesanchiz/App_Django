
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

      let opci1 = document.getElementById("op1");
      opci1.textContent = `${json[0].codigo}`;

      let opci2 = document.getElementById("op2");
      opci2.textContent = `${json[1].codigo}`;

      let opci3 = document.getElementById("op3");
      opci3.textContent = `${json[2].codigo}`;

      let opci4 = document.getElementById("op4");
      opci4.textContent = `${json[3].codigo}`;

    });
}
