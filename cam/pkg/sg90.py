# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time
import atexit

# 这个类表示单个的SG90模块
class Steering:
    max_delay = 0.2
    min_delay = 0.05

    def __init__(self, channel, init_position, min_angle, max_angle, speed):
        self.channel = channel
        self.init_position = init_position
        self.position = init_position
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.speed = speed

        atexit.register(GPIO.cleanup)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.channel, GPIO.OUT, initial=False)

        self.pwm = GPIO.PWM(self.channel, 50)  # PWM
        self.pwm.start(2.5 + 10 * self.position / 180)  # 让舵机转到初始位置
        time.sleep(Steering.max_delay)
        self.pwm.ChangeDutyCycle(0)  # 这一步比较重要，如果不加的话，舵机会不规则抖动（具体原因还不知道）
        time.sleep(Steering.min_delay)

    def forwardRotation(self):
        print("current postion: " + str(self.position))

        if (self.position + self.speed) <= self.max_angle:
            self.position = self.position + self.speed
            self.pwm.ChangeDutyCycle(2.5 + 10 * self.position / 180)  # 设置舵机角度
            time.sleep(Steering.min_delay)
            self.pwm.ChangeDutyCycle(0)  # 舵机回到中位
            time.sleep(Steering.min_delay)

    def reverseRotation(self):
        print("current postion: " + str(self.position))

        if (self.position - self.speed) >= self.min_angle:
            self.position = self.position - self.speed
            self.pwm.ChangeDutyCycle(2.5 + 10 * self.position / 180)  # 设置舵机角度
            time.sleep(Steering.min_delay)
            self.pwm.ChangeDutyCycle(0)  # 舵机回到中位
            time.sleep(Steering.min_delay)

    def reset(self):
        self.position = self.init_position
        self.pwm.start(2.5 + 10 * self.init_position / 180)  # 让舵机转到初始位置
        time.sleep(Steering.max_delay)
        self.pwm.ChangeDutyCycle(0)  # 这一步比较重要，如果不加的话，舵机会不规则抖动（具体原因还不知道）
        time.sleep(Steering.min_delay)

    def stop(self):
        self.pwm.stop()
        time.sleep(Steering.max_delay)
        GPIO.cleanup()


vertical_steer = Steering(20, 90, 60, 180, 15) # GPIO编号 初始角度 最小角度 最大角度 每次旋转的角度
horizontal_steer = Steering(21, 90, 45, 150, 15)

if __name__ == "__main__":
    steer = Steering(21, 90, 0, 180, 15)
    while True:
        direction = input("Please input direction: ")
        if direction == "F":
            steer.forwardRotation()
        elif direction == "R":
            steer.reverseRotation()
        elif direction == "S":
            steer.stop()