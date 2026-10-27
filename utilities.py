import os


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def print_header(title):
    border = "=" * 50

    print(border)
    print(title.center(50))
    print(border)


def pause():
    input("\nPress Enter to continue...")
