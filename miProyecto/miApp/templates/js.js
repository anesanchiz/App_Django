// IMAGENES PRODUCTOS
function actualizarImagenPrincipal(event){
  event.preventDefault();
  let imagen = document.getElementById('imagen-seleccionada');
  imagen.src = event.currentTarget.href;
}

let enlaces = document.getElementsByTagName('a')
for(el of enlaces){
  el.addEventListener('click', actualizarImagenPrincipal);
}



// IMAGENES COMPONENTES
function actualizarImagenComps(event){
  event.preventDefault();
  let imagen = document.getElementById('compimagen');
  imagen.src = event.currentTarget.href;
}

let enlaces = document.getElementsByTagName('a')
for(el of enlaces){
  el.addEventListener('click', actualizarImagenComps);
}






const URL = "http://127.0.0.1:8000/miApp/pedidosjs/";

//Botón [+] para ver detalles
let masBtn = document.getElementById("btn-js-mas");

masBtn.addEventListener("click", (event) => {
  loadData();
});


function loadData(URL) {
  fetch(URL)
    .then((response) => response.json())
    .then((json) => {

    console.log(json);

      let cod_pedido = document.getElementById("codigo");
      cod_pedido.textContent = `${json.codigo}`;

      let fech_pedido = document.getElementById("fecha");
      fech_pedido.textContent = `${json.fecha}`;

      let cant_pedido = document.getElementById("cantidad");
      cant_pedido.textContent = `- ${json.cantidad} -`;
    });
}

loadData();


