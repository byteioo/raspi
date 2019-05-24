import RPi.GPIO as GPIO
import atexit

class Led:
    def __init__(self, channel):
        self.channel=channel
        atexit.register(GPIO.cleanup)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.channel, GPIO.OUT)

    def open(self):
        GPIO.output(self.channel, GPIO.LOW)

    def close(self):
        GPIO.output(self.channel,GPIO.HIGH)
    def stop(self):
        GPIO.cleanup()

led=Led(channel=26)
if __name__ == "__main__":
    led=Led(26)
    while True:
        direction = input("Please input direction: ")
        if direction == "O":
            led.open()
        elif direction == "C":
            led.close()
        elif direction == "S":
            led.stop()