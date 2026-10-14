from colorama import Fore, Style, init
import time
import sys
from playsound import playsound
import threading
import tkinter as tk
from tkinter import messagebox

init(autoreset=True)

def typewriter(text, color=Fore.RESET, delay=0.05):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def countdown(seconds=5):
    print(Fore.LIGHTYELLOW_EX + "\nGet ready for your birthday surprise!")
    for i in range(seconds, 0, -1):
        print(Fore.LIGHTRED_EX + f"{i}...", end='', flush=True)
        time.sleep(1)
        print("\r", end='')
    print(Fore.LIGHTGREEN_EX + "Go!            ")
    time.sleep(0.5)

def confetti_classic():
    confetti_line = Fore.YELLOW + "✨" + Fore.CYAN + "*" + Fore.MAGENTA + "✿" + Fore.GREEN + "❀" + Fore.RED + "*" + Fore.BLUE + "✨"
    for _ in range(3):
        print(confetti_line * 6)
        time.sleep(0.2)

def confetti_stars():
    confetti_line = Fore.YELLOW + "★" + Fore.CYAN + "☆" + Fore.LIGHTWHITE_EX + "✦" + Fore.LIGHTBLUE_EX + "✧" + Fore.LIGHTMAGENTA_EX + "✩"
    for _ in range(3):
        print(confetti_line * 8)
        time.sleep(0.2)

def confetti_hearts():
    confetti_line = Fore.RED + "❤" + Fore.MAGENTA + "❥" + Fore.LIGHTRED_EX + "♥" + Fore.LIGHTMAGENTA_EX + "💕" + Fore.LIGHTYELLOW_EX + "💖"
    for _ in range(3):
        print(confetti_line * 6)
        time.sleep(0.2)

balloons = r'''
     .-"""-.
    / .===. \
    \/ 6 6 \/
    ( \___/ )
 ___ooo__V__ooo___
'''

stars_art = r'''
      *     .     *    .  *   .
   .      ✦   .      ✧   *   .
 *   ✩   .   ☆   .   ★   *
'''

hearts_art = r'''
   ❤   ❥   ♥   💕   💖   ❤
  ♥   💖   ❤   ❥   💕   ♥
'''

def play_song():
    try:
        playsound('happy-birthday-254480.mp3')
    except Exception as e:
        print(Fore.RED + f"Could not play song: {e}")

def show_popup(name):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Happy Birthday!", f"🎉🎂 Happy Birthday dear {name}! 🎂🎉\nWishing you a fantastic year ahead! 🥳")
    root.destroy()

def happy_birthday(name, theme):
    # Play song in a separate thread so it doesn't block
    threading.Thread(target=play_song, daemon=True).start()
    if theme == 'classic':
        confetti_classic()
        print(Fore.LIGHTBLUE_EX + balloons)
    elif theme == 'stars':
        confetti_stars()
        print(Fore.LIGHTWHITE_EX + stars_art)
    elif theme == 'hearts':
        confetti_hearts()
        print(Fore.LIGHTMAGENTA_EX + hearts_art)
    else:
        confetti_classic()
        print(Fore.LIGHTBLUE_EX + balloons)
    typewriter(f"🎉🎂 Happy Birthday dear {name}! 🎂🎉", Fore.YELLOW, 0.08)
    typewriter("Wishing you a fantastic year ahead! 🥳", Fore.CYAN, 0.06)
    if theme == 'classic':
        confetti_classic()
    elif theme == 'stars':
        confetti_stars()
    elif theme == 'hearts':
        confetti_hearts()
    else:
        confetti_classic()
    # Show GUI popup
    show_popup(name)

# --- Theme selection and countdown ---
theme = 'hearts'  # Set the theme here: 'classic', 'stars', or 'hearts'
countdown(5)
happy_birthday("Siya", theme) 