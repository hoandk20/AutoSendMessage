import pyautogui
import time
import threading
import keyboard
import ctypes
import os
import pyperclip

def is_running_as_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

if not is_running_as_admin():
    raise OSError("This script must be run as administrator")

running = False

def toggle_sending():
    global running
    running = not running
    if running:
        print("Started sending messages...")
    else:
        print("Stopped sending messages...")

def read_text_from_file(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("File not found.")
        return None

file_path = 'C:/Users/k/OneDrive/Desktop/Code/AutoMessage/Text.txt'  # Change this to your file path
message = read_text_from_file(file_path, encoding='utf-8')

def send_message():
    global running
    while True:
        if running:
            pyperclip.copy(message)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
        time.sleep(0.5)

# Set up the hotkey listener
keyboard.add_hotkey('x', toggle_sending)

# Start the message sending loop in a separate thread
thread = threading.Thread(target=send_message)
thread.daemon = True
thread.start()

# Keep the script running
keyboard.wait('esc')