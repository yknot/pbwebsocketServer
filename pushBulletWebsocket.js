var spawn = require('child_process').spawn;       // spawn
var WebSocket = require('ws');    // websocket
var fs = require('fs');           // open file


// read api key
fs.readFile('apiKey', 'utf8', function(err, data) {
	// if can't find apiKey
	if (err) throw 'no apiKey file';
	var apiKey = (data);

	// function to run websocket
	startWS(apiKey);
});

function startWS(apiKey) {
	
	// start websocket
	var ws = new WebSocket('wss://stream.pushbullet.com/websocket/' + apiKey);
	
	// on message
	ws.on('message', function(message) {
		// if update
		if (JSON.parse(message).type == "tickle"){
			
			// get date
			var d = new Date()
			
			// log date and event
			console.log(d + ' tickle' )
			
		}
	});
}


