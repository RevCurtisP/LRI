#!/bin/python

#lri2txt.py - Print LRI image as Unicode Characters

gfxchars = [' ','\u2597','\u2596','\u2584','\u259D','\u2590','\u259E','\u259F',
       '\u2598','\u259A','\u258C','\u2599','\u2580','\u259C', '\u259B', '\u2588']

def lri2txt(lridata):
  lines = []
  line = ""
  for char in lridata.upper():
    if char<'A' or char>'P': continue
    index = ord(char) - 65
    line += gfxchars[index]
    if len(line) == 16:
      lines.append(line + '\n')
      line = ""
  return lines

lrifilename = "atom-white.lri"
txtfilename = "atom-white.txt"
with open(lrifilename) as lrifile:
  lridata = lrifile.read()
  text = lri2txt(lridata)
  with open(txtfilename, 'w', encoding='utf-8') as txtfile:
    txtfile.writelines(text)
