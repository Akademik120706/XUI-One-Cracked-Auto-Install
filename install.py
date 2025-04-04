#!/usr/bin/env python3
# Script By: Akademik11

# Auto-install colorama if not present
try:
    from colorama import init, Fore, Style
except ImportError:
    import subprocess
    import sys
    print("Colorama not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import init, Fore, Style

import subprocess
import os
import time

init(autoreset=True)

def print_banner(color, message):
    line = "─" * (len(message) + 4)
    print(f"{color} ┌{line}┐")
    print(f"{color} │  {message}  │")
    print(f"{color} └{line}┘")

def run_command(command, cwd=None):
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd)
    except subprocess.CalledProcessError:
        print(Fore.RED + f"[Error] Command failed: {command}")
        exit(1)

def main():
    os.system('clear')

    print_banner(Fore.YELLOW, "Preparing System to Install XUI.One")
    time.sleep(3)

    print_banner(Fore.RED, "Do you want to continue?")

    while True:
        choice = input(Fore.GREEN + "[1] Yes\n[2] No\nChoose an option: ")
        if choice == "1":
            print(Fore.YELLOW + "You selected Yes... Installing XUI.One now...")
            break
        elif choice == "2":
            print(Fore.RED + "Installation cancelled.")
            exit()
        else:
            print(Fore.RED + "Invalid input. Please try again.")

    time.sleep(4)

    run_command("apt-get install -y unzip")

    os.chdir("/tmp")
    print_banner(Fore.YELLOW, "Downloading XUI.One Files")
    run_command("wget https://infinity-panel.pro/panels/xuione/xuifull.zip")
    run_command("unzip -o xuifull.zip")
    time.sleep(3)
    run_command("unzip -o XUI.One-crack")
    time.sleep(3)
    run_command("unzip -o XUI_1.5.12")
    run_command("chmod +x install")

    print_banner(Fore.YELLOW, "Starting XUI.One Official Installer")
    time.sleep(2)
    run_command("./install")

    print_banner(Fore.RED, "Applying XUI.One Crack")
    run_command("chmod -R 777 xui-crack")
    os.chdir("xui-crack")
    run_command("chmod +x install.sh")
    run_command("./install.sh")

    print_banner(Fore.YELLOW, "Process Completed. Exporting Info...")
    time.sleep(2)
    run_command("systemctl enable xuione")

    print_banner(Fore.RED, "Please Save MySQL Credentials")
    print()
    run_command("tail -n 4 credentials.txt", cwd="/tmp")

    time.sleep(4)
    print_banner(Fore.RED, "XUI Status Information")
    run_command("./status", cwd="/home/xui")

if __name__ == "__main__":
    main()
