function formulari() {
   s_escena = document.getElementById("seleccio_escenes");
   i = s_escena.selectedIndex;
   if (i >= 0) {
      escena = s_escena.options[i].value;
   }else {
      escena = "No has seleccionat cap escena";
   }
   document.getElementById("error").style.display = "block";
   document.getElementById("error").style.visibility = "visible";
   document.getElementById("error").innerHTML = escena;
}

function play(escena) {
   var xhr;
   var contenidoRecibido = '';

   if (escena.length===0) {
      document.getElementById("escena_actual").innerHTML = "";
      return;
   }

   xhr = new XMLHttpRequest();

   xhr.onreadystatechange = function() {
      if (xhr.readyState===4 && xhr.status===200) {
         contenidoRecibido = xhr.responseText;
         document.getElementById("escena_actual").innerHTML = contenidoRecibido;
      }
   };

   xhr.open("POST","apuntador.py?do=play&escena="+escena);
   xhr.send();
}

function anterior() {
}

function seguent() {
}
