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
	if len(title) != len(equalsSign):
		return False
	if isEquqalsSign(equalsSign):
		return True

deGuide = open("developer-guide/index.rst")
#deGuide = deGuideFile.read()

lineAbove = deGuide.readline()
line = deGuide.readline()

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
output = ''
for i in range(1,20):
	
	if isEquqalsSign(line.strip('\n')):
		output = lineAbove+line
		lineAbove = line
		line = deGuide.readline()
		while (isEquqalsSign(line.strip()) == False):
			output = output + line
			lineAbove = line
			line = deGuide.readline()
	else:
		lineAbove = line
		line = deGuide.readline()
print output

