#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-08-25 20:23:52
# @Last Modified by:   john
# @Last Modified time: 2016-08-25 20:32:26

from random import shuffle, randint

h = open('orchestra','w')

total_bytes = 1000
mess = []
for i in range(total_bytes):
	possibs = range(0, 255)
	shuffle(possibs)
	for k in possibs:
		mess.append(chr(k))

	if i == total_bytes/2:
		mess.append("USCGA{there_is_no_orchestra_without_the_strings}")

content =  "".join(mess)
h.write(content)
h.close()
