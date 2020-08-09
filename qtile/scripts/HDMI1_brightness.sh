#!/bin/bash
#This script controlls the brightness of the HDMI1 connected monitor 
var_file="/home/anyel/.config/qtile/scripts/brightness_file.tmp"
screen="HDMI1"
variation=0.08
minimum=0.4

usage(){
	echo "Usage $0 [+|-] " >&2
	echo "  + : increments brightness in 10%" >&2 
	echo "  - : decrements brightness in 10%" >&2 
}

if [ $# -ne 1 ] || [[ "$1" =~ [^+-=] ]]; then 
	usage
	exit 1 
fi 
 
if [ ! -e "$var_file" ] || [ "$1" = "=" ] ; then 
	echo "1" > "$var_file"
	xrandr --output "$screen" --brightness 1
	exit 0 
fi 

actual=$(<"$var_file")
new_brightness=$( echo "$actual $1 $variation " | bc  )

if [ $( echo "$new_brightness < $minimum" | bc ) = 1 ]; then 
	new_brightness="$minimum"
elif [ $( echo "$new_brightness > 1" | bc ) = 1 ]; then 
	new_brightness=1
fi

echo "$new_brightness" > "$var_file"
xrandr --output "$screen" --brightness "$new_brightness"



