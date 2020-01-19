seconds = 50
minutes = 59
hours = 12

import time

from turtle import *
setup()
t1 = Turtle()

while True:
    t1.clear()
    t1.write(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2), font = ("arial", 25, "normal"))  #the zfill forces Py to show 2 numbers like :05 seconds
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:  #this means when the seconds reach 60 youll zero out and add one to minutes
        seconds = 0
        minutes = minutes + 1

    if minutes == 60:  #this means when the minutes reach 60 youll zero out and add one to hours
        minutes = 0
        hours = hours + 1