#!/bin/bash 
#The script requires one parameter: 
#   git
#This option copies to the github project directory the files written in sourceFile
#the first line of sourceFile is the destination of the copy (actually the project's root folder)
#For the rest of the lines, there is just a file path per line
#   local
#!/bin/bash 
#This script updates the config files read from sourceFile
#The first line of sourceFile contains the source folder where the script will look for the files.
#The next lines consist of one file per line
#The files to be copied must have the same basename as the file read from sourceFile
#   clean
#Deletes all files in sourceFile

if [ $# -ne 1 ] ; then 
    echo "Usage: $0 [ git | local ]"
    exit 1
fi 


if [ "$1" != "local" ] && [ "$1" != "git" ] && [ "$1" != "clean" ] ; then 
    echo "Invalid option"
    echo "Available options: "
    echo -e "   git : updates project's root folder"
    echo -e "   local : updates local config files"
    exit 2
fi 

sourceFile="/home/anyel/allpha/configs/files"

if [ ! -f "$sourceFile" ] && [ ! -e "$sourceFile"] ; then 
    echo "Coultn't read source file : $sourceFile"
    exit 1
fi 

dest=$( head -n 1 < "$sourceFile" )

if [ "$1" = "git" ] ; then 
    while read file
    do
        [ -e "$file" ] && [ -r "$file" ] && cp -r $file $dest
    done <<< $( tail -n +2 < "$sourceFile" ) 
elif [ "$1" = "local" ] ; then 
    while read file
    do
        updated="$dest/$(basename "$file")"
        [ -e "$updated" ] && [ -r "$updated" ] && cp -r "$updated" "$file"
    done <<< $( tail -n +2 < "$sourceFile" ) 
else
    while read file
    do
        file=$( basename "$file" )
        rm -rf "$file"
    done <<< $( tail -n +2 < "$sourceFile" )
fi 
