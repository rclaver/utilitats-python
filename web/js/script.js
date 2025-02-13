function formulari() {
   s_escena = document.getElementById("seleccio_escenes");
   i = s_escena.selectedIndex;
   if (i >= 0) {
      escena = s_escena.options[i].value;
   }else {
      escena = "No has seleccionat cap escena";
   }
   visible("div_formulari", false);
   visible("div_error", true);
   visible("escena_actual", true);
   visible("div_botons", true);
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

function visible(e, es_visible) {
   if (es_visible) {
      d = "block";
      v = "visible";
   }else {
      d = "none";
      v = "hidden";
   }
   document.getElementById(e).style.display = d;
   document.getElementById(e).style.visibility = v;
}

function get_propietat(e) {
   ret = "weight: " + document.getElementById(e).style.fontWeight + ".";
   return ret;
}

function get_screen_sizes(selection) {
   if (selection === "min") {
      sizes = "- body.clientHeight: " + document.body.clientHeight + "<br>" +
              "- window.screen.height: " + window.screen.height + "<br>" +
              "- window.innerHeight: " + window.innerHeight + "<br>" +
              "- body.clientWidth: " + document.body.clientWidth + "<br>" +
              "- window.screen.width: " + window.screen.width + "<br>" +
              "- window.innerWidth: " + window.innerWidth;
   }else {
      sizes = "- body.scrollHeight: " + document.body.scrollHeight + "<br>" +
              "- documentElement.scrollHeight: " + document.documentElement.scrollHeight + "<br>" +
              "- body.offsetHeight: " + document.body.offsetHeight + "<br>" +
              "- documentElement.offsetHeight: " + document.documentElement.offsetHeight + "<br>" +
              "- body.clientHeight: " + document.body.clientHeight + "<br>" +
              "- documentElement.clientHeight: " + document.documentElement.clientHeight + "<br>" +
              "- body.scrollWidth: " + document.body.scrollWidth + "<br>" +
              "- documentElement.scrollWidth: " + document.documentElement.scrollWidth + "<br>" +
              "- body.offsetWidth: " + document.body.offsetWidth + "<br>" +
              "- documentElement.offsetWidth: " + document.documentElement.offsetWidth + "<br>" +
              "- body.clientWidth: " + document.body.clientWidth + "<br>" +
              "- documentElement.clientWidth: " + document.documentElement.clientWidth;
   }
   return sizes;
}