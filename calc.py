import tkinter as tk
import math

def on_click(event):
    # Function to handle button clicks and update the expression
    current_text = entry.get()
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "⌫":
        entry.delete(len(current_text) - 1)
    elif button_text == "sin⁻¹":
        entry.insert(tk.END, "math.asin(")
    elif button_text == "cos⁻¹":
        entry.insert(tk.END, "math.acos(")
    elif button_text == "tan⁻¹":
        entry.insert(tk.END, "math.atan(")
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Advanced Scientific Calculator")
root.geometry("400x500")
root.configure(bg="black")

# Entry widget to display the expression and result
entry = tk.Entry(root, font=("Helvetica", 20), bg="white", fg="black", justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

# List of buttons and their positions
buttons = [
("sin⁻¹", "sin⁻¹", None),("cos⁻¹", "cos⁻¹", None),("tan⁻¹", "tan⁻¹", None),("sin", "sin", "math.sin"),("cos", "cos", "math.cos"),
("tan", "tan", "math.tan"),("π", "π", "math.pi"),("log", "log", "math.log10"),("ln", "ln", "math.log"), ("√", "√", "math.sqrt"),
("x²", "²", "**2"),("xʸ", "^", "**"),("!", "!", "math.factorial"),("e", "e", "math.e"), ("x³", "³", "**3"),
("(", "(", None),(")", ")", None), ("0", "0", None),("C", "C", None),("⌫", "⌫", None),
("1", "1", None), ("2", "2", None), ("3", "3", None),("/", "/", None),("*", "*", None),
("4", "4", None) ,("5", "5", None),("6", "6", None),("-", "-", None),("+", "+", None),
("7", "7", None),("8", "8", None),("9", "9", None),(".", ".", None), ("=", "=", None), 
]

# Create buttons and add them to the window
for i, (name, symbol, func) in enumerate(buttons):
    btn = tk.Button(root, text=symbol, font=("Helvetica", 20), bg="gray", fg="black", height=2, width=6)
    btn.grid(row=i // 5 + 1, column=i % 5, padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", on_click)
    root.grid_columnconfigure(i % 5, weight=1)
    root.grid_rowconfigure(i // 5 + 1, weight=1)

# Run the main loop
root.mainloop()
