import os
import re
#TODO: add exception/ error handling, make it clean

def rename_files():
  files = os.listdir("/home/idontremember/Documents/dev/web/udacity/prank")
  save_curr = os.getcwd()
  os.chdir("/home/idontremember/Documents/dev/web/udacity/prank")
  for name in files:
    print("Old file name > " + name)
    new_name = re.sub(r'\d+', '', name)
    print("New file name > " + new_name)
    os.rename(name, new_name) 
  os.chdir(save_curr)
   # alternative could be using string.translate function as suggested in udacit   course
rename_files()
