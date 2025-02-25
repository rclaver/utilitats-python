  {% include "head.tpl" %}
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
     <script src="/static/js/escenes.js"></script>
  {% endif %}

  <script>
    const contenidorEscena = document.getElementById('escena_actual');

    // Conectar al endpoint de eventos
    const eventSource = new EventSource('/{{estat}}');

    // Escuchar eventos de tipo "message" (el predeterminado)
    eventSource.onmessage = function(event) {
        contenidorEscena.textContent = event.data;  // Actualizar el contenido del div
    };

    // Manejar errores (opcional)
    eventSource.onerror = function() {
        console.error("Error en la conexión SSE.");
        eventSource.close();  // Cerrar la conexión en caso de error
    };
  </script>

</body>
