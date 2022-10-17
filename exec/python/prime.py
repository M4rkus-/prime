#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, time

def pgen():
  ''' ... generates the sequence of all primes: 2,3,5,7,11 ... 
  '''

  p=2
  f=1

  try:

    ts2=time.time()

    while(True):

      if f%p%2: sys.stdout.write(str(p)+"\n")
      p+=1
      f*=(p-2)

  except:

#   raise KeyboardInterrupt .. Ctrl-C

    ts2-=time.time()
    sys.stderr.write("time: "+str(round(-ts2,3))+" sec\n")

def main():
  pgen()
  sys.exit()

if __name__=="__main__":
  main()
