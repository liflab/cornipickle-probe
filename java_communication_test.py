#!/usr/bin/python

import subprocess

p = subprocess.Popen(["java", "-jar", "cornipickle/Cornipickle.jar"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
p.stdin.write("First line\n")
p.stdin.write("Second line\n")
p.stdin.write("x\n") # this line will not be printed into the file

f = open('resultPython.txt','w')
line = p.stdout.readline()
while(line != "x\n"):
	f.write(line)
	line = p.stdout.readline()
