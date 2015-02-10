var spawn = require('child_process').spawn;       // spawn
var WebSocket = require('ws');    // websocket
var fs = require('fs');           // open file


// read api key
fs.readFile('api_key', 'utf8', function(err, data) {
	if (err) throw err;
	var apiKey = (data);

	// function to run websocket
	startWS(apiKey);
});

function startWS(apiKey) {
	
	// start websocket
	var ws = new WebSocket('wss://stream.pushbullet.com/websocket/' + apiKey);
	
	// on message
	ws.on('message', function(message) {
		// if tickle
		if (JSON.parse(message).type == "tickle"){
			
			console.log('tickle')
			
		}
	});
}


