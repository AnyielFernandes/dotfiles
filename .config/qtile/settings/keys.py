from libqtile.config import Key
from libqtile.command import lazy

myTerm = "alacritty"
mod = "mod4"

def switch_screens():
    @lazy.function
    def __inner(qtile):
        i = qtile.screens.index(qtile.current_screen)
        group = qtile.screens[i - 1].group
        qtile.current_screen.set_group(group)
    return __inner

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

    #Program shortcuts
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod], "s", lazy.spawn("spotify")),
    Key([mod], "n", lazy.spawn("nautilus")),
    Key([mod], "d", lazy.spawn("discord")),
    Key([mod, "shift" ], "w", lazy.spawn("libreoffice --writer")),
    Key([mod],"v",lazy.spawn("virtualbox")),
    Key([mod], "r", lazy.spawn("rofi -show drun")),
    Key([],"Print", lazy.spawn("xfce4-screenshooter")),

    # Toggle between different layouts as defined below
    Key([mod], "q", lazy.next_layout()),
    Key([mod], "Tab", lazy.prev_layout()),
    Key([mod], "w", lazy.window.kill()),

    #Control-commands
    Key([mod, "shift"], "space", lazy.layout.rotate()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod,"control"],"Escape",lazy.spawn("systemctl poweroff")),
    Key([mod,"control"],"s",lazy.spawn("systemctl suspend")),

    #Monitor commands: 
    Key([mod], "0", lazy.next_screen() ),
    Key([mod], "apostrophe",switch_screens() ),

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


