from tkinter import *
import log
import click
import solution as sol

expression = ''
input_field = ''

def calculator():
    log.logger.debug("function call - calculator")
    global expression
    global input_field

    root = Tk()
    root.geometry('270x320')
    root.resizable(0, 0)
    root.title('Calculator')
    log.logger.info('create: windown - (Calculator)')

    frame_input = Frame(root)
    frame_input.grid(row = 0, column = 0, columnspan = 4, sticky = 'nsew')
    input_field = Entry(frame_input, font = ('Times new roman', 16), width = 24, state = 'readonly')
    input_field.pack(fill = BOTH)

    buttons = (('7', '8', '9', '/'),
               ('4', '5', '6', '*'),
               ('1', '2', '3', '-'),
               ('0', '.', '=', '+'))

    button = Button(root, text = 'C', command=lambda: click.btn_clear())
    button.grid(row = 1, column = 3, sticky="nsew")
    for row in range(4):
        for col in range(4):
            Button(root, width = 2 , height = 3, text=buttons[row][col],
                    command = lambda row = row, col = col: click.btn_click(buttons[row][col])).grid \
                     (row = row + 2, column = col, sticky = "nsew", padx = 5, pady = 5)
    log.logger.info("create: gui and buttons") 

    log.logger.info("opening the window - (Calculator)")
    root.mainloop()
    log.logger.info("closing the window - (Calculator)")