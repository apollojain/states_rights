var states = [];

    function getStates(states){
    	// states.forEach(function(entry){
    		return states.join(', ');
    	// });
    }

	$('#map').usmap({
      'stateStyles': {
        fill: "#4ECDC4",
        stroke: "#41A59B",
        "stroke-width": 1,
        "stroke-linejoin": "round",
        scale: [1, 1]
      },
      'stateHoverStyles': {
        fill: "#C7F464",
        stroke: "#ADCC56",
        scale: [1.1, 1.1]
      },
      'labelBackingStyles': {
        fill: "#4ECDC4",
        stroke: "#41A59B",
        "stroke-width": 1,
        "stroke-linejoin": "round",
        scale: [1, 1]
      },
      
      // The styles for the hover
      'labelBackingHoverStyles': {
        fill: "#C7F464",
        stroke: "#ADCC56",
      },
      'labelTextStyles': {
      fill: "#222",
        'stroke': 'none',
        'font-weight': 300,
        'stroke-width': 0,
        'font-size': '10px'
      },
      click: function(event, data) {
      	var i = states.indexOf(data.name);
      	if(i >= 0){
      		states.splice(i, 1);
      	}else{

      		states.push(data.name);

      	}
      	var formattedStates = getStates(states);
      	document.getElementById("selected_states").value = formattedStates;
      	console.log(document.getElementById("selected_states").value);
        $('#clicked-state').html('<b>You clicked:</b> '+ formattedStates);
      }
    });