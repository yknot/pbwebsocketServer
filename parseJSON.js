var fs = require('fs');

// latest file -- get latest create date
// command -- get latest commands

if(process.argv[2] == 'latest'){

	fs.readFile(process.argv[3], 'utf8', function(err, data) {
		if (err) throw err;
		var pbs = (JSON.parse(data));
		
		if (pbs.pushes[0].created !== undefined)
			console.log(pbs.pushes[0].created);
	});
} else if(process.argv[2] == 'command'){

	fs.readFile('newPushes', 'utf8', function(err, data){
		if (err) throw err;
		var pbs = (JSON.parse(data));
		
		for (i = 0; i < pbs.pushes.length-1; i++){

			if (pbs.pushes[i].body !== undefined 
				&& pbs.pushes[i].target_device_iden 
				== 'ujA68FT1A28sjAyPxI9Aei') {

				if (pbs.pushes[i].title !== undefined) {

					console.log(pbs.pushes[i].body);
				}
			}
		}

	});

} else {
	console.log('Invalid command');
}
