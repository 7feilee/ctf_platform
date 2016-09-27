#!/usr/bin/env python

import base64 as b
import subprocess
import wget

filename = 'woof64.jpg'
wget.download('https://pbs.twimg.com/profile_images/378800000822867536/3f5a00acf72df93528b6bb7cd0a4fd0c.jpeg', filename)

flag = "USCGA{the_best_base_is_the_base64}"

#for i in range(1):
#	print flag
flag = b.b64encode(flag)

subprocess.call(('exiftool '+filename+' -comment=%s' % flag ).split())
