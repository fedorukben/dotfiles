import subprocess
import os

from typing import List

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.utils import logger


###############################################################################################################################################
#############  HOOKS  #########################################################################################################################
###############################################################################################################################################

@hook.subscribe.client_new
def client_new(client):
    logger.warning(client)
    if client.name == 'Discord':
        client.togroup('chat')
    elif client.name == 'urxvt':
        client.togroup('dev')
    elif client.name == f'{emacs}@{machine_name}':
        client.togroup('dev')
    elif client.name == f'{todo_application}':
        client.togroup('todo')
    elif client.name == 'Inkscape':
        client.togroup('draw')

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.qtile/hooks/autostart.sh'])


###############################################################################################################################################
#############  ENVIRONMENT VARIABLES  #########################################################################################################
###############################################################################################################################################

machine_name = "benmanjaro"
mod = "mod4"
terminal = "urxvt"
browser = "qutebrowser"
editor = "vim"
run_launcher = "dmenu_run -c -hp brave,pcmanfm"
clipboard_manager = "copyq toggle"
screenshot_all = "main /tmp/recent-screenshot.png"
screenshot_sel = "maim -s /tmp/recent-screenshot.png"
screenshot_copy = "xclip -sel clip -t image/png -i /tmp/recent-screenshot.png"
default_layout = "monadtall"
emacs = "emacs"
todo_application = "Todoist"


###############################################################################################################################################
#############  KEYS  ##########################################################################################################################
###############################################################################################################################################

keys = [
    Key([mod],                  "h",               lazy.layout.left(),                          desc="Move focus to left"),
    Key([mod],                  "l",               lazy.layout.right(),                         desc="Move focus to right"),
    Key([mod],                  "j",               lazy.layout.down(),                          desc="Move focus down"),
    Key([mod],                  "k",               lazy.layout.up(),                            desc="Move focus up"),
    Key([mod, "shift"],         "space",           lazy.layout.next(),                          desc="Move window focus to other window"),
    Key([mod, "shift"],         "l",               lazy.layout.shiuffle_right(),                desc="Move window to the right"),
    Key([mod, "shift"],         "j",               lazy.layout.shuffle_down(),                  desc="Move window down"),
    Key([mod, "shift"],         "k",               lazy.layout.shuffle_up(),                    desc="Move window up"),
    Key([mod, "control"],       "h",               lazy.layout.grow_left(),                     desc="Grow window to the left"),
    Key([mod, "control"],       "l",               lazy.layout.grow_right(),                    desc="Grow window to the right"),
    Key([mod, "control"],       "j",               lazy.layout.grow_down(),                     desc="Grow window down"),
    Key([mod, "control"],       "k",               lazy.layout.grow_up(),                       desc="Grow window up"),
    Key([mod],                  "n",               lazy.layout.normalize(),                     desc="Reset all window sizes"),
    Key([mod, "shift"],         "space",           lazy.layout.toggle_split(),                  desc="Toggle between split and unsplit sides of stack"),
    Key([mod],                  "Return",          lazy.spawn(terminal),                        desc="Launch terminal"),
    Key([mod],                  "b",               lazy.spawn(browser),                         desc="Launch browser"),
    Key([mod],                  "space",           lazy.spawn(emacs),                           desc="Launch doom emacs"),
    Key([mod],                  "Tab",             lazy.next_layout(),                          desc="Toggle between layouts"),
    Key([mod],                  "p",               lazy.spawn(run_launcher),                    desc="Launch the run launcher"),
    Key([mod],                  "c",               lazy.window.kill(),                          desc="Kill focused window"),
    Key([mod],                  "q",               lazy.restart(),                              desc="Restart Qtile"),
    Key([mod, "shift"],         "q",               lazy.shutdown(),                             desc="Shutdown Qtile"),
    Key([mod],                  "w",               lazy.to_screen(1),                           desc="Move keyboard focus to monitor 2"),
    Key([mod],                  "e",               lazy.to_screen(0),                           desc="Move keyboard focus to monitor 1"),
    Key([mod],                  "r",               lazy.to_screen(2),                           desc="Move keyboard focus to monitor 3"),
    Key([mod],                  "period",          lazy.next_screen(),                          desc="Move keyboard focus to next monitor"),
    Key([mod],                  "comma",           lazy.prev_screen(),                          desc="Move keyboard focus to previous monitor"),
    Key([mod],                  "f",               lazy.window.toggle_fullscreen(),             desc="Toggle fullscreen"),
    Key([mod, "shift"],         "f",               lazy.window.toggle_floating(),               desc="Toggle floating"),
    Key([mod, "shift"],         "c",               lazy.spawn(clipboard_manager),               desc="Start clipboard manager"),
    Key([mod],                  "Print",           lazy.spawn(screenshot_sel),                  desc="Screenshot by selection"),
    Key([mod, "shift"],         "Print",           lazy.spawn(screenshot_all),                  desc="Screenshot all windows"),
    Key([mod, "control"],       "Print",           lazy.spawn(screenshot_copy),                 desc="Copy last screenshot to clipboard"),
    Key([mod],                  "t",               lazy.spawn('pkill picom'),                   desc="Kill picom"),
    Key([mod, "shift"],         "t",               lazy.spawn('picom'),                         desc="Spawn a new instance of picom"),
]

group_names = [
        ('www',       {'layout': default_layout}),
        ('dev',       {'layout': default_layout}),
        ('todo',      {'layout': default_layout}),
        ('chat',      {'layout': default_layout}),
        ('draw',      {'layout': default_layout}),
        ('bin',       {'layout': default_layout})
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

layouts = [
    layout.MonadTall(
        font = "Source Code Pro",
        fontsize = 10,
        margin = 8
    ),
    layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar([
            widget.CurrentLayout(),
            widget.GroupBox(),
            widget.Prompt(),
            widget.WindowName(),
            widget.Chord(
                chords_colors={
                    'launch': ("#ff0000", "#ffffff"),
                },
                name_transform=lambda name: name.upper(),
            ),
            widget.Clipboard(),
            widget.Volume(),
            widget.BatteryIcon(),
            widget.QuickExit(),
            widget.Net(
                interface = "enp6s0",
                format = "{down} ↓↑ {up}",
            ),
            widget.Systray(),
            widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
        ], 24),
    ),
    Screen(
        bottom=bar.Bar([
            widget.GroupBox(),
            widget.WindowName(),
            widget.Spacer(
                length = bar.STRETCH
            ),
        ], 24),
    )
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "LG3D"
