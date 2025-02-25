  {% include "head.tpl" %}
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>

<body bgcolor="#FFFFFF">
  {% if sentencia is not defined %}
     {% set sentencia = "Escenes per a: " ~ actor %}
  {% endif %}
  {% if estat is not defined %}
     {% set estat = "inici" %}
  {% endif %}

  <div class="contenidor">
    <div class="titol">L'apuntador del teatre</div>
    <div id="div_error" class="error text"></div>
    <div id="escena_actual" class="escena text">{{sentencia}}</div>

    <div id="div_botons" class="div_botons contenidor">
      <img id="btn_anterior" class="imatge" onClick="window.location.href='{{ url_for('anterior', escena=actor) }}';" src="{{url_for('static', filename='img/web-anterior.png')}}">
      <img id="{{'btn_' ~ estat}}" class="imatge" onClick="window.location.href='{{ url_for(estat, escena=actor) }}';" src="{{url_for('static', filename='img/web-' ~ estat ~ '.png')}}">
      <img id="btn_seguent" class="imatge" onClick="window.location.href='{{ url_for('seguent', escena=actor) }}';" src="{{url_for('static', filename='img/web-seguent.png')}}">
      {% if estat == "stop" %}
      <img id="btn_record" class="imatge" onClick="window.location.href='{{ url_for('seguent', escena=actor) }}';" src="{{url_for('static', filename='img/web-record.png')}}">
      {% endif %}
    </div>
  </div>

  {% if estat == "payer" %}
     <script src="/static/js/escenes3.js"></script>
  {% endif %}

  <script>
    $(document).ready(function() {
      let contenedor = $("#escena_actual");
      function getLine() {
        $.ajax({
          url: '/inici',  // Ruta para obtener las líneas
          success: function(data) {
            contenedor.text(data);  // Reemplazamos el contenido del div
          },
          error: function() {
            console.log("Error al obtener la línea.");
          }
        });
      }
      setInterval(getLine, 1000);
    });
  </script>

</body>
