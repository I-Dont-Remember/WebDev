import urllib
def read_text():
  the_file= open("/home/idontremember/Documents/dev/web/udacity/taco.txt")
  contents = the_file.read()
  the_file.close()
  check_curses(contents)

def check_curses(text):
  connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
  output = connection.read()
  print(output)
  connection.close()

read_text()

