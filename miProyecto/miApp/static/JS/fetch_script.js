function cargarDatos(filtro) {
    let url = "http://127.0.0.1:8000/pedidosjs/<int:pk>/"
    fetch(url)
        .then((respuesta) => respuesta.json())
        .then((datos) => {
            crearTablaTareas(datos, filtro)
        })
}

cargarDatos("");



function crearFila(objeto){
    console.log(objeto.nombre)
    let fila = `
        <tr>
            <td>${objeto.codigo}</td>
            <td>${objeto.referencia}</td>
            <td>${objeto.datos_cliente.empresa}</td>
            <td>${objeto.estado_tarea}</td>
            <td style="text-align: center;"><a class="btn btn-warning" href="/tarea/${objeto.id}">Mostrar más</a></td>
        </tr>
    `
    return fila;
}
