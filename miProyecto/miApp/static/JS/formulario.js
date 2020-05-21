
var formulario= document.getElementById("formito1");

formulario.addEventListener('submit',function(e){
    e.preventDefault();

   var datos = new FormData(formulario);
   var DatosForm = {
    referencia: datos.get('referencia'),
    precio: datos.get('precio'),
    nombre: datos.get('nombre'),
    descripcion: datos.get('descripcion'),
    categoria: datos.get('categoria'),
    tipo_componentes: datos.get('tipo_componentes'),
};

    for (var key in DatosForm) {
      console.log(key, DatosForm[key]);
      datos.append(key, DatosForm[key]);
}

      fetch('http://127.0.0.1:8000/miApp/productonuevo/', {
      method: 'POST',
      body: datos

      })

      .then((response) =>{
      return response.json()
      })
})

      .then((data) => {
      console.log(data)
      }


function reset(){
    formulario.reset();
}



/*

function crearMensaje(){
    let mensaje = `
        <div class="mensaje-close" id="mensaje-close" onclick="cerrarPopup()">x</div>
        <p id="contenido-mensaje">El cliente ha sido registrado correctamente</p>
        `;
     return mensaje;
}
function cerrarPopup(){
    let popup = document.getElementById('mensaje-content');
    limpiarFormulario();

    popup.style.display = 'none';

}
function mostrarMensaje(){
    //Seleccionamos el div que hemos creado
    let div = document.getElementById('mensaje-content');
    let mensaje = crearMensaje(); // Devuelve el mensaje para insertar en el DIV
    div.innerHTML=''; //Borramos el contenido del div por si tuviera algo
    div.innerHTML = mensaje; //Insertamos el mensaje en el div

}
guardar.addEventListener('click', mostrarMensaje);
*/
