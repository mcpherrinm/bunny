#!/usr/bin/env python2

from glob import glob
from PIL import Image
import sys

images = sorted(glob("frame_*.gif"))

charwidth=8
charheight=13

charset=[]
charmap=[' ', '@', '~', 't', '(', '%', '^', 's',
         '/', 'C', 'G', 'O', '#', '7']

def printchar(c, char):
  if c < len(charmap):
    sys.stdout.write(charmap[c])
  else:
    print_unknown(char)
    sys.exit(1)


def print_unknown(char):
  matrix = [[0 for x in xrange(20)] for x in xrange(20)]
  i = 0
  for c in char:
    x = i / 11
    y = i % 11
    matrix[y][x] = c
    i += 1

  print
  print "unknown:"
  print "'''"
  for y in range(len(matrix)):
    for x in range(len(matrix[y])):
      c = matrix[y][x]
      if c == 1:
        pixel = ' '
      elif c == 0:
        pixel = '#'
      else:
        raise
      sys.stdout.write(pixel)
    print
  print "'''"


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
      printchar(charset.index(char), char)
    print
  print "\"\"\""
