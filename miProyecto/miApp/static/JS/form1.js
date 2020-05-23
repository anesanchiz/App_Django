function devuelveDatos(datos){
    const datos_form = new FormData();

    for(key in datos){
        datos_form.append(key, datos[key])
    }
    fetch('http://127.0.0.1:8000/miApp/productonuevo/', {
       method: 'POST',
       body: datos_form
    })

    .then(function(response) {
       if(response.ok) {
           return response.text()
       } else {
           throw "Error en la llamada AJAX";
       }

    })
    .then(function(texto) {
       console.log(texto);
    })
    .catch(function(err) {
       console.log(err);
    });
}

document.getElementById('botoncit').addEventListener('click', function(event){
    event.preventDefault();

    var datos = {
        referencia: document.getElementsByName("referencia")[0].value,
        precio: document.getElementsByName("precio")[0].value,
        nombre: document.getElementsByName("nombre")[0].value,
        descripcion: document.getElementsByName("descripcion")[0].value,
        categoria: document.getElementsByName("categoria")[0].value,
        tipo_componentes: document.getElementsByName("tipo_componentes")[0].value,
    }

    console.log(datos);
    devuelveDatos(datos);
});

