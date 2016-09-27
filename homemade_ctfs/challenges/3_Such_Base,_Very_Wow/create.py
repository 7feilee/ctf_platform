#!/usr/bin/env python

import base64 as b
import subprocess
import wget
wget.download('http://barkpost-assets.s3.amazonaws.com/wp-content/uploads/2013/11/muchdoge-700x393.jpg', 'woof64^10.jpg')

flag = "USCGA{base64_squared_could_still_be_base64}"

for i in range(10):
#	print flag
	flag = b.b64encode(flag)

subprocess.call(('exiftool woof64^10.jpg -comment=%s' % flag ).split())
