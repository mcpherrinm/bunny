#!/usr/bin/env python2

from glob import glob
from PIL import Image
import sys

images = sorted(glob("frame_*.gif"))

charwidth=8
charheight=13

charset=[]
charmap=[" ", "@", "/", "t", "(", "%", "G", "~",
         "O","^", "C", "s", "#", "7"]

def printchar(c):
  if c < len(charmap):
    sys.stdout.write(charmap[c])
  else:
    print "unknown", c
    sys.exit(1)

print "import time"
for imagename in images:
  print "time.sleep(0.2)"
  print "print \"\033[2J\033[;H\" "
  print "print \"\"\""
  image = Image.open(imagename)
  for row in range(0, image.size[1], charheight):
    for col in range(0, image.size[0]-charwidth, charwidth):
      # This gives us the index of each character.
      # we pull that into a list and output either the char or index
      char=[]
      for charcol in range(col, col+charwidth):
        for charrow in range(row, row+charheight-2):
          char.append(image.getpixel((charcol, charrow)))
      if not char in charset:
        charset.append(char)
      printchar(charset.index(char))
    print
  print "\"\"\""
