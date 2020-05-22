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


//ARREGLAR
function goBack() {
  window.history.go(-1);
}



