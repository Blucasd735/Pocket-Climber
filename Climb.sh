#!/bin/bash

XDG_DATA_HOME=${XDG_DATA_HOME:-$HOME/.local/share}

if [ -d "/opt/system/Tools/PortMaster/" ]; then
  controlfolder="/opt/system/Tools/PortMaster"
elif [ -d "/opt/tools/PortMaster/" ]; then
  controlfolder="/opt/tools/PortMaster"
elif [ -d "$XDG_DATA_HOME/PortMaster/" ]; then
  controlfolder="$XDG_DATA_HOME/PortMaster"
else
  controlfolder="/roms/ports/PortMaster"
fi

export controlfolder

source "$controlfolder/control.txt"

 # If using a 32 bit port
[ -f "${controlfolder}/mod_${CFW_NAME}.txt" ] && source "${controlfolder}/mod_${CFW_NAME}.txt"

get_controls

GAMEDIR="/$directory/ports/climb_amy"

cd "$GAMEDIR" || exit 1
> "$GAMEDIR/log.txt" && exec > >(tee "$GAMEDIR/log.txt") 2>&1

export LD_LIBRARY_PATH="$GAMEDIR/lib:$GAMEDIR/lib/arm64-v8a:$LD_LIBRARY_PATH"
export SDL_GAMECONTROLLERCONFIG="$sdl_controllerconfig"
chmod +x "$GAMEDIR/gmloadernext.aarch64"

# GMLOADER_NXEXTRACT_BEGIN
chmod +x "$GAMEDIR/run-extractor.sh" "$GAMEDIR/nxextract.py" \
  "$GAMEDIR/nxextract-ui" "$GAMEDIR/tools/prepare_gmloader_runtime.py" \
  "$GAMEDIR/tools/source_guard.py" 2>/dev/null || true
if ! "$GAMEDIR/run-extractor.sh"; then
  printf 'ERRO: falha ao preparar APK/XAPK em gamedata. Veja nxextract.log.\n' \
    > "${CUR_TTY:-/dev/tty0}" 2>/dev/null || true
  sleep 6
  pm_finish 2>/dev/null || true
  exit 1
fi
# GMLOADER_NXEXTRACT_END

$GPTOKEYB "gmloadernext.aarch64" &
pm_platform_helper "gmloadernext.aarch64"
"$GAMEDIR/gmloadernext.aarch64" -c "$GAMEDIR/gmloader.json"

pm_finish