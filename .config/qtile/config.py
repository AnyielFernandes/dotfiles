# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

from os import listdir
from os import path
import subprocess
import json
import os


#Some useful variables
home = path.expanduser('~')
qtile_path = path.join(home, ".config", "qtile")
myTerm = "alacritty"
mod = "mod4"

keys = [
    ### Window controls
    Key([mod], "k",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "i",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod], "l",
        lazy.layout.right(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "j",
        lazy.layout.left(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_up(),
        desc='Move windows up in current stack'
        ),
    Key([mod], "o",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "u",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod], "s", lazy.spawn("spotify")),
    Key([mod], "n", lazy.spawn("nautilus")),
    Key([mod], "d", lazy.spawn("discord")),
    Key([mod, "shift" ], "w", lazy.spawn("libreoffice --writer")),
    Key([mod],"v",lazy.spawn("virtualbox")),

    # Toggle between different layouts as defined below
    Key([mod], "q", lazy.next_layout()),
    Key([mod], "Tab", lazy.prev_layout()),
    Key([mod], "w", lazy.window.kill()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod,"control"],"Escape",lazy.spawn("systemctl poweroff")),
    Key([mod,"control"],"s",lazy.spawn("systemctl suspend")),
    Key([mod], "r", lazy.spawn("rofi -show drun")),

    #Monitor commands: 
    Key([mod], "Escape", lazy.next_screen() ),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 3- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 3+ unmute")), 
    Key([], "XF86AudioPlay", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")),
    Key([], "XF86AudioNext", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")),
    Key([], "XF86AudioPrev", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")),

    #Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    Key([mod],"F1", lazy.spawn("bash /home/anyel/.config/qtile/scripts/HDMI1_brightness.sh =")),
    Key([mod],"Up", lazy.spawn("bash /home/anyel/.config/qtile/scripts/HDMI1_brightness.sh +")),
    Key([mod],"Down", lazy.spawn("bash /home/anyel/.config/qtile/scripts/HDMI1_brightness.sh -")),
    #Night light
    Key([mod],"Right",lazy.spawn("redshift -Pg 0.8:0.7:0.8 -O 4800")), 
    Key([mod],"Left",lazy.spawn("redshift -x")),

    #Bar
    Key([mod], "BackSpace" , lazy.hide_show_bar("top")),
    
]


##### GROUPS #####
group_names = [("", {'layout': 'max'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'max'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'max'}),
               ("", {'layout': 'max'}),
               ("", {'layout': 'stack'}),
               ("", {'layout' : 'max'}),
               ("", {'layout': 'max'}), ]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group	




layout_conf = {
    'border_focus': '#ffffff',
    'border_width': 1,
    'margin':3 
}

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.Matrix(**layout_conf),
    layout.VerticalTile(**layout_conf,border_normal="#000000"),
    layout.Stack(num_stacks=2,**layout_conf),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    #layout.Columns(),
    #layout.MonadWide(**layout_conf),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.Zoomy(),
]



##### COLORS #####
colors = [["#13001f"], # panel background 0
          ["#434758"], # background for current screen tab 1
          ["#ffffff"], # font color for group names 2
          ["#9d00ff"], # border line color for current tab 3
          ["#00294a"], # odd widgets 4
          ["#1e3a61"], # color for the even widgets 5
          ["#e1acff"], # window name 6
          ["#858585"], # color for non active windows 7
          ["#6900ab"]] # color for selected group on non selected screen 8

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Copperplate",
    fontsize = 12,
    padding = 2,
    background=colors[0]
)

extension_defaults = widget_defaults.copy()

separator_A = widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -1,
                       fontsize = 50
                       )
background_A = { 'background' : colors[4],
                 'foreground' : colors[2]}

separator_B = widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -1,
                       fontsize = 50
                       )
background_B = { 'background' : colors[5],
                 'foreground' : colors[2]}

background_C = { 'background' : colors[0],
                 'foreground' : colors[2]}

