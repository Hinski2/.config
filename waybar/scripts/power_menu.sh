#!/bin/bash

selection=$(yad --center --width=200 --height=200 --title="Power Menu" \
    --list --column=Action \
    " Power Off" \
    "🔁 Reboot" \
    "🌙 Suspend" \
    "❄️ Hibernate")

case "$selection" in
    *"Power Off"*) systemctl poweroff ;;
    *"Reboot"*) systemctl reboot ;;
    *"Suspend"*) systemctl suspend ;;
    *"Hibernate"*) systemctl hibernate ;;
esac


