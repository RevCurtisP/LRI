#!/bin/python

#raw2lri.py - Convert Raw Image to LRP image

#Raw Image is extracted from Monochrome 32x32 BMP file
#Consists of 32 lines of 4 bytes each
#Top line is bottom of image

import argparse

def raw2rli(rawdata, invert=False):
  if len(rawdata) != 128: raise Error("Incorrect Data Length")
  lridata = []
  for row in range(124, 0, -8):
    lriline = ""
    for index in range (0, 4):
      upperbyte = rawdata[row + index]
      lowerbyte = rawdata[row + index - 4]
      divisor = 64
      for i in range(0,4):
        upperbits = int(upperbyte / divisor) & 3
        lowerbits = int(lowerbyte / divisor) & 3
        rawchar = upperbits * 4 + lowerbits
        if invert: rawchar = 15 - rawchar
        lriline += chr(rawchar + 65)
        divisor /= 4
    lridata.append(lriline + '\n')
  return lridata

def main(imagename, invert=False):
  print("Converting", imagename)
  rawfilename = imagename+".raw"
  lrifilename = imagename+".LRI"
  with open(rawfilename, "rb") as rawfile:
    rawdata = bytearray(rawfile.read())
    lridata = raw2rli(rawdata, invert)
    with open(lrifilename, "w") as lrifile:
      lrifile.writelines(lridata)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("-i", help="Invert Image", action='store_true')
  parser.add_argument("imgname", help="Image Name (without extension")
  args = parser.parse_args()
  main(args.imgname, args.i)
