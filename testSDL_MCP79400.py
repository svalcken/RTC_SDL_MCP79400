#!/usr/bin/env python
#
# Test SDL_MCP79400
# John C. Shovic, SwitchDoc Labs
# 07/28/2014
#
# Evaluation of the following RTC Clocks
#
#	DS1307
#	MCP79400
#	DS3231 
# 	PCF8563 
#

# imports

import sys
import time
import datetime

import SDL_MCP79400

# Main Program

print ""
print "Test SDL_MCP79400 Version 1.0 - SwitchDoc Labs"
print ""
print ""
print "Program Started at:"+ time.strftime("%Y-%m-%d %H:%M:%S")

filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"
starttime = datetime.datetime.utcnow()

# MCP79400
# Note:  MCP79400 can't quite use the same library as DS1307 for read/write time
# There are differences in starting the clock
mcp79400 = SDL_MCP79400.SDL_MCP79400(1, 0x6F)
mcp79400.write_now()

# Main Loop - sleeps 10 minutes, then reads and prints values of all clocks


while True:

	currenttime = datetime.datetime.utcnow()

	deltatime = currenttime - starttime
 
	print ""
	print "Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S")
	
	print "MCP79400=\t\t%s" % mcp79400.read_datetime()

	time.sleep(10.0)
