#!/bin/sh
xrandr --auto --output HDMI-A-1-1 --mode 1920x1080 --right-of HDMI-A-0 &
nitrogen --set-zoom-fill --random ~/Wallpapers --head=0 &
nitrogen --set-zoom-fill --random ~/Wallpapers --head=1 &
picom &
mpv --no-video ~/.qtile/hooks/startup.mp3 &
