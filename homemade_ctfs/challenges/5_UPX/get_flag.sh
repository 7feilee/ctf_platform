#!/bin/sh

upx -d delivery -o unpacked >/dev/null 2>&1
strings unpacked | grep "USCGA"
rm unpacked	

