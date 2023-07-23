#### A ##########################################################

# Sends a sample notification
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'


##### B ##########################################################

alias bd=". bd -si"


##### C ##########################################################

# Clear
alias c="clear"
# Exports my calendar whenever I finish editing
alias calcurse="calcurse -D /home/benfedoruk/.calcurse && calcurse -D /home/benfedoruk/.calcurse --export > /home/benfedoruk/Code/html/personalwebsite/cal.ics"
# Safe overwrite for cp
alias cp="cp -i"


##### D ##########################################################

# Access dotfiles.
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'


##### G ##########################################################

# Generate a new random 20-digit password
alias genpass="openssl rand -base64 20"


##### I ##########################################################

# Get external IP address
alias ipe="curl ipinfo.io/ip; echo \n"
# Get internal IP address
alias ipi="ipconfig getifaddr en0"


##### J ##########################################################

# Simple alias for J console
alias j="j9 -c"


##### L ##########################################################

# List
alias l="ls -CF"
# List all
alias la="ls -A"
# Perform a long list (list all, with permissions)
alias ll="ls -alF"
# List by file size
alias lt="ls --human-readable --size -1 -S --classify"
# List all by file size
alias lta="ls -A --human-readable --size -1 -S --classify"


##### M ##########################################################

# Allows easy parent mkdirs
alias mkdir="mkdir -pv"
# Better mount, no virtual drives
alias mnt="mount | awk -F' ' '{ printf \"%s\t%s\n\",\$1,\$3; }' | column -t | egrep ^/dev/ | sort"
# Directs mutt to neomutt
alias mutt="neomutt"
# Safe overwrite for mv
alias mv="mv -i"


##### S ##########################################################

# Run a speed test
alias speed="speedtest-cli --server 2406 --simple"


##### U ##########################################################

# Unpacking a .tar file
alias untar="tar -zxvf"


##### W ##########################################################

# Allows you to resume on an error
alias wget="wget -c"


##### X ##########################################################

# Updates .Xresources
alias xup="xrdb ~/.Xresources"
