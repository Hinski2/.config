#!/usr/bin/env python3
import sys
import os
import subprocess
from enum import Enum


class Mode(Enum):
    NVIDIA = "nvidia"
    INTEL = "intel"

CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(CONFIG_DIR, "hyprland.conf")

# ── Per-mode sections ─────────────────────────────────────────────────────────

MONITORS = {
    Mode.NVIDIA: """\
# laptop monitor
monitor=eDP-1,1920x1080@165,3840x1300,1.0

# main monitor
# monitor=HDMI-A-1,preferred,-1080x-2350,1,transform,1 # pivot
monitor=HDMI-A-1,3840x2160@60,0x0,1.0
""",
    Mode.INTEL: """\
# laptop monitor
monitor=eDP-2,1920x1080@165,auto,1

# projector
monitor=HDMI-A-1,preferred,auto,1
""",
}

ENVS = {
    Mode.NVIDIA: """\
env = XDG_CURRENT_DESKTOP,Hyprland
env = XCURSOR_SIZE,24

# for nvidia
env = WLR_DRM_DEVICES,/dev/dri/card0:/dev/dri/card1   # 1) RTX jako primary, 2) Intel
env = LIBVA_DRIVER_NAME,nvidia
env = __GLX_VENDOR_LIBRARY_NAME,nvidia
env = GBM_BACKEND,nvidia-drm
env = WLR_RENDERER_ALLOW_SOFTWARE,0
# env = WLR_NO_HARDWARE_CURSORS,1
""",
    Mode.INTEL: """\
env = XDG_CURRENT_DESKTOP,Hyprland

#for intel
env = LIBVA_DRIVER_NAME,iHD
env = WLR_DRM_DEVICES,/dev/dri/card2
env = WLR_RENDERER_ALLOW_SOFTWARE,0
env = WLR_NO_HARDWARE_CURSORS,1

env = HYPRCURSOR_SIZE,40
env = XCURSOR_SIZE,40
""",
}

CURSOR = {
    Mode.NVIDIA: """\
cursor {
    # no_hardware_cursors = true
}
""",
    Mode.INTEL: """\
cursor {
    no_hardware_cursors = true
}
""",
}

WORKSPACES = {
    Mode.NVIDIA: """\
workspace = 1, monitor:HDMI-A-1, persistent:true
workspace = 2, monitor:eDP-1, persistent:true
workspace = 3, monitor:eDP-1, persistent:true
""",
    Mode.INTEL: """\
workspace = 1, persistent:true
workspace = 2, persistent:true
workspace = 3, persistent:true
""",
}

FOCUS_MONITOR_BINDS = {
    Mode.NVIDIA: "",
    Mode.INTEL: """\
# move cursor between monitors
bind=CTRL_SUPER_ALT, left, focusmonitor, -1
bind=CTRL_SUPER_ALT, right, focusmonitor, +1

""",
}

# ── Common section ────────────────────────────────────────────────────────────

