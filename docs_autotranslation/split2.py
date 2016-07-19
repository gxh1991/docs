#!/usr/bin/env python
import re
import os

#Filenames for each guide
guides = ['header','section_Git_and_Gerrit_Setup','section_Hacking_from_CLI','developing-app','alto/alto-developer-guide','armoury/odl-armoury-dev','bgpcep/odl-bgpcep-bgp-all-dev'
,'capwap/capwap-dev','controller/controller','didm/didm-dev','dlux/dlux-core-dev','iotdm/iotdm-dev','l2switch/l2switch-dev','lacp/lacp-dev.adoc','messaging4transport/messaging4transport-developer',
'controller/netconf/odl-netconf-dev','nic/nic-dev','nemo/odl-nemo-engine-dev','netide/netide-developer-guide','neutron/neutron','sdninterfaceapp/odl-sdninterfaceapp-all-dev',
'openflowjava/odl-openflowjava-protocol-dev','openflowplugin/odl-ofp-developer-guide','opflex/agent-ovs-dev','opflex/genie-dev','opflex/libopflex-dev',
'ovsdb/ovsdb-southbound-developer', #newly added guides
'ovsdb/ovsdb-openstack-developer','ovsdb/ovsdb-sfc-developer','ovsdb/ovsdb-hwvtep-developer',
'bgpcep/odl-bgpcep-pcep-all-dev','packetcable/packetcable-dev','sfc/sfc','sxp/odl-sxp-dev','tcpmd5/odl-tcpmd5-all-dev',
'topoprocessing/odl-topoprocessing-framework-dev','ttp/ttp-model-dev','ttp/ttp-cli-tools-dev','usc/odl-usc-channel-dev','vtn/vtn-dev','yangtools/yangtools',
'yang-push/odl-yang-push-dev']

guidesDirectory = 'tmp1'


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
	output = []
	for i in range(0,len(lineNumber)):
		if i != len(lineNumber)-1:
			start = lineNumber[i] - 1
			end = lineNumber[i+1] -1
			output.append(printLines(lines,start,end))
		else:
			start = lineNumber[i] - 1
			end = len(lines)
			output.append(printLines(lines,start,end))
	return output

def containsSlash(str):
	if str == '':
		return False
	for s in str:
		if s == '/':
			return True
	return False

def initDirectory( str ):
	if containsSlash(str) == False:
		return 
	else:
		dir = str.split('/')[0]
		try:
			os.stat(guidesDirectory+'/'+dir)
		except:
			os.mkdir(guidesDirectory+'/'+dir)
		return

def printToFile( textList ):
	number = 0

	for text in textList:
		try:
			#file = open('tmp1/'+ str(number),'w')
			file = open(guidesDirectory+'/'+ guides[number],'w')
		except:
			#os.mkdir('tmp1')
			print guides[number]
			file = open(guidesDirectory+'/'+ guides[number],'w')
		file.write(text)
		file.close()
		number += 1
	return



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
	if isGuideHeader(lineAbove,line):
		lineNumber.append(deGuide.line-1)
	lineAbove = line
	line = deGuide.readline()

for guide in guides:
	initDirectory(guide)



deGuide = FileWrapper(open("developer-guide/index.rst"))
lines = deGuide.readlines()

textList = getGuides(lines,lineNumber)
printToFile(textList)

