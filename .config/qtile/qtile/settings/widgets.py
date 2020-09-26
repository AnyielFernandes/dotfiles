from libqtile import widget

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
    font="Fira Code",
    fontsize = 12,
    padding = 2,
    background=colors[0]
)

extension_defaults = widget_defaults.copy()

base = lambda fg, bg : {
        'foreground': fg,
        'background': bg
        }

icon = lambda fg, bg, fontsize = 12, text="?", padding=0: widget.TextBox(
            **base(fg,bg),
            fontsize=fontsize,
            text=text,
            padding=padding
        )

powerline = lambda fg, bg, : widget.TextBox(
            **base(fg,bg),
            text = '',
            padding = -1,
            fontsize = 50
        )

workspaces = lambda: [
                widget.Sep(
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
                widget.WindowName( **base(colors[6],colors[0]), padding = 0, show_state = False ),
        ]

main_widgets = [
        *workspaces(), 
        powerline(colors[4],colors[0]), 
        widget.CurrentLayoutIcon(
            scale = 0.7, 
            **base(colors[2],colors[4]), 
            ),
        powerline(colors[5],colors[4]), 
        widget.TextBox(
            text = "  ",
            padding = 0,
            fontsize = 15, 
            mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('nm-connection-editor')},
            **base(colors[2],colors[5])
            ),
        powerline(colors[4],colors[5]), 
        widget.TextBox(
            text = "  ",
            padding = 2,
            fontsize = 15, 
            mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('blueman-adapters')},
            **base(colors[2],colors[4])
        ),
        powerline(colors[5],colors[4]), 
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
            **base(colors[2],colors[5])
        ),
        powerline(colors[4],colors[5]), 
        icon(colors[2],colors[4],14," "),
        widget.Volume(
            padding = 5, 
            fontsize = 14,
            **base(colors[2],colors[4])
        ),
        powerline(colors[5],colors[4]),
        widget.TextBox(
            text = " ",
            padding = 2,
            fontsize = 14, 
            **base(colors[2],colors[5])
        ),
        widget.Pacman(
            update_interval = 1800,
            font = "Ubuntu Bold",
            **base(colors[2],colors[5])
        ),
        widget.TextBox(
            text = "Updates",
            padding = 5,
            font = "Ubuntu Bold",
            **base(colors[2],colors[5])
        ),
        powerline(colors[4],colors[5]), 
        widget.Clock(
            format = " %A, %B %d  %H:%M ", 
            font = "Ubuntu Bold",
            **base(colors[2],colors[4])
        ),
        powerline(colors[0],colors[4]), 
        widget.Systray(
            padding = 5,
            **base(colors[2],colors[0])
        ),
        widget.Sep(
            linewidth = 0,
            padding = 6, 
            **base(colors[2],colors[0])
        )
    ]

secondary_widgets = [
        *workspaces(), 
        powerline(colors[4],colors[0]), 
        widget.CurrentLayoutIcon(
            scale = 0.7, 
            **base(colors[2],colors[4]), 
            ),
        powerline(colors[5],colors[4]), 
        widget.TextBox(
            text = "  ",
            padding = 0,
            fontsize = 15, 
            mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('nm-connection-editor')},
            **base(colors[2],colors[5])
            ),
        powerline(colors[4],colors[5]), 
        widget.TextBox(
            text = "  ",
            padding = 2,
            fontsize = 15, 
            mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('blueman-adapters')},
            **base(colors[2],colors[4])
        ),
        powerline(colors[5],colors[4]), 
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
            **base(colors[2],colors[5])
        ),
        powerline(colors[4],colors[5]), 
        icon(colors[2],colors[4],14," "),
        widget.Volume(
            padding = 5, 
            fontsize = 14,
            **base(colors[2],colors[4])
        ),
        powerline(colors[5],colors[4]),
        widget.TextBox(
            text = " ",
            padding = 2,
            fontsize = 14, 
            **base(colors[2],colors[5])
        ),
        widget.Pacman(
            update_interval = 1800,
            font = "Ubuntu Bold",
            **base(colors[2],colors[5])
        ),
        widget.TextBox(
            text = "Updates",
            padding = 5,
            font = "Ubuntu Bold",
            **base(colors[2],colors[5])
        ),
        powerline(colors[4],colors[5]), 
        widget.Clock(
            format = " %A, %B %d  %H:%M ", 
            font = "Ubuntu Bold",
            **base(colors[2],colors[4])
        ),
        powerline(colors[0],colors[4]), 
        widget.Systray(
            padding = 5,
            **base(colors[2],colors[0])
        ),
        widget.Sep(
            linewidth = 0,
            padding = 6, 
            **base(colors[2],colors[0])
        )
    ]



