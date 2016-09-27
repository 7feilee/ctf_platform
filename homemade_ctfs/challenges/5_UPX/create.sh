#!/bin/sh

gcc source.c -o delivery -m32 -static
upx --exact delivery
