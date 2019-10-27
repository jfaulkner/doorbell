#!/usr/bin/python
import random
import subprocess
import RPi.GPIO as GPIO
sounds = ["./1.wav","./2.wav","./3.wav","./4.wav","./5.wav"]
count = 0

def scream(channel):
  global count
  count = count + 1
  if count % 2 == 0:
    subprocess.call(["aplay",sounds[random.randint(0,len(sounds)-1)]])

subprocess.call(["amixer","cset","numid=3","1"])
subprocess.call(["aplay",sounds[0]])

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(23,GPIO.FALLING,callback=scream,bouncetime=300)
print("... waiting for doorbell ...")

raw_input("--- Press ENTER to quit ---\n")

GPIO.cleanup()

