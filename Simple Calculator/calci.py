import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Cool Calculator")
        master.geometry("300x400")
        master.configure(bg="#2C3E50")  # Dark blue-gray background

        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure button styles
        style.configure('TButton', 
                        background="#3498DB",  # Light blue
                        foreground="white", 
                        font=('Arial', 12, 'bold'),
                        padding=10)
        style.map('TButton', background=[('active', '#2980B9')])  # Darker blue when pressed

        # Create and style the display
        self.display = tk.Entry(master, width=20, justify='right', font=('Arial', 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # Create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Add buttons to the grid
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(master, text=button, command=cmd, style='TButton').grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Add clear button
        ttk.Button(master, text='Clear', command=self.clear, style='TButton').grid(row=row, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

        # Configure grid weights
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, key)

    def clear(self):
        self.display.delete(0, tk.END)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()