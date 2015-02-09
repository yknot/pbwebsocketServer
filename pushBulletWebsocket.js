var exec = require('child_process').exec;   // run command
var WebSocket = require('ws');              // websocket
var fs = require('fs');                     // open file

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
			// show 
			console.log("tickle");
			setTimeout(function() {
				console.log("unpause");
				// start update
				var child = exec('./getUpdate.sh');
				// stdout
				child.stdout.on('data', function(data) {
					console.log('stdout: ' + data);
				});
				// stderr
				child.stderr.on('data', function(data) {
					console.log('stderr: ' + data);
				});
				// finish
				child.on('close', function(code) {
					console.log('closing code: ' + code);
				});
			}
					   , 5000);
					   
				
		}
	});
}

