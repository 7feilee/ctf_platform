#!/bin/sh

exiftool woof64.jpg | grep "Comment" | cut -d ":" -f2 | while read line; do echo $line|base64 -d; done
