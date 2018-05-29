var velocidad = 80;
var tamano = 10;



function dibujar(){
	var canvas = document.getElementById('canvas');
	var ctx = canvas.getContext('2d');
	ctx.clearRect(0,0, canvas.width, canvas.height);
}

function main(){

}

setInterval('main', velocidad)