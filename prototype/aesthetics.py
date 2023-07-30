import tkinter as tk
from tkinter import ttk

def optimizeDesign(root):
    # Set the aesthetics for the application
    root.title("AI Data Analysis App")
    root.geometry("800x600")
    root.configure(bg='lightgrey')

    # Create a style object to customize the application's widgets
    style = ttk.Style(root)
    style.configure("TButton", font=("Arial", 20), background="lightblue")
    style.configure("TLabel", font=("Arial", 24), background="lightgrey")
    style.configure("TEntry", font=("Arial", 20))

    # Create a canvas to hold the application's widgets
    canvas = tk.Canvas(root, height=600, width=800, bg='lightgrey')
    canvas.pack()

    # Create a frame for the input field
    input_frame = tk.Frame(root, bg='white', bd=5)
    input_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    # Create a frame for the output display
    output_frame = tk.Frame(root, bg='white', bd=5)
    output_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor='n')

    # Create a frame for the submit button
    button_frame = tk.Frame(root, bg='lightgrey', bd=5)
    button_frame.place(relx=0.5, rely=0.9, relwidth=0.75, relheight=0.1, anchor='n')

    return input_frame, output_frame, button_frame

if __name__ == "__main__":
    root = tk.Tk()
    input_frame, output_frame, button_frame = optimizeDesign(root)
    root.mainloop()