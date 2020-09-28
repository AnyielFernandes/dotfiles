#!/bin/bash 
#This script executes some commands on the startup of qtile, so that some stuff gets fixed. 


# This configures the output for dual screen environment. 
if xrandr | grep "HDMI1" | grep -o "connected" >&2; then 
	xrandr --output eDP1 --mode 1366x768 --pos 1920x233 --rotate normal \
	--output HDMI1 --mode 1920x1080 --pos 0x0 --primary --rotate normal	
fi 


#It removes every tmp file in the qtile scripts directory
scripts_dir="/home/anyel/.config/qtile/scripts"
find "$scripts_dir" -name "*.tmp" -exec rm {} \;   

picom & 
feh --bg-scale --randomize /home/anyel/backgrounds
