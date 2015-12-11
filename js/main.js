function run() {
	var timespans = ['1990-2000', '2000-2010'];
	var container = document.getElementById('container');
	var globe = new DAT.Globe(container);

	//console.log(globe);
	var i, tweens = [];
			  
	globe.animate();
	document.body.style.backgroundImage = 'none';
				
	var settimespan = function(globe, t) {
		return function() {
			new TWEEN.Tween(globe).to({time: t/timespans.length},500).easing(TWEEN.Easing.Cubic.EaseOut).start();
			var y = document.getElementById('timespan'+timespans[t]);
			if (y.getAttribute('class') === 'timespan active') {
				return;
			}
			var yy = document.getElementsByClassName('timespan');
			for(i = 0; i < yy.length; i++) {
				yy[i].setAttribute('class','timespan');
			}
			y.setAttribute('class', 'timespan active');
		};
	};
		  
	for(var i = 0; i < timespans.length; i++) {
		var y = document.getElementById('timespan'+timespans[i]);
		y.addEventListener('mouseover', settimespan(globe,i), false);
	}
			  
	var xhr;
	TWEEN.start();
				  
	xhr = new XMLHttpRequest();
	xhr.open('GET', '/json/data.json', true);
	xhr.onreadystatechange = function(e) {
		if (xhr.readyState === 4) {
			if (xhr.status === 200) {
				var data = JSON.parse(xhr.responseText);
				window.data = data;
				for (i = 0; i < data.length; i++) {
					globe.addData(data[i][1], {format: 'magnitude', name: data[i][0], animated: true});
				}
				globe.createPoints();
				settimespan(globe,0)();
				globe.animate();
				document.body.style.backgroundImage = 'none';
			}
		}
	};
	xhr.send(null);
}