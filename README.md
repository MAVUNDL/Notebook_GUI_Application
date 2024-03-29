---

# Notebook Application

This is a simple GUI application built with Python's `ttkbootstrap` library. It provides a basic notepad-like interface where you can write and save your notes.

## Features

- User-friendly interface
- Ability to write and save notes
- Notes are appended to the existing notes, not overwritten

## How to Run the Application

1. Ensure that Python is installed on your machine.
2. Install the `ttkbootstrap` library if you haven't already. You can do this by running `pip install ttkbootstrap` in your terminal.
3. Download the Python script for the application.
4. Open a terminal window and navigate to the directory where the script is located.
5. Run the command `python filename.py`, replacing "filename" with the name of the Python script.

## How to Use the Application

1. Write your notes in the text box.
2. Click the "Save text" button to save your notes. The notes will be appended to the existing notes in a file named `Notes.txt`.

## Code Overview

Here's a brief overview of the code:

```python
import ttkbootstrap as ttk

# creating a window
window = ttk.Window()
window.title("Notebook")

# creating a label
label = ttk.Label(text='Welcome to your Notebook', font='Calibri 15 bold')
label.pack()

# creating a frame
frame = ttk.Frame(master=window)
frame.pack()

# creating a text box
text_box = ttk.Text(master=frame, width=100, height=15, font='Calibri 10 bold')
text_box.pack(pady=10)

# creating a button
def save_text():
    with open('Notes.txt', 'a') as file:
        file.write("\n~~~~~~~~~~~~~~~~~~~~~~ Saved text ~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        file.write(text_box.get('1.0', ttk.END))
        file.write("~~~~~~~~~~~~~~~~~~~~~~ End of Text ~~~~~~~~~~~~~~~~~~~~~~~~")

button = ttk.Button(master=window, text='Save text', command=save_text)
button.pack(pady=5)

# Creating a main loop
window.mainloop()
```

---
