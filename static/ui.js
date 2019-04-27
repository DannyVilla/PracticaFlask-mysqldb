/*eslint-env browser*/
// la primera línea es para eliminar los errores que da brackets por usar eslint
// https://eslint.org/docs/rules/no-undef 
/* una lista de eventos se encuentra en https://www.w3schools.com/jsref/dom_obj_event.asp */

document.getElementById("btnAcceso").addEventListener("click", enviarPeticion);
document.getElementById("popup-cerrar").addEventListener("click", cerrar);

function enviarPeticion() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 ) {
            var respuesta = xhr.responseXML;
            var x = respuesta.getElementsByTagName("resultado");
            document.getElementsByClassName("popup-titulo")[0].innerHTML = x[0].getElementsByTagName("titulo")[0].textContent;
            document.getElementsByClassName("popup-contenido")[0].innerHTML = x[0].getElementsByTagName("contenido")[0].textContent;
            document.getElementById("popup").style.display = "block";
        }
    };
   
    var u = document.getElementById("user").value;
    var p = document.getElementById("pass").value;
    var q = "user="+u+"&"+"pass="+p;
    
    xhr.open("POST", "http://127.0.0.1/cgi-bin/crud/accesoAjax.pl", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded"); 
    xhr.send(q);
}

function cerrar(e){
    if (e.target)
        document.getElementById("popup").style.display = "none";
}