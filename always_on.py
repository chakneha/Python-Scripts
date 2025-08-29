import tkinter as tk
import threading
import time
import pyautogui

# Global flag for stopping the loop
running = False

def start_bot():
    global running
    running = True
    status_label.config(text="Bot is running...")
    threading.Thread(target=run_bot, daemon=True).start()

def stop_bot():
    global running
    running = False
    status_label.config(text="Bot stopped.")

def run_bot():
    global running
    while running:
        time.sleep(5)

        # Move mouse in a pattern
        for i in range(50):
            if not running: return
            pyautogui.moveTo(i * 10, 5)
        pyautogui.press('ctrl')

        for i in range(50):
            if not running: return
            pyautogui.moveTo(5, (50 - i) * 10)

        pyautogui.hotkey('alt', 'tab')  # Switch window

        for i in range(2):
            if not running: return
            time.sleep(2)
            pyautogui.hotkey('win', 'd')  # Show Desktop

        for i in range(2):
            if not running: return
            time.sleep(2)
            pyautogui.press('win')  # Open Start Menu

        pyautogui.hotkey('ctrl', 't')
        time.sleep(1)

        pyautogui.write('Microsoft Learn', interval=0.1)
        pyautogui.press('enter')
        time.sleep(3)

        for _ in range(3):
            if not running: return
            pyautogui.scroll(-500)
            time.sleep(1)

        for _ in range(3):
            if not running: return
            pyautogui.scroll(500)
            time.sleep(1)

        pyautogui.hotkey('ctrl', 'w')
        time.sleep(10)

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Always-On")
root.geometry("300x150")

status_label = tk.Label(root, text="Bot not running", fg="red")
status_label.pack(pady=10)

start_btn = tk.Button(root, text="Start Bot", command=start_bot, bg="green", fg="white")
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop Bot", command=stop_bot, bg="red", fg="white")
stop_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(pady=5)

root.mainloop()
