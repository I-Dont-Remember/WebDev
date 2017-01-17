#!/usr/bin/python

import webbrowser
import time

twohrs = 2 * 60 * 60
curr = 0
breaks = 3

print("Program started on " + time.ctime())
while(curr < breaks):
  time.sleep(5)
  webbrowser.open("https://www.google.com", new=2)
  curr += 1


