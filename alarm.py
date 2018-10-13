import datetime 
import time
import random
import pygame
import sys
import numpy as np

def check(alarmTime):
	if len(alarmTime)==1:
		if alarmTime[0]<=24 and alarmTime[0]>0:
			return True

	if len(alarmTime)==2:
		if alarmTime[0]<=24 and alarmTime[0]>=0:
			if alarmTime[1]<60 and alarmTime[1]>=0:
				return True

	if len(alarmTime)==3:
		if alarmTime[0]<=24 and alarmTime[0]>=0:
			if alarmTime[1]<60 and alarmTime[1]>=0:
				if alarmTime[2]<60 and alarmTime[2]>=0:
					return True
	return False
	
print("Set the Alarm in HH:MM:SS format")

inputTime=raw_input()

try:
	alarmTime=[int(a) for a in inputTime.split(":")]
	if check(alarmTime):
		True
		
	else:
		raise ValueError

except ValueError:
	print("Invalid format.Enter it correctly!")
	sys.exit()

TotalSeconds=3600*alarmTime[0]+60*alarmTime[1]+1*alarmTime[2]


current=datetime.datetime.now()
currentTime=3600*current.hour+60*current.minute+1*current.second

diff=TotalSeconds-currentTime

if diff<0:
	diff=diff+86400

print("I will wake you in %s" % datetime.timedelta(seconds=diff))

time.sleep(diff)

print("Get up!!")

#setting the audio file
pygame.init()
pygame.mixer.music.load("alarm.mp3")
pygame.mixer.music.play()
time.sleep(10)


			
