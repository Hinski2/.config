#!/bin/bash

status=$(playerctl status 2>/dev/null)
if [ "$status" = "Playing" ] || [ "$status" = "Paused" ]; then
    artist=$(playerctl metadata artist 2>/dev/null)
    title=$(playerctl metadata title 2>/dev/null)
    icon="⏸"
    [ "$status" = "Playing" ] && icon="▶️"

    # JSON dla Waybara (żeby było kolorowo można też dodać "class")
    echo "{\"text\": \"$icon $artist - $title\", \"tooltip\": \"$status\", \"class\": \"$status\"}"
else
    echo "{\"text\": \"⏹\", \"tooltip\": \"No media\", \"class\": \"stopped\"}"
fi
