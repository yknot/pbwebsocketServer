var spawn = require('child_process').spawn;



var cmd = spawn('./getUpdate.sh');

cmd.stdout.on('data', function(data) {
	process.stdout.write(data);
});
cmd.stderr.on('data', function(data) {
	process.stderr.write(data);
});

