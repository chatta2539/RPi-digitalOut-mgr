import RPi.GPIO as GPIO
arrPinout = [0, 26, 20, 21]
class digitalOut():

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for i in list(range(1, 4)):
            GPIO.setup(arrPinout[i], GPIO.OUT)

    def pinoutOff(self):
        for i in list(range(1, 4)):
            GPIO.output(arrPinout[i], 1)
            
        if self.pinoutState(1) == 1 and self.pinoutState(2) == 1 and self.pinoutState(3) == 1:
            return True
        else:
            return False

    def pinoutOn(self):
        for i in list(range(1, 4)):
            GPIO.output(arrPinout[i], 0)
        if self.pinoutState(1) == 0 and self.pinoutState(2) == 0 and self.pinoutState(3) == 0:
            return True
        else:
            return False
        
    def pinoutStateAll(self):
        stateAll = []
        for i in list(range(1, 4)):
            stateAll.append(not bool(GPIO.input(arrPinout[i])))
        return stateAll

    def pinoutControl(self, pinNumber, command):
        if not isinstance(command, bool):
            return False
        try:
            if pinNumber > 0 and pinNumber <= 3:
                GPIO.output(arrPinout[pinNumber], not command)
                return True
            else:
                raise ValueError("Value %d out of range digital output port" % (pinNumber,))
        except Exception as e:
            return e

    def pinoutState(self, pinNumber):
        try:
            if pinNumber > 0 and pinNumber <= 3:
                return not bool(GPIO.input(arrPinout[pinNumber]))
            else:
                raise ValueError("Value %d out of range digital output port" % (pinNumber,))
        except Exception as e:
            # print(e)
            return e
            
