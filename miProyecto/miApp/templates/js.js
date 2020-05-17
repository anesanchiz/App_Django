// IMAGENES PRODUCTOS
let enlaces = document.getElementsByTagName('a')
// Paso 2: itera por el listado de enlaces añadiendo un controlador para el evento
for(el of enlaces){
  el.addEventListener('click', actualizarImagenPrincipal);
}
// Paso 3: El controlador deberá cambiar la imagen principal accediendo a sus atributos
function actualizarImagenPrincipal(event){
  event.preventDefault(); // detener la navegación
  let imagen = document.getElementById('imagen-seleccionada');
  // Cambiar el atributo src de la imagen, poniendo el del enlace clickado
  imagen.src = event.currentTarget.href;
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
