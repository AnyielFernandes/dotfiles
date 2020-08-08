#!/bin/bash 
var_file="brightness_file"
if [ ! -e  "$var_file" ] ; then 
	echo "1" > "$var_file"
fi 

actual=$(<"$var_file") 

if [ "$actual" -eq "1" ] ; then 
	xrandr --output HDMI1 --brightness 0.7
else
	xrandr --output HDMI1 --brightness 1
fi 


echo " 1 - $actual" | bc > "$var_file" 
