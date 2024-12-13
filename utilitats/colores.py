"""
Definició de les constants de colors
"""
__all__ = ['C_NONE','C_BLK','C_RED','C_GRN','C_YLW','C_BLU','C_MAG','C_CYN','C_WHT','CB_BLK','CB_RED','CB_GRN','CB_YLW','CB_BLU','CB_MAG','CB_CYN','CB_WHT','BG_BLK','BG_RED','BG_GRN','BG_YLW','BG_BLU','BG_MAG','BG_CYN','BG_WHT']

C_NONE="\033[0m"    # unsets color to term's fg color

# regular colors
C_BLK="\033[0;30m"    # black
C_RED="\033[0;31m"    # red
C_GRN="\033[0;32m"    # green
C_YLW="\033[0;33m"    # yellow
C_BLU="\033[0;34m"    # blue
C_MAG="\033[0;35m"    # magenta
C_CYN="\033[0;36m"    # cyan
C_WHT="\033[0;37m"    # white

# emphasized (bolded) colors
CB_BLK="\033[1;30m"
CB_RED="\033[1;31m"
CB_GRN="\033[1;32m"
CB_YLW="\033[1;33m"
CB_BLU="\033[1;34m"
CB_MAG="\033[1;35m"
CB_CYN="\033[1;36m"
CB_WHT="\033[1;37m"

# background colors
BG_BLK="\033[40m"
BG_RED="\033[41m"
BG_GRN="\033[42m"
BG_YLW="\033[43m"
BG_BLU="\033[44m"
BG_MAG="\033[45m"
BG_CYN="\033[46m"
BG_WHT="\033[47m"
