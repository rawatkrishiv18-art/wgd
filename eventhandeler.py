from thinker import *
window = Tk()
window.title("event handler")
window.geometry("1000x1000")
def handle_keypress(event):
    """print the character associated with the key pressed"""
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nthe button was clicked!")

button = Button(window, text="Click me")
button.pack()
button.bind("<Button-1>", handle_click)

window.mainloop()