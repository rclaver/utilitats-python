<!DOCTYPE html>
<html>
<head>
  <meta name="robots" content="index,follow">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>L'apuntador del teatre</title>
  <link rel="icon" type="image/x-icon" href="{{url_for('static', filename='img/favicon.ico')}}">
  <link rel="stylesheet" type="text/css" href="{{url_for('static', filename='css/estils.css')}}" />
  <script src="{{url_for('static', filename='js/script.js')}}"></script>
</head>

<body bgcolor="#FFFFFF">
  {% if sentencia is not defined %}
     {% set sentencia = "Escenes per a: " ~ actor %}
  {% endif %}

  <div class="contenidor">
      <div class="titol">L'apuntador del teatre</div>
      <div id="div_error" class="error text"></div>
      <div id="escena_actual" class="escena text">{{sentencia}}</div>

      <div id="div_botons" class="div_botons contenidor">
        <img id="btn_anterior" class="imatge" onClick="window.location.href='{{ url_for('anterior', escena=actor) }}';" src="{{url_for('static', filename='img/web-anterior.png')}}">
        <img id="btn_player"   class="imatge" onClick="window.location.href='{{ url_for('player',   escena=actor) }}';" src="{{url_for('static', filename='img/web-play.png')}}">
        <img id="btn_seguent"  class="imatge" onClick="window.location.href='{{ url_for('seguent',  escena=actor) }}';" src="{{url_for('static', filename='img/web-seguent.png')}}">
      </div>
  </div>
</body>
