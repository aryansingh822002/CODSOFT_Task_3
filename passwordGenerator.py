import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.username_var = tk.StringVar()
        self.length_var = tk.StringVar()
        self.generated_password_var = tk.StringVar()
        self.generated_password_var.set("")

        self.username_label = tk.Label(root, text="Enter Username:")
        self.username_label.pack(padx=10, pady=5)

        self.username_entry = tk.Entry(root, textvariable=self.username_var)
        self.username_entry.pack(padx=10, pady=5)

        self.length_label = tk.Label(root, text="Enter Password Length:")
        self.length_label.pack(padx=10, pady=5)

        self.length_entry = tk.Entry(root, textvariable=self.length_var)
        self.length_entry.pack(padx=10, pady=5)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(padx=10, pady=5)

        self.generated_password_label = tk.Label(root, text="Generated Password:")
        self.generated_password_label.pack(padx=10, pady=5)

        self.generated_password_label = tk.Label(root, textvariable=self.generated_password_var, font=("Arial", 14))
        self.generated_password_label.pack(padx=10, pady=5)

        self.accept_button = tk.Button(root, text="Accept", command=self.accept_password)
        self.accept_button.pack(padx=10, pady=5)

        self.reject_button = tk.Button(root, text="Reject", command=self.reject_password)
        self.reject_button.pack(padx=10, pady=5)

        self.generated_password = ""

    def generate_password(self):
        password_length = int(self.length_var.get()) if self.length_var.get() else 12
        characters = string.ascii_letters + string.digits + string.punctuation
        self.generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        self.generated_password_var.set(self.generated_password)

    def accept_password(self):
        if self.generated_password:
            username = self.username_var.get() if self.username_var.get() else "User"
            message = f"Password accepted for {username}: {self.generated_password}"
            self.generated_password_var.set(message)

    def reject_password(self):
        self.generated_password_var.set("")
        self.generated_password = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
