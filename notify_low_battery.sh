#!/bin/bash 
#This script sends a notification if battery is under a defined perfentage, 
#and it is not charging

warning_at=60
battery_level=$( acpi | egrep -o "[0-9]{2}%" | head -c 2 ) 

if [ $battery_level -lt $warning_at ] && acpi | grep "Discharging" &>/dev/null; then 
	notify-send -i /home/anyel/allpha/icons/low-battery.svg "low battery" -u critical
fi
