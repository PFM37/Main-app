import customtkinter as ctk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
import keyword
import re
import subprocess
import threading
import Test

def text_editor(file_type="txt"):
    Test.testing()
    def open_file(event=None):
        if not confirm_discard():
            return

        filepath = askopenfilename(
            filetypes=[('Text Files', '*.txt'), ('Python Files', '*.py'), ('All Files', '*.*')]
        )

        if not filepath:
            return

        try:
            with open(filepath, 'r', encoding='utf-8') as input_file:
                text = input_file.read()

            txt_edit.delete(1.0, ctk.END)
            txt_edit.insert(ctk.END, text)
            txt_edit.edit_modified(False)
            window.title(f'Text Editor - {filepath}')
            apply_syntax_highlighting()
        except Exception as e:
            messagebox.showerror("Open File Error", f"An error occurred: {e}")

    def save_file(event=None):
        filepath = asksaveasfilename(
            defaultextension='.txt',
            filetypes=[('Text Files', '*.txt'), ('Python Files', '*.py'), ('All Files', '*.*')]
        )

        if not filepath:
            return

        try:
            with open(filepath, 'w', encoding='utf-8') as output_file:
                text = txt_edit.get(1.0, ctk.END)
                output_file.write(text)
            window.title(f'Text Editor - {filepath}')
        except Exception as e:
            messagebox.showerror("Save File Error", f"An error occurred: {e}")

    def confirm_discard():
        if txt_edit.edit_modified():
            ctk.set_appearance_mode("Dark")  # Set system theme (light/dark)
            response = messagebox.askyesnocancel(
                "Unsaved Changes",
                "You have unsaved changes. Do you want to save before proceeding?"
            )
            if response is None:  # Cancel
                return False
            if response:  # Yes
                save_file()
        return True

    def apply_syntax_highlighting():
        txt_edit.tag_remove("keyword", "1.0", ctk.END)
        txt_edit.tag_remove("comment", "1.0", ctk.END)
        txt_edit.tag_remove("string", "1.0", ctk.END)

        content = txt_edit.get("1.0", ctk.END)

        for kw in keyword.kwlist:
            for match in re.finditer(rf'\b{kw}\b', content):
                start, end = match.span()
                start_index = f"1.0 + {start} chars"
                end_index = f"1.0 + {end} chars"
                txt_edit.tag_add("keyword", start_index, end_index)

        for match in re.finditer(r'#.*', content):
            start, end = match.span()
            start_index = f"1.0 + {start} chars"
            end_index = f"1.0 + {end} chars"
            txt_edit.tag_add("comment", start_index, end_index)

        for match in re.finditer(r'(["\'])(?:(?=(\\?))\2.)*?\1', content):
            start, end = match.span()
            start_index = f"1.0 + {start} chars"
            end_index = f"1.0 + {end} chars"
            txt_edit.tag_add("string", start_index, end_index)

    def run_code():
        code = txt_edit.get(1.0, ctk.END)
        terminal.insert(ctk.END, "# This is simple recreation of the Window's Termianl, It cannot run commands\n", "green")
        terminal.tag_configure("green", foreground="green")
        terminal.insert(ctk.END, ">>> Running code...\n", "info")

        try:
            process = subprocess.Popen(
                ["python", "-c", code],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            def handle_output():
                for line in process.stdout:
                    terminal.insert(ctk.END, line, "output")
                    terminal.see(ctk.END)
                for line in process.stderr:
                    terminal.insert(ctk.END, line, "error")
                    terminal.see(ctk.END)
                terminal.insert(ctk.END, ">>> Done.\n", "info")

            threading.Thread(target=handle_output, daemon=True).start()
        except Exception as e:
            terminal.insert(ctk.END, f"Error: {e}\n", "error")



    # Create the main window
    window = ctk.CTk()
    window.title('Text Editor')
    window.geometry('1200x800')  # Larger window size

    # Set the window icon
    window.iconbitmap(r"C:\Users\Mansi pradhan\Downloads\website\Python\PFM.ico")

    # Editor Text Widget (Larger height and font size)
    txt_edit = ctk.CTkTextbox(
        window,
        wrap=ctk.WORD,
        undo=True,
        font=("Consolas", 14),  # Larger font
        height=30  # Increased height
    )
    txt_edit.grid(row=0, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)

    # Terminal Text Widget (Larger height and font size)
    terminal = ctk.CTkTextbox(
        window,
        wrap=ctk.WORD,
        font=("Consolas", 12),  # Larger font
        height=15  # Increased height
    )
    terminal.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)

    # Terminal Input (Larger input area)
    terminal_input = ctk.CTkEntry(
        window,
        font=("Arial", 14),  # Larger font
    )
    terminal_input.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

    # Buttons (Larger size and font)
    btn_open = ctk.CTkButton(
        window,
        text="Open",
        command=open_file,
        font=("Arial", 14),  # Larger font
        height=50,  # Increased button height
    )
    btn_open.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    btn_save = ctk.CTkButton(
        window,
        text="Save",
        command=save_file,
        font=("Arial", 14),
        height=50,
    )
    btn_save.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    btn_run = ctk.CTkButton(
        window,
        text="Run",
        command=run_code,
        font=("Arial", 14),
        height=50,
    )
    btn_run.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

    # Configure grid for responsiveness
    window.grid_rowconfigure(0, weight=3)  # Main text editor
    window.grid_rowconfigure(1, weight=2)  # Terminal
    window.grid_rowconfigure(2, weight=1)  # Input field
    window.grid_rowconfigure(3, weight=1)  # Buttons
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)

    # Run the application
    window.mainloop()

# Set up CustomTkinter
ctk.set_appearance_mode("Dark")

te = text_editor

if __name__ == "__main__":
    text_editor()
