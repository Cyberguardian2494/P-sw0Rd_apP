import random
import string
import tkinter as tk

def generate_password():
    """Generates a random password based on the given criteria."""
    uppercase_letters = random.sample(string.ascii_uppercase, 3)
    lowercase_letters = random.sample(string.ascii_lowercase, 3)
    numbers = random.sample(string.digits, 3)
    symbols = random.sample("@#$%^&*_?", 3)

    password_list = uppercase_letters + lowercase_letters + numbers + symbols
    random.shuffle(password_list)

    password.set("".join(password_list))  # Update the UI with the new password

# Create the UI window
root = tk.Tk()
root.title("Password Generator")

password = tk.StringVar()  # Variable to hold generated password

# UI Elements
label = tk.Label(root, text="Generated Password:", font=("Arial", 12))
label.pack(pady=5)

password_display = tk.Entry(root, textvariable=password, font=("Arial", 12), width=20, state="readonly")
password_display.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12))
generate_button.pack(pady=5)

# Run the UI application
root.mainloop()
