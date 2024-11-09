# main.py
import tkinter as tk
from tkinter import messagebox, scrolledtext
from backend import save_credentials, check_credentials
from chatbot import get_response

# GUI for ChatBot Interface
def chatbot_interface():
    def send_message():
        user_message = user_input.get("1.0", "end-1c")
        chat_area.insert(tk.END, f"You: {user_message}\n")
        response = get_response(user_message)
        chat_area.insert(tk.END, f"Bot: {response}\n\n")
        user_input.delete("1.0", tk.END)

    # Create chatbot window
    chatbot_window = tk.Toplevel()
    chatbot_window.title("ChatBot Interface")
    chatbot_window.configure(bg="#2c2f33")

    chat_area = scrolledtext.ScrolledText(chatbot_window, bg="#23272a", fg="white", wrap=tk.WORD)
    chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    user_input = tk.Text(chatbot_window, height=2, bg="#2c2f33", fg="white")
    user_input.pack(padx=10, pady=5, fill=tk.X)

    send_button = tk.Button(chatbot_window, text="Send", command=send_message, bg="#7289da", fg="white")
    send_button.pack(pady=5)

# GUI for Login Page
def login_page():
    def login():
        user_id = id_entry.get()
        password = password_entry.get()

        if check_credentials(user_id, password):
            messagebox.showinfo("Success", "Login successful!")
            login_window.destroy()
            chatbot_interface()
        else:
            messagebox.showerror("Error", "Invalid credentials, exiting!")
            login_window.destroy()

    # Create login window
    login_window = tk.Toplevel()
    login_window.title("Login Page")
    login_window.configure(bg="#2c2f33")

    tk.Label(login_window, text="User ID:", bg="#2c2f33", fg="white").pack(pady=5)
    id_entry = tk.Entry(login_window, bg="#23272a", fg="white")
    id_entry.pack(pady=5)

    tk.Label(login_window, text="Password:", bg="#2c2f33", fg="white").pack(pady=5)
    password_entry = tk.Entry(login_window, show="*", bg="#23272a", fg="white")
    password_entry.pack(pady=5)

    login_button = tk.Button(login_window, text="Login", command=login, bg="#7289da", fg="white")
    login_button.pack(pady=10)

# GUI for Registration Page
def registration_page():
    def register():
        user_id = id_entry.get()
        password = password_entry.get()

        if user_id and password:
            save_credentials(user_id, password)
            messagebox.showinfo("Success", "Registration successful!")
            registration_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    # Create registration window
    registration_window = tk.Toplevel()
    registration_window.title("Registration Page")
    registration_window.configure(bg="#2c2f33")

    tk.Label(registration_window, text="User ID:", bg="#2c2f33", fg="white").pack(pady=5)
    id_entry = tk.Entry(registration_window, bg="#23272a", fg="white")
    id_entry.pack(pady=5)

    tk.Label(registration_window, text="Password:", bg="#2c2f33", fg="white").pack(pady=5)
    password_entry = tk.Entry(registration_window, show="*", bg="#23272a", fg="white")
    password_entry.pack(pady=5)

    register_button = tk.Button(registration_window, text="Register", command=register, bg="#7289da", fg="white")
    register_button.pack(pady=10)

# Main Application
def main_app():
    # Create main window
    root = tk.Tk()
    root.title("Welcome to ChatBot System")
    root.configure(bg="#2c2f33")

    tk.Label(root, text="Welcome to ChatBot!", font=("Arial", 16), bg="#2c2f33", fg="white").pack(pady=20)

    register_button = tk.Button(root, text="Register", command=registration_page, bg="#7289da", fg="white", width=20)
    register_button.pack(pady=10)

    login_button = tk.Button(root, text="Login", command=login_page, bg="#7289da", fg="white", width=20)
    login_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_app()
