//Función para que el usuario pueda filtrar
//si quiere ver los pedidos Pendientes, Entregados o Todos

function filtro () {
    var im = document.getElementById('filtro').value;
    var datos = document.getElementsByClassName('dato');
    var todos = 'Todos';

    if(im!='')
      for (var i = 0; i < datos.length; i ++)
        if(datos[i].textContent.indexOf(im)>-1) //retorna el primer índice en el
        //que se puede encontrar un elemento dado en el array, ó retorna -1 si el elemento no esta presente.
          datos[i].style.display="block";
        else
          datos[i].style.display="none";
}
