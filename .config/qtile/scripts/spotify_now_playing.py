#!/usr/bin/python
from subprocess import call
import os
import dbus

session_bus = dbus.SessionBus()
spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                     "/org/mpris/MediaPlayer2")
spotify_properties = dbus.Interface(spotify_bus,
                                    "org.freedesktop.DBus.Properties")
metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

# The property Metadata behaves like a python dict
for key, value in metadata.items():
    print (key, value)

# To just print the title
song = metadata['xesam:title']
album = metadata['xesam:album']
artist = metadata['xesam:artist'][0]
icon = "/home/anyel/.config/qtile/icons/spotify_icon.png"
options = "-i " + icon + " -u low"
notify_send = "/usr/bin/notify-send"
notify_msg = " 'Song: " + song + "\n  By: " + artist +"'"
command = notify_send + " " + options + " " + notify_msg

os.system(command)
