/*function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


var csrftoken = getCookie("csrftoken");
*/

var formulario= document.getElementById("formito1");

formulario.addEventListener('submit',function(e){
    e.preventDefault();

   var datos = new FormData(formulario);
   var DatosForm = {
    referencia: datos.get("referencia"),
    precio: datos.get("precio"),
    nombre: datos.get("nombre"),
    descripcion: datos.get("descripcion"),
    categoria: datos.get("categoria"),
    tipo_componentes: datos.get("tipo_componentes"),
};

//COMPRUEBO QUE SE HA REALIZADO CORRECTAMENTE
    for (var key in DatosForm) {
      console.log(key, DatosForm[key]);
      datos.append(key, DatosForm[key]);
}

      datos.append("csrfmiddlewaretoken", csrftoken);
      fetch('http://127.0.0.1:8000/miApp/productonuevo/', {
      method: 'POST',
      body: datos
      })


      .then((response) =>{
      return response.json()
       })

      .then((data) =>{
      console.log(data)
      })
})


function reset(){
    formulario.reset();
}


