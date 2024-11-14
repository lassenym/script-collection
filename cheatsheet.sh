#!/bin/bash

# Define color variables
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
RESET='\033[0m'

# Define an array to hold the cheatsheet entries
entries=(
    "sudo pacman -Rnsc <pkg> -> Uninstall"
    "pacman -Qe -> List explicitly-installed packages"
    "pacman -Qs <query> -> Search installed packages for keywords"
    "pacman -Qm -> List non-main-repo packages"
    "autorem -> Remove unused packages"
    "ücache -> Clear yay & pacman cache"
    "üp -> Update .bashrc"
    "üü -> Show cheatsheet"
    "üwe -> Show weather"
    "yt <video link> -> Play video on VLC"
    "ää -> Show program list"
    "äwe -> Prints white"
    "übash -> cd into bash directory"
    "ürem -> Cleanly remove package"
    "hm -> Show potential package updates"
    "ph (l, p, s, d) -> Use pacman-helper"
)

# Create the alias with colored output
echo -e "${MAGENTA}#########################################################################${RESET}"

for entry in "${entries[@]}"; do
    cmd="${entry%%->*}"
    desc="${entry##*->}"

    # Calculate the required padding for command column
    padding=$(( 25 - ${#cmd} ))
    padding_spaces=$(printf '%*s' $padding)

    printf "${WHITE}|${RESET}${CYAN} %s${RESET}${YELLOW}->${RESET} ${GREEN}%-41s${RESET}${WHITE}|\n" "$cmd$padding_spaces" "$desc"
    (( count++ ))
    if [ $count -eq 4 ]; then
        echo -e "${WHITE}------------------------------------------------------------------------${RESET}"
    fi

done

echo -e "${MAGENTA}#########################################################################${RESET}"
