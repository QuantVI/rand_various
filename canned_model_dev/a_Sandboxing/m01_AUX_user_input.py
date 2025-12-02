# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 19:00:28 2025
"""

def input_pop_first(message):
    """We'd prefer system prompts for things like user-name and password
    to show as message boxes. If that isn't possible, then we default
    to terminal input."""

    try:
        import tkinter as tk
        from tkinter import simpledialog
        
        # start the loop
        root = tk.Tk()
        # hide the main window
        root.withdraw()
        # store the user input string
        result = simpledialog.askstring(title="Input", prompt=message)
        # end the loop
        root.destroy()
        
        if result is not None: return result
        else:
            print("\nDidn't get GUI input. Use terminal input.\n")
            return input(message + " ")
    except Exception:
        # We couldn't display the box
        return input(message + " ")
