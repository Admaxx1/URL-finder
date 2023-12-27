import webbrowser as wb
import tkinter as tk
import pyautogui
import time as t

def submit():
    wb.open(entry.get())

def clear():
    entry.delete(0, tk.END)

def new_tab():
    def new_tab_search():
        wb.open_new_tab(entry_tab.get())

    def close():
        entry_tab.pack_forget()
        submit_button_tab.pack_forget()
        close_button.pack_forget()

    entry_tab = tk.Entry(width=50, font=20)
    entry_tab.pack()
    entry_tab.insert(True,'https://')
    submit_button_tab = tk.Button(win, text='SUBMIT', font=('Arial', 20, 'bold'), command=new_tab_search)
    submit_button_tab.pack()
    close_button = tk.Button(win, text='close', font=('Arial', 15, 'bold'), command=close)
    close_button.pack()
    

def perform_pyautogui_actions():
    print('Hello')
    print(pyautogui.position())
    pyautogui.moveTo(108, 90, 1)
    pyautogui.tripleClick()
    pyautogui.press('backspace')
    pyautogui.write("https>&&www.")

def chatGPTcmd():
    wb.open('https://chat.openai.com')

win = tk.Tk()
win.title('URL shortcut')
win.geometry('400x400')
win.resizable(False, False)

entry = tk.Entry(width=50, font=20)
entry.pack()

entry.insert(True, '# type in your URL here')

submit_button = tk.Button(win, text='SUBMIT', font=('Arial', 20, 'bold'), command=submit)
submit_button.pack()
clear_button = tk.Button(win, text='CLEAR', font=('Arial', 20, 'bold'), command=clear)
clear_button.pack()
open_new_tab = tk.Button(win, text='New tab', font=('Arial', 20, 'bold'), command=new_tab)
open_new_tab.pack()
chatGPT = tk.Button(win, text='chatGPT', font=('Arial', 20, 'bold'), command=chatGPTcmd)
chatGPT.pack()

# Schedule the PyAutoGUI actions to be executed after 3000 milliseconds (3 seconds)
win.after(1000, perform_pyautogui_actions)

win.mainloop()
