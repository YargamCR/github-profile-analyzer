import os


def clear_terminal():
    # 'nt' means Windows, otherwise it defaults to Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')
