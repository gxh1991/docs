#!/usr/bin/env python
# This scirpt split developer-guide into independent rst files.

import re

deGuideFile = open("developer-guide/index.rst")
deGuide = deGuideFile.read()

pattern = '==+'
