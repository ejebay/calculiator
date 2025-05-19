import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        
        # Input/output field
        self.entry = tk.Entry(root, width=20, font=("Arial", 14), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Buttons
        self.create_buttons()
        
    def create_buttons(self):
        button_list = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]
        
        row = 1
        col = 0
        for button in button_list:
            if button == '=':
                cmd = self.calculate
            elif button == 'C':
                cmd = self.clear
            else:
                cmd = lambda x=button: self.add_to_expression(x)
                
            tk.Button(self.root, text=button, width=5, height=2, font=("Arial", 12),
                     command=cmd).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
                
    def add_to_expression(self, value):
        self.entry.insert(tk.END, value)
        
    def clear(self):
        self.entry.delete(0, tk.END)
        
    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero!")
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression!")
            self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()