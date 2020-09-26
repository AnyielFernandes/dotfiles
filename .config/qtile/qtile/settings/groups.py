from libqtile.config import Key, Group
from libqtile.command import lazy
from settings.keys import mod, keys

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

