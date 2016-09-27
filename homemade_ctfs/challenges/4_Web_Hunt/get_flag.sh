#!/bin/sh

yes |  unzip nothinginthebox.zip >/dev/null 2>&1

grep -RPoh "USCGA{.*?}" nothinginthebox.com
