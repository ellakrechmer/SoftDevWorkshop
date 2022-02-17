// EELs :: Eliza Knapp, Ella Krechmer, Lucas Lee
// SoftDev pd0
// K31 -- animation with JS
// 2022-02-15

var c = document.getElementById("playground");
var dotButton = document.getElementById("dotButton");
var dvdButton = document.getElementById("dvdButton");
var stopButton = document.getElementById("stopButton");

var ctx = c.getContext("2d");
ctx.fillStyle = "blue";
var img=new Image();
img.src="logo_dvd.jpg";


var x=c.height/2;
var y=c.width/2;

var imgWidth=60;
var imgHeight=40;

dx=5;
dy=5;


var clear = (e) => {
    ctx.clearRect(0, 0, c.width, c.height);
}


var radius = 0;
var growing = true;
var requestID;

var drawDot = (e) => {
    console.log("drawDot...")

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);

    clear(e);

    ctx.beginPath(); // this thingy resets the drawing so the circles aren't connected
    ctx.fillStyle = "red";
    ctx.arc(c.width/2, c.height/2, radius, 0, 2 * Math.PI);
    ctx.fill();

    if(radius > 250) growing = false;
    else if(radius < 1) growing = true;

    if(growing) radius++;
    else radius--;
}

var stopIt = (e) => {
    console.log("stopIt invoked...")
    console.log(requestID );

    window.cancelAnimationFrame(requestID);
}

var drawDVD = (e) => {
    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDVD);

    clear();

    ctx.drawImage(img, x, y, imgWidth, imgHeight);
    if (x+imgWidth===c.width || x===0) dx=-dx;
    if (y+imgHeight===c.height || y===0) dy=-dy;

    x+=dx;
    y+=dy;
}

dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", drawDVD);
stopButton.addEventListener("click", stopIt);
