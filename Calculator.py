import customtkinter as ctk
from PIL import Image, ImageTk

def secret_window():
    # Create the secret window as a Toplevel, not CTK()
    sw = ctk.CTkToplevel()
    sw.title("How Did You Get Here? You Are Not Supposed to Be Here")
    sw.geometry("500x700")
    sw.iconbitmap(r"C:\Users\Mansi pradhan\Downloads\website\Python\PFM.COM.ico")

def calculator_operation(root):
    # Hide the main window instead of destroying it
    root.withdraw()

    # Create a new window for the calculator operation
    operation_window = ctk.CTkToplevel()
    operation_window.title("Calculator")
    operation_window.geometry("500x500")
    operation_window.iconbitmap(r"C:\Users\Mansi pradhan\Downloads\website\Python\PFM.ico")

    # Define a function for handling operations
    def perform_operation():
        try:
            input1 = operation_entry.get().strip().lower()

            # Validate operation type
            if input1 in ["divide", "multiply", "subtraction", "addition"]:
                num1 = float(first_num_entry.get())
                num2 = float(second_num_entry.get())

                if input1 == "divide":
                    if num2 == 0:
                        result_label.configure(text="Cannot divide by zero!")
                    else:
                        result_label.configure(text=f"Result: {num1 / num2:.2f}")
                elif input1 == "multiply":
                    result_label.configure(text=f"Result: {num1 * num2:.2f}")
                elif input1 == "subtraction":
                    result_label.configure(text=f"Result: {num1 - num2:.2f}")
                elif input1 == "addition":
                    result_label.configure(text=f"Result: {num1 + num2:.2f}")
            else:
                result_label.configure(text="Invalid operation. Use divide, multiply, subtraction, addition.")
        except ValueError:
            result_label.configure(text="Please enter valid numbers.")

    def close_window(event=None):
        operation_window.destroy()
        root.deiconify()  # Show the main window again

    # UI components for the operation window
    title_label = ctk.CTkLabel(operation_window, text="Choose an operation or press ESC to close:", font=("Arial", 14))
    title_label.pack(pady=15)

    operation_label = ctk.CTkLabel(operation_window, text="Operation (divide, multiply, subtraction, addition):", font=("Arial", 12))
    operation_label.pack(pady=5)
    operation_entry = ctk.CTkEntry(operation_window, font=("Arial", 12))
    operation_entry.pack(pady=5)

    first_num_label = ctk.CTkLabel(operation_window, text="Enter first number:", font=("Arial", 12))
    first_num_label.pack(pady=10)
    first_num_entry = ctk.CTkEntry(operation_window, font=("Arial", 12))
    first_num_entry.pack(pady=5)

    second_num_label = ctk.CTkLabel(operation_window, text="Enter second number:", font=("Arial", 12))
    second_num_label.pack(pady=10)
    second_num_entry = ctk.CTkEntry(operation_window, font=("Arial", 12))
    second_num_entry.pack(pady=5)

    perform_button = ctk.CTkButton(operation_window, text="Perform Operation", font=("Arial", 12), command=perform_operation)
    perform_button.pack(pady=20)

    result_label = ctk.CTkLabel(operation_window, text="Result: ", font=("Arial", 12))
    result_label.pack(pady=15)

    # Bind the Escape key to close the window
    operation_window.bind("<Escape>", close_window)

def main():
    ctk.set_appearance_mode("Dark")

    root = ctk.CTk()
    root.title('Calculator')
    root.geometry("600x400")
    root.iconbitmap(r"C:\Users\Mansi pradhan\Downloads\website\Python\PFM.ico")

    header_label = ctk.CTkLabel(root, text="Python Calculator", font=("Arial", 20, "bold"))
    header_label.pack(pady=10)

    label = ctk.CTkLabel(root, text="Press Alt to open the calculator, Esc to exit the app", font=("Arial", 15))
    label.pack(pady=0)

    start_button = ctk.CTkButton(root, text="Start Calculator", font=("Arial", 15), command=lambda: calculator_operation(root))
    start_button.pack(padx=20, pady=20, expand=True)

    # Bind the Escape key to close the main app
    root.bind("<Escape>", lambda event: root.quit())

    # Bind the Alt key to open the calculator operation window
    root.bind("<Alt_L>", lambda event: calculator_operation(root))
    
    # Bind Ctrl + Esc to open the secret window
    root.bind("<Control-Escape>", lambda event: secret_window())

    root.mainloop()

if __name__ == "__main__":
    main()