COMMON = """\
exec-once=foot
exec-once=waybar
exec-once=swaybg -m fill -i ~/Pictures/linus.png
exec-once=blueman-applet
exec-once=dunst
exec-once=xdg-desktop-portal-hyprland
exec-once=xdg-desktop-portal
exec-once=/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
exec-once=hypridle

input {
	kb_layout=pl
	follow_mouse=1
    	accel_profile = flat
    	sensitivity = 2.5

	touchpad {
		natural_scroll = true
        	scroll_factor = 0.5
	}
}

general {
    col.active_border = rgba(e9a6ffff) 
    col.inactive_border = rgba(000000cc)
    border_size = 3
    gaps_out = 0
    gaps_in = 0
}

animations {
    enabled = true

    # Default animations, see https://wiki.hyprland.org/Configuring/Animations/ for more

    animation = windows, 1, 3, default, popin
    animation = layers, 1, 3, default, slide
    animation = fade, 0, 3, default
    animation = border, 1, 3, default 
    animation = workspaces, 1, 3, default, slide 
}

opengl {
    nvidia_anti_flicker = false
}

decoration {
    rounding = 0

    # Change transparency of focused and unfocused windows
    active_opacity = 1 
    inactive_opacity = 1

    shadow {
        enabled = false
        range = 4
        render_power = 3
        color = rgba(1a1a1aee)
	}

	blur {
        enabled = true
        size = 3
        passes = 1
        vibrancy = 0.1696
    }
}

bind=SUPER,Return,exec,foot
bind=Super,space,exec,wofi --show drun
bind=SUPER,W,killactive,
bind=SUPER,M,exit,
bind=ctrl,F12,exec,guake
bind=SUPER,l,exec,hyprlock

# moving focus
bind=SUPER, left,  movefocus, l
bind=SUPER, right, movefocus, r
bind=SUPER, up,    movefocus, u
bind=SUPER, down,  movefocus, d

bind=Super, H, movefocus, l
bind=Super, L, movefocus, r
bind=Super, K, movefocus, u
bind=Super, J, movefocus, D

# move windows
bind=SUPER_SHIFT,left,movewindow,l
bind=SUPER_SHIFT,right,movewindow,r
bind=SUPER_SHIFT,up,movewindow,u
bind=SUPER_SHIFT,down,movewindow,d

bind=SUPER_SHIFT,H,movewindow,l
bind=SUPER_SHIFT,L,movewindow,r
bind=SUPER_SHIFT,K,movewindow,u
bind=SUPER_SHIFT,J,movewindow,d

# mouse + resizing / swappint windows
bindm = $SUPER, mouse:272, movewindow
bindm = $SUPER, mouse:273, resizewindow

# move windows between monitors
bind=CTRL_SUPER_ALT,left,movewindow,mon:-1
bind=CTRL_SUPER_ALT,right,movewindow,mon:+1
bind=CTRL_SUPER_ALT,h,movewindow,mon:-1
bind=CTRL_SUPER_ALT,l,movewindow,mon:+1

# ss
bind=,Print,exec,grim -g "$(slurp)" /tmp/screenshot_$(date +%s).png && mv /tmp/screenshot_*.png ~/Pictures/
bind=SHIFT,Print,exec,grim -g "$(slurp)" /tmp/swap_ss.png && swappy -f /tmp/swap_ss.png
bind=SUPER_SHIFT,S,exec,sh -c 'grim -g "$(slurp)" /tmp/clip_ss.png && wl-copy < /tmp/clip_ss.png'

# Media keys
bind=,XF86AudioPlay,exec,playerctl play
bind=,XF86AudioPause,exec,playerctl pause
# bind=,XF86AudioStop,exec,playerctl pause
bind=,XF86AudioNext,exec,playerctl next
bind=,XF86AudioPrev,exec,playerctl previous

bind = , XF86AudioRaiseVolume, exec, pactl set-sink-volume @DEFAULT_SINK@ +3%
bind = , XF86AudioLowerVolume, exec, pactl set-sink-volume @DEFAULT_SINK@ -3%
"""

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    valid = {m.value: m for m in Mode}
    if len(sys.argv) != 2 or sys.argv[1] not in valid:
        print(f"Usage: mode.py [{"|".join(valid)}]")
        sys.exit(1)

    mode = valid[sys.argv[1]]

    config = (
        f"# Generated by mode.py — mode: {mode.value}\n\n"
        + MONITORS[mode] + "\n"
        + ENVS[mode] + "\n"
        + COMMON + "\n"
        + CURSOR[mode] + "\n"
        + FOCUS_MONITOR_BINDS[mode]
        + "# workspaces\n"
        + WORKSPACES[mode] + "\n"
        + "bind=CTRL_ALT,LEFT,workspace,e-1\n"
        + "bind=CTRL_ALT,RIGHT,workspace,e+1\n"
        + "\n"
        + "bind=CTRL_ALT,1,workspace,1\n"
        + "bind=CTRL_ALT,2,workspace,2\n"
        + "bind=CTRL_ALT,3,workspace,3\n"
        + "\n"
        + "bind = CTRL_SUPER, left, movetoworkspace, r-1\n"
        + "bind = CTRL_SUPER, right, movetoworkspace, r+1\n"
    )

    with open(OUTPUT, "w") as f:
        f.write(config)

    print(f"Switched Hyprland to {mode.value} config.")

    result = subprocess.run(["hyprctl", "reload"], capture_output=True, text=True)
    if result.returncode == 0:
        print("Hyprland reloaded.")
    else:
        print(f"hyprctl reload failed: {result.stderr.strip()}")

if __name__ == "__main__":
    main()
