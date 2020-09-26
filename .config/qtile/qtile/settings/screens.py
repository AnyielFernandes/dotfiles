import subprocess
from libqtile.config import Screen
from libqtile import bar
from settings.widgets import main_widgets, secondary_widgets

status_bar = lambda widgets: bar.Bar(widgets,22,opacity = 1)

screens = [Screen(top=status_bar(main_widgets))]

connected_monitors = subprocess.run(
        "xrandr | grep 'connected' | cut -d ' ' -f2",
        shell=True,
        stdout=subprocess.PIPE
        ).stdout.decode("UTF-8").split("\n")[:-1].count("connected")

if connected_monitors > 0:
    for i in range(connected_monitors - 1):
        screens.append(Screen(top=status_bar(secondary_widgets)))
