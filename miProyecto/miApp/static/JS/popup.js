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
    let div = document.getElementById('popup');
    let mensaje = crearMensaje(); // Devuelve el mensaje para insertar en el DIV
    div.innerHTML=''; //Borramos el contenido del div por si tuviera algo
    div.innerHTML = mensaje; //Insertamos el mensaje en el div

}
let registrar = document.getElementById("botoncit");
registrar.addEventListener('click', mostrarMensaje);
