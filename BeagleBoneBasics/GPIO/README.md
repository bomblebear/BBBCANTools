## GPIO with Adafruit-BBIO

First you need to install [Adafruit_BBIO](https://pypi.org/project/Adafruit-BBIO/)
```bash
apt-get update
sudo apt-get install python-pip python-setuptools python-smbus 

pip install Adafruit_BBIO 

#you can excute .py with
python xx.py

#or
chmod u+x xx.py
./xx.py

```

some basic codes
```python
#Importing the Adafruit’s BeagleBone IO Python Library 
import Adafruit_BBIO.GPIO as GPIO 
#Setting pin’s direction to output
GPIO.setup("P8_12", GPIO.OUT) 
#Writing a pin HIGH 
GPIO.output("P8_12", GPIO.HIGH) 
#Writing a pin LOW 
GPIO.output("P8_12", GPIO.LOW) 
#Setting a pin’s direction to input 
GPIO.setup("P8_14", GPIO.IN) 
#Reading an input pin’s value (will return 0 or GPIO.LOW for low and 1 or GPIO.HIGH for high) 
GPIO.input("P8_12") 
#Setting a pin for PWM (at 50% duty cycle) 
import Adafruit_BBIO.PWM as PWM 
PWM.start("P8_13", 50) 
#Changing the PWM duty cycle 
PWM.set_duty_cycle("P8_13", 25) 
#Setting up analog input 
import Adafruit_BBIO.ADC as ADC 
ADC.setup() 
#Reading an analog input (returns a value between 0 and 1) 
analogReading = ADC.read("P9_39") 
```

