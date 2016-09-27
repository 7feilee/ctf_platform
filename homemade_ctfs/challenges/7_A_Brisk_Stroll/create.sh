#!/bin/bash

gcc source.c -o who_put_this_here -m32
cat original.png who_put_this_here > a_walk_with_the_numbers.png

