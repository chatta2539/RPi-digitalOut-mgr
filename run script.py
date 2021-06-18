from digitalOut import digitalOut
import time

lib = digitalOut()

lib.pinoutOff() #Turn off all port of Do
time.sleep(1)
lib.pinoutOn() #Turn on all port of Do
time.sleep(1)
print(lib.pinoutStateAll()) #Check state all of Do in array [True, True, True]
time.sleep(1)
lib.pinoutControl(1, False) #Control Do via defined (pin 1-3) and state (True or False)
time.sleep(1)
print(lib.pinoutState(1)) #Check state by port via defined the port to check the state