myBar = [ widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                        ),
                widget.Image(
                    background = colors[0],
                    filename = "/home/anyel/.config/qtile/icons/Manjaro_Icon.svg",
                    mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('/home/anyel/.config/xmenu/xmenu.sh')},
                    margin = 3 
                    ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[7],
                        background = colors[0]
                        ),
                widget.Sep(
                        linewidth = 0,
                        padding = 7,
                        foreground = colors[7],
                        background = colors[0]
                        ),
                widget.GroupBox(
                        font = "Ubuntu Bold",
                        fontsize = 13,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 6,
                        borderwidth = 3,
                        active = colors[2],
                        inactive = colors[7],
                        rounded = True,
                        highlight_color = colors[1],
                        highlight_method = "line",
                        this_current_screen_border = colors[3],
                        this_screen_border = colors [8],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[8],
                        foreground = colors[2],
                        background = colors[0]
                        ),
                widget.Prompt(),
                widget.Sep(
                        linewidth = 0,
                        padding = 40,
                        foreground = colors[2],
                        background = colors[0]
                        ),
                widget.WindowName( foreground = colors[6], background = colors[0], padding = 0, show_state = False ),
                
                widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = -1,
                       fontsize = 50
                       ),
                widget.CurrentLayoutIcon(
                        scale = 0.7, 
                        **background_A
                        ),

                widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -1,
                       fontsize = 50
                       ),

                widget.TextBox(
                        text = "  ",
                        padding = 0,
                        fontsize = 15, 
                        mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('nm-connection-editor')},
                        **background_B

                ),

                widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -1,
                       fontsize = 50
                       ),

                widget.TextBox(
                        text = "  ",
                        padding = 2,
                        fontsize = 15, 
                        mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('blueman-adapters')},
                        **background_A
                ),

                widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -1,
                       fontsize = 50
                       ),

                widget.Battery(
                        charge_char = " ",
                        discharge_char = "",
                        empty_char = "",
                        full_char = "",
                        low_foreground = colors[6],
                        notify_below = 0.15,
                        fontsize = 14,
                        format = '{char} {percent:2.0%}', 
                        update_interval = 1,
                        **background_B
                ),
    
                widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -1,
                       fontsize = 50
                       ),

                widget.TextBox(
                        text = " ",
                        padding = 0,
                        fontsize = 14, 
                        **background_A
                ),
                widget.Volume(
                        padding = 5, 
                        fontsize = 14,
                        **background_A
                        ),

                widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -1,
                       fontsize = 50
                       ),
                
                widget.TextBox(
                        text = " ",
                        padding = 2,
                        fontsize = 14, 
                        **background_B
                        ),
                widget.Pacman(
                        update_interval = 1800,
                        font = "Ubuntu Bold",
                        **background_B
                        ),
                widget.TextBox(
                        text = "Updates",
                        padding = 5,
                        font = "Ubuntu Bold",
                        **background_B
                        ),

                widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -1,
                       fontsize = 50
                       ),
                
                widget.Clock(
                        format = " %A, %B %d  %H:%M ", 
                        font = "Ubuntu Bold",
                        **background_A
                        ),

                widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[0],
                       padding = -1,
                       fontsize = 50,
                       ),

                widget.Systray(
                        padding = 5,
                        **background_C
                        ),

                widget.Sep(
                        linewidth = 0,
                        padding = 6, 
                        **background_C
                ),

            ]




screens = [
    Screen(
        top=bar.Bar(
            myBar
            ,
            24,
        ),
    ),

    # Screen 2 
    Screen(
        top=bar.Bar(
                [ widget.Sep(
                        linewidth = 0,
                        padding = 6,
                        foreground = colors[2],
                        background = colors[0]
                        ),
                widget.Image(
                    background = colors[0],
                    filename = "/home/anyel/.config/qtile/icons/Manjaro_Icon.svg",
                    mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('/home/anyel/.config/xmenu/xmenu.sh')},
                    margin = 3 
                    ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[7],
                        background = colors[0]
                        ),
                widget.Sep(
                        linewidth = 0,
                        padding = 7,
                        foreground = colors[7],
                        background = colors[0]
                        ),
                widget.GroupBox(
                        font = "Ubuntu Bold",
                        fontsize = 13,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 5,
                        padding_x = 6,
                        borderwidth = 3,
                        active = colors[2],
                        inactive = colors[7],
                        rounded = True,
                        highlight_color = colors[1],
                        highlight_method = "line",
                        this_current_screen_border = colors[3],
                        this_screen_border = colors [8],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[8],
                        foreground = colors[2],
                        background = colors[0]
                        ),
                widget.Prompt(),
                widget.Sep(
                        linewidth = 0,
                        padding = 40,
                        foreground = colors[2],
                        background = colors[0]
                        ),
                widget.WindowName( foreground = colors[6], background = colors[0], padding = 0, show_state = False ),
                
                widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = -1,
                       fontsize = 50
                       ),
                widget.CurrentLayoutIcon(
                        scale = 0.7, 
                        **background_A
                        ),

                widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -1,
                       fontsize = 50
                       ),

                widget.TextBox(
                        text = "  ",
                        padding = 0,
                        fontsize = 15, 
                        mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('nm-connection-editor')},
                        **background_B

                ),

                widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -1,
                       fontsize = 50
                       ),

                widget.TextBox(
                        text = "  ",
                        padding = 2,
                        fontsize = 15, 
                        mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('blueman-adapters')},
                        **background_A
                ),

                widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -1,
                       fontsize = 50
                       ),

                widget.Battery(
                        charge_char = " ",
                        discharge_char = "",
                        empty_char = "",
                        full_char = "",
                        low_foreground = colors[6],
                        notify_below = 0.15,
                        fontsize = 14,
                        format = '{char} {percent:2.0%}', 
                        update_interval = 1,
                        **background_B
                ),
    
                widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -1,
                       fontsize = 50
                       ),

                widget.TextBox(
                        text = " ",
                        padding = 0,
                        fontsize = 14, 
                        **background_A
                ),
                widget.Volume(
                        padding = 5, 
                        fontsize = 14,
                        **background_A
                        ),

                widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -1,
                       fontsize = 50
                       ),
                
                widget.TextBox(
                        text = " ",
                        padding = 2,
                        fontsize = 14, 
                        **background_B
                        ),
                widget.Pacman(
                        update_interval = 1800,
                        font = "Ubuntu Bold",
                        **background_B
                        ),
                widget.TextBox(
                        text = "Updates",
                        padding = 5,
                        font = "Ubuntu Bold",
                        **background_B
                        ),

                widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -1,
                       fontsize = 50
                       ),
                
                widget.Clock(
                        format = " %A, %B %d  %H:%M ", 
                        font = "Ubuntu Bold",
                        **background_A
                        ),

                widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[0],
                       padding = -1,
                       fontsize = 50,
                       ),

                widget.Systray(
                        padding = 5,
                        **background_C
                        ),

                widget.Sep(
                        linewidth = 0,
                        padding = 6, 
                        **background_C
                ),

            ]
            ,
            24,
        ),
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


