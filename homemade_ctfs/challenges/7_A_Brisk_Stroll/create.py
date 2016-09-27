#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-08-25 22:29:17
# @Last Modified by:   john
# @Last Modified time: 2016-08-25 22:39:53

from random import *

from string import *
import subprocess

printable = ascii_lowercase + ascii_uppercase 

source = \
'''
#include <stdio.h>

int main(){
	
	printf("||");

}
'''

handle = open("source.c",'w')

for i in range(100):
	random = list(printable[:randint(4,len(printable))])
	random2 = list(printable[:randint(4,len(printable))])
	shuffle(random)
	shuffle(random2)
	random = "".join(random)
	random2 = "".join(random2)

	handle.seek(0)
	data = source.replace("||", random)
	print random
	handle.write( data )


	subprocess.call( str("gcc source.c -o " + random2 ).split())

handle.close()
