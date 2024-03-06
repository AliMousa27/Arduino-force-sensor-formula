# Arduino-force-sensor-formula
## Connection
![image](https://github.com/AliMousa27/Arduino-force-sensor-formula/assets/114988369/e34fc40b-f3a5-47d9-9e65-fd8f520cbba7)

## Purpose
I couldnt find the formula for a force sensor online to convert the reading to newtons, so I used what i already knew from machine learning to get a model that overfits the specific given sensor.

## Extras

### Running the script
If you want to run the script for yourself and see the graph, you just need numpy and matplotlib installed

### Arduinio function
If you just want the function to copy paste into your code
the parameter reading is basically ```analogRead(PIN)``` to read the pin the force sensor is connected to
```
double get_force_in_newton(double reading) {
  double y = 0.03550409483919946 
           + 0.005699338211384924 * reading 
           - 2.4244948469120643e-05 * pow(reading, 2) 
           + 2.86084887870513e-07 * pow(reading, 3) 
           - 6.193324080239549e-10 * pow(reading, 4) 
           + 5.844506382269629e-13 * pow(reading, 5);
  return y;
}
```
### WARNING
this function is extremely overfitted and is practically useless for anything but that force sensor in tinkercad



