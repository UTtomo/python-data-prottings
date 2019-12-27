(function(){
  'use strict';

  var btn = document.getElementById('btn');
  var Gpio = require('onoff').Gpio; //include onoff to interact with the GPIO
  var LED = new Gpio(4, 'out'); //use GPIO pin 4 as output
  var pushButton = new Gpio(17, 'in', 'both'); //use GPIO pin 17 as input, and 'both' button presses, and releases should be handled
  
  btn.addEventListener('click',function(err,value){
    
    　LED.writeSync(value); //turn LED on or off depending on the button state (0 or 1)
  });
  

  
})();
