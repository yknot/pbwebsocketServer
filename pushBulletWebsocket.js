var WebSocket = require('ws');    // websocket
var fs = require('fs');           // open file


// read api key
fs.readFile('pbwebsocketServer.config', 'utf8', function(err, data) {
	// if can't find config file
	if (err) throw 'no config file';
	var configs = JSON.parse(data);

	// function to run websocket
	for (key in configs){
		startWS(configs[key]["APIKey"], key);
	}


});

function startWS(apiKey, name) {
	
	// start websocket
	var ws = new WebSocket('wss://stream.pushbullet.com/websocket/' + apiKey);
	
	// on message
	ws.on('message', function(message) {
		// if update
		if (JSON.parse(message).type == "tickle"){
			
			// get date
			var d = new Date();
			
			// log date and event
			console.log(d + ' ' + name );
			
		}
	});
}


