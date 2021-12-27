"""
Clears the terminal
The code was found on
https://askubuntu.com/questions/25077/how-to-really-clear-the-terminal
"""
import os


def clear_screen():
    os.system('printf "\ec"')
