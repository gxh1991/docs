#!/usr/bin/env python
import re

def isEquqalsSign( str ):
	if str.strip() == '':
		return False
	for ch in str:
		if ch != '=':
			return False
	return True

def isGuideHeader( title,equalsSign ):

	if not isEquqalsSign(equalsSign.rstrip()):
		return False
	if len(title.rstrip()) == len(equalsSign.rstrip()):
		return True
	else:
		return False	

def printLines(lines,start,end):
	out = ''
	while(start < end):
		out += lines[start]
		start += 1
	return out

def getGuides( lines, lineNumber ):
	output = ''
	for i in range(0,len(lineNumber)):
		if i != len(lineNumber)-1:
			start = lineNumber[i] - 1
			end = lineNumber[i+1] -1
			output += printLines(lines,start,end)
		else:
			start = lineNumber[i] - 1
			end = len(lines)
			output += printLines(lines,start,end)
	return output



class FileWrapper(object):
	def __init__(self,f):
		self.f = f
		self.line = 0
	def close(self):
		return self.f.close
	def readline(self):
		self.line += 1
		return self.f.readline()
	def readlines(self):
		return self.f.readlines()

deGuide = FileWrapper(open("developer-guide/index.rst"))

lineAbove = deGuide.readline()
line = deGuide.readline()

lineNumber = []

while (line != ''):
	output = ''
	if isGuideHeader(lineAbove,line):
		lineNumber.append(deGuide.line-1)
	lineAbove = line
	line = deGuide.readline()


print lineNumber
deGuide = FileWrapper(open("developer-guide/index.rst"))
lines = deGuide.readlines()
# for index in lineNumber:
# 	print lines[index-1]
print getGuides(lines,lineNumber)

# while (line != ''):
# 	output = ''
# 	if isEquqalsSign(line.strip('\n')):
# 		output = lineAbove+line
# 		lineAbove = line
# 		line = deGuide.readline()
# 		while (!isEquqalsSign(line.strip())):
# 			output = output + line
# 	else:
# 		lineAbove = line
# 		line = deGuide.readline()
# output = ''
# for i in range(1,20):
	
# 	if isEquqalsSign(line.strip('\n')):
# 		output = lineAbove+line
# 		lineAbove = line
# 		line = deGuide.readline()
# 		while (isEquqalsSign(line.strip()) == False):
# 			output = output + line
# 			lineAbove = line
# 			line = deGuide.readline()
# 	else:
# 		lineAbove = line
# 		line = deGuide.readline()
# print output

