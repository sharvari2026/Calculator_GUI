from tkinter import Tk, Entry, StringVar, Button

class Calculator:
    def __init__(self, app):
        app.title("MINI CALCULATOR")
        app_width = 400  # Width of the calculator window
        screen_width = app.winfo_screenwidth()
        x_position = (screen_width - app_width) // 2  # Calculate the X-coordinate to center horizontally
        app.geometry(f'{app_width}x600+{x_position}+0')
        app.config(bg='gray')
        app.resizable(False, False)

        self.equation = StringVar()
        self.entryValue = ''

        e1 = Entry(width=17, bg='#fff', font=('Arial Bold', 32), textvariable=self.equation, justify='center')
        e1.grid(row=0, column=0, columnspan=5)

        b1 = Button(root, width=11, height=4, text='(', relief='raised', bg='light green', command=lambda: self.show('('))
        b1.grid(row=2, column=1, padx=5, pady=5)

        b2 = Button(root, width=11, height=4, text=')', relief='raised', bg='light green', command=lambda: self.show(')'))
        b2.grid(row=2, column=2, padx=5, pady=5)

        b3 = Button(root, width=11, height=4, text='Delete', relief='raised', bg='light green', command=self.delete_last)
        b3.grid(row=6, column=3, padx=5, pady=5)

        b4 = Button(root, width=11, height=4, text='1', relief='raised', bg='white', command=lambda: self.show('1'))
        b4.grid(row=3, column=1, padx=5, pady=5)

        b5 = Button(root, width=11, height=4, text='2', relief='raised', bg='white', command=lambda: self.show('2'))
        b5.grid(row=3, column=2, padx=5, pady=5)

        b6 = Button(root, width=11, height=4, text='3', relief='raised', bg='white', command=lambda: self.show('3'))
        b6.grid(row=3, column=3, padx=5, pady=5)

        b7 = Button(root, width=11, height=4, text='4', relief='raised', bg='white', command=lambda: self.show('4'))
        b7.grid(row=4, column=1, padx=5, pady=5)

        b8 = Button(root, width=11, height=4, text='5', relief='raised', bg='white', command=lambda: self.show('5'))
        b8.grid(row=4, column=2, padx=5, pady=5)

        b9 = Button(root, width=11, height=4, text='6', relief='raised', bg='white', command=lambda: self.show('6'))
        b9.grid(row=4, column=3, padx=5, pady=5)

        b10 = Button(root, width=11, height=4, text='7', relief='raised', bg='white', command=lambda: self.show('7'))
        b10.grid(row=5, column=1, padx=5, pady=5)

        b11 = Button(root, width=11, height=4, text='8', relief='raised', bg='white', command=lambda: self.show('8'))
        b11.grid(row=5, column=2, padx=5, pady=5)

        b12 = Button(root, width=11, height=4, text='9', relief='raised', bg='white', command=lambda: self.show('9'))
        b12.grid(row=5, column=3, padx=5, pady=5)

        b13 = Button(root, width=11, height=4, text='0', relief='raised', bg='white', command=lambda: self.show('0'))
        b13.grid(row=6, column=1, padx=5, pady=5)

        b14 = Button(root, width=11, height=4, text='+', relief='raised', bg='pink', command=lambda: self.show('+'))
        b14.grid(row=2, column=4, padx=5, pady=5)

        b15 = Button(root, width=11, height=4, text='-', relief='raised', bg='pink', command=lambda: self.show('-'))
        b15.grid(row=3, column=4, padx=5, pady=5)

        b16 = Button(root, width=11, height=4, text='x', relief='raised', bg='pink', command=lambda: self.show('*'))
        b16.grid(row=4, column=4, padx=5, pady=5)

        b17 = Button(root, width=11, height=4, text='/', relief='flat', bg='pink', command=lambda: self.show('/'))
        b17.grid(row=5, column=4, padx=5, pady=5)

        b18 = Button(root, width=11, height=4, text='.', relief='raised', bg='light green', command=lambda: self.show('.'))
        b18.grid(row=2, column=3, padx=5, pady=5)

        b19 = Button(root, width=11, height=4, text='=', relief='raised', bg='pink', command=self.solve)
        b19.grid(row=6, column=4, padx=5, pady=5)

        b20 = Button(root, width=11, height=4, text='Clear', relief='raised', bg='skyblue', command=self.clear)
        b20.grid(row=6, column=2, padx=5, pady=5)

    def show(self, value):
        self.entryValue += str(value)
        self.equation.set(self.entryValue)

    def clear(self):
        self.entryValue = ''
        self.equation.set(self.entryValue)

    def delete_last(self):
        self.entryValue = self.entryValue[:-1]  # Remove the last character
        self.equation.set(self.entryValue)

    def solve(self):
        result = eval(self.entryValue)
        self.equation.set(result)

root = Tk()
Calculator = Calculator(root)
root.mainloop()
