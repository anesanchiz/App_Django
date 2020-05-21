// FUNCIONES APLICADAS EN PRODUCTOS Y COMPONENTES.HTML PARA DINAMIZAR LAS IMAGENES
    let enlaces = document.getElementsByClassName("pics")
        for(el of enlaces){
            el.addEventListener('click', actualizarImagenPrincipal);
        }


    function actualizarImagenPrincipal(event){
        event.preventDefault();
        let imagen = document.getElementById('imagen-seleccionada');
        imagen.src = event.currentTarget.href;
    }

        let enlaces1 = document.getElementsByClassName("pics1")
        for(el of enlaces1){
        el.addEventListener('click', actualizarImagenComps);
        }

    function actualizarImagenComps(event){
        event.preventDefault();
        let imagen1 = document.getElementById('compimagen');
        imagen1.src = event.currentTarget.href;
    }
