#!/usr/bin/env python
import os

header = open('header.rst','w')
text = header.read()
header.close()
file = open('index.rst','w')
file.write(text)
file.write('.. toctree:: \n')
file.write(':maxdepth: 1 \n')