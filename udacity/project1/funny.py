#!/usr/bin/python

import webbrowser
import time

twohrs = 2 * 60 * 60
curr = 0
breaks = 7

print("Program started on " + time.ctime())
while(curr < breaks):
  time.sleep(1)
  webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=2)
  curr += 1


