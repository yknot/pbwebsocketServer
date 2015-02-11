var fs = require('fs');

// latest file -- get latest create date
// command -- get latest commands

if(process.argv[2] == 'latest'){

	// read passed in file
	fs.readFile(process.argv[3], 'utf8', function(err, data) {
		if (err) throw err;
		// parse
		var pbs = (JSON.parse(data));
		
		// read first (latest) push and grab created date
		if (pbs.pushes[0].created !== undefined)
			console.log(pbs.pushes[0].created);
	});
} else if(process.argv[2] == 'command'){

	// read new pushes
	fs.readFile(process.argv[3], 'utf8', function(err, data){
		if (err) throw err;
		// parse
		var pbs = (JSON.parse(data));
		
		// for each push in the new data
		for (i = 0; i < pbs.pushes.length-1; i++){

			// if there is a body and title (so not an update) and it's sent to the server
			if (pbs.pushes[i].body !== undefined 
				&& pbs.pushes[i].target_device_iden 
				== 'ujA68FT1A28sjAyPxI9Aei'
				&& pbs.pushes[i].title !== undefined){

				// log body to file
				console.log(pbs.pushes[i].body);
				
			}
		}

	});

}
