    webiopi().ready(function() {
        // Create a "Light" labeled button for GPIO 17
        var button = webiopi().createGPIOButton(17, "Light");
 
        // Append button to HTML element with ID="controls" using jQuery
        $("#controls").append(button);
 
        // Refresh GPIO buttons
        // pass true to refresh repeatedly of false to refresh once
                webiopi().refreshGPIO(true);
    });
