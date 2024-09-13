# -*- coding: utf-8 -*-

def application(environ, start_response):
	pc = "<p style='font:10pt \"Courier New\";'>"
	pa = "<p style='font-family:Arial;'>"

	if (environ["PATH_INFO"] == "/"):
		respuesta = pa + "Página inicial</p>"
		respuesta += pa + "Estás en la raíz</p>"
		respuesta += pa + "<a href='/principal'>Ir a la página principal</a></p>"
	elif (environ["PATH_INFO"] == "/principal"):
		respuesta = pa + "Bienvenidos a mi página web principal</p>"
	else:
		respuesta = pa + "<trong>Página incorrecta</strong></p>"

	respuesta = pa + "<b>Parámetros CGI:</b></p>" + \
					pc + "REQUEST_METHOD: " + environ["REQUEST_METHOD"] + "<br>" \
					"SCRIPT_NAME: " + environ["SCRIPT_NAME"] + "<br>" \
					"PATH_INFO: " + environ["PATH_INFO"] + "<br>" \
					"QUERY_STRING: " + environ["QUERY_STRING"] + "<br>" \
					"CONTENT_TYPE: " + environ["CONTENT_TYPE"] + "<br>" \
					"CONTENT_LENGTH: " + environ["CONTENT_LENGTH"] + "<br>" \
					"SERVER_NAME: " + environ["SERVER_NAME"] + "<br>" \
					"SERVER_PORT: " + environ["SERVER_PORT"] + "<br>" \
					"SERVER_PROTOCOL: " + environ["SERVER_PROTOCOL"] + "<br>" \
					"url: " + environ["SERVER_NAME"] + ":" + environ["SERVER_PORT"] + "/" +  environ["SCRIPT_NAME"] + environ["PATH_INFO"] + "</p>" + \
					respuesta

	start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

	return [respuesta.encode()]

if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	srv = make_server('localhost', 8080, application)
	srv.serve_forever()
