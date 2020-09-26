from libqtile import layout

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
    # layout.Bsp(),
    # layout.Columns(),
    # layout.MonadWide(**layout_conf),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.Zoomy(),
]

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
