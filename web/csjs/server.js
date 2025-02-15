var express = require('express');
var app     = express();
var server  = require('http').createServer(app);
var io      = require('socket.io')(server);
var bodyParser = require('body-parser') //for POST request

app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
   extended: true
}));

server.listen(8080, function() {
   console.log("Server running on port 8080.");
});

var query;
var dir = __dirname;

app.get('/', function(req, res) {
   res.sendFile(dir + '/index.html');
});

app.post('/', function(req, res) {
   query = req.body.input1
   console.log("Server: In post request.")
   console.log(query);
   res.sendFile(dir + '/apuntador.html');
});

io.on('connection', function(socket) {
   socket.on('ready', function() {
      socket.emit('change_result', {result: query});
   });
});