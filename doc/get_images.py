#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
from subprocess import call

filename= 'imglist.txt'
with open(filename, 'r') as myfile:
    content = myfile.read().replace('\n', '')
    ##\((https?://www.fiware.org/wp-content/uploads/.*?\.(?:jpeg|png))\)
    results = re.findall('\((https?://www.fiware.org/wp-content/uploads/.*?\.(?:jpeg|png|jpg))\)', content)

    for link in results:
        path = re.sub('https?://www.fiware.org/wp-content/', '', link)
        print link + "-->" + path
        #os.makedirs(path, mode=0x777, exist_ok=True)
        call(["curl","-L","--create-dirs","-o", path, link])

