/*
   your PPTASK:

   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.

    		Write with your future self or teammates in mind.

    		If you find yourself falling out of flow mode, consult
    		other teams
    		MDN

   A few comments have been pre-filled for you...

   (delete this block comment once you are done)
*/

// EELs :: Eliza Knapp, Ella Krechmer, Lucas Lee
// SoftDev pd2
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };


var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

var green = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('green');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
var fib = function(n) {
  if(n < 0){
      return "Invalid Input";
  }
  else if(n == 0){
      return 0;
  }
  else if(n == 1){
      return 1;
  }
  else{
      return fib(n-1) + fib(n-2);
  }
};


// FAC
var fac = function(n) {
  if(n < 0){
      return "Invalid Input";
  }
  else if(n == 0){
      console.log("done");
      return 1;
  }
  else{
      return n * fac(n-1);
  }

};


// GCD
var gcd = function(a, b) {
    r = a % b;
    while (r != 0) {
        a = b;
        b = r;

        r = a % b;
    }

    return b;
}


//Button

var dasbut = document.getElementById("b");
dasbut.addEventListener('click', function(){addItem("woohoo")});
