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
  <div class="contenidor">
      <div class="titol">L'apuntador del teatre</div>
      <div id="div_error" class="error text"></div>
      <div id="escena_actual" class="escena text">Escenes per a: "{{actor}}"</div>

      <div id="div_botons" class="div_botons contenidor">
        <img id="btn_anterior" class="imatge " src="{{url_for('static', filename='img/web-anterior.png')}}" onClick="anterior();">
        <img id="btn_play" class="imatge" onClick="{{ url_for('play', escena='{{actor}}') }}" src="{{url_for('static', filename='img/web-play.png')}}">
        <img id="btn_seguent" class="imatge" src="{{url_for('static', filename='img/web-seguent.png')}}" onClick="seguent();">
      </div>
  </div>
</body>
