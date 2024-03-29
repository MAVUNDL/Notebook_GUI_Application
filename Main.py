import ttkbootstrap as ttk

# creating a window
window = ttk.Window()
# crating the title
window.title("Notebook")
# creating a label
label = ttk.Label(
    text='Welcome to your Notebook',
    font='Calibri 15 bold'
)
label.pack()
# creating a frame
frame = ttk.Frame(
    master=window
)
frame.pack()
# creating a text box
text_box = ttk.Text(
    master=frame,
    width=100,
    height=15,
    font='Calibri 10 bold'
)
text_box.pack(pady=10)


# creating a button
def save_text():
    with open('Notes.txt', 'w') as file:
        file.write(text_box.get('1.0', ttk.END))


button = ttk.Button(
    master=window,
    text='Save text',
    command=save_text,
)
button.pack(pady=5)
# Creating a main loop
window.mainloop()
