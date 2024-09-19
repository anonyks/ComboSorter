import os
import time
from tkinter import filedialog as fd
from colorama import Fore, Back, Style, init

# Initialize colorama for colorized terminal output
init(autoreset=True)

# Color and style setup for terminal output
COLORS = {
    "black": Fore.BLACK,
    "white": Fore.WHITE,
    "yellow": Fore.YELLOW,
    "red": Fore.RED,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "cyan": Fore.CYAN,
    "white_bg": Back.WHITE,
    "yellow_bg": Back.YELLOW,
    "red_bg": Back.RED,
    "green_bg": Back.GREEN,
    "reset": Fore.RESET
}

def print_banner():
    """Prints the application banner."""
    banner = f"""
    {COLORS['green']}▄███▄   █▀▄▀█ ██   ▄█ █           ▄▄▄▄▄   ████▄ █▄▄▄▄    ▄▄▄▄▀ ▄███▄   █▄▄▄▄
    █▀   ▀  █ █ █ █ █  ██ █          █     ▀▄ █   █ █  ▄▀ ▀▀▀ █    █▀   ▀  █  ▄▀
    ██▄▄    █ ▄ █ █▄▄█ ██ █        ▄  ▀▀▀▀▄   █   █ █▀▀▌      █    ██▄▄    █▀▀▌
    █▄   ▄▀ █   █ █  █ ▐█ ███▄      ▀▄▄▄▄▀    ▀████ █  █     █     █▄   ▄▀ █  █
    ▀███▀      █     █  ▐     ▀                        █     ▀      ▀███▀     █
             ▀     █                                 ▀                      ▀
                  ▀
    {COLORS['yellow']} Coder: {COLORS['cyan']}@AnonyKs_xD
    {COLORS['yellow']} Telegram Channel: {COLORS['cyan']}https://t.me/@AnonyKs_xD
    """
    print(banner)

def email_sorter():
    """Opens a file dialog to select an email list and sorts the emails by domain."""
    email_file_path = fd.askopenfilename(title="Select your email list file")
    if not email_file_path:
        print(f"{COLORS['red']}No file selected. Exiting...")
        return

    try:
        with open(email_file_path, 'r', encoding="utf-8", errors="ignore") as file:
            sorted_emails = {}
            for count, line in enumerate(file, start=1):
                try:
                    user, domain = line.strip().split('@')
                    if domain not in sorted_emails:
                        sorted_emails[domain] = []
                    sorted_emails[domain].append(line)
                except ValueError:
                    print(f"{COLORS['red']}Invalid line at {count}: {line.strip()}")
                    continue

        # Writing sorted emails to files
        for domain, emails in sorted_emails.items():
            domain_file = f"sorted/{domain}.txt"
            os.makedirs(os.path.dirname(domain_file), exist_ok=True)
            with open(domain_file, 'w', encoding="utf-8") as file:
                file.writelines(emails)
            print(f"{COLORS['green']}Saved {len(emails)} emails under domain {domain} to {domain_file}")

    except Exception as e:
        print(f"{COLORS['red']}An error occurred: {e}")

if __name__ == "__main__":
    print_banner()
    email_sorter()
