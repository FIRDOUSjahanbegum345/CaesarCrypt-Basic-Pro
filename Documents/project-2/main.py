# =========================================================
# CAESARCRYPT BASIC PRO
# Professional Internship Version
# Features:
# 1. Caesar Cipher Encryption/Decryption
# 2. Custom Shift Value
# 3. Passcode Protection (SHA-256 Hashing)
# 4. Copy Output
# 5. Reset
# 6. Save Output to File
# 7. Brute Force Attack Demo
# =========================================================

import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
import hashlib

# =========================================================
# Global Variables
# =========================================================
saved_passcode = ""

# =========================================================
# Caesar Cipher Functions
# =========================================================
def encrypt_text(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def decrypt_text(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char

    return result


# =========================================================
# Encrypt Function
# =========================================================
def generate_secret():
    global saved_passcode

    message = input_box.get("1.0", tk.END).strip()
    passcode = pass_entry.get().strip()
    shift_value = shift_entry.get().strip()

    if not message:
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    if not passcode:
        messagebox.showwarning("Warning", "Please enter a passcode.")
        return

    if not shift_value.isdigit():
        messagebox.showwarning("Warning", "Shift must be a number.")
        return

    shift = int(shift_value)

    encrypted = encrypt_text(message, shift)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, encrypted)

    # Save hashed passcode
    saved_passcode = hashlib.sha256(passcode.encode()).hexdigest()

    messagebox.showinfo("Success", "Message encrypted successfully.")


# =========================================================
# Decrypt Function
# =========================================================
def reveal_secret():

    encrypted_message = input_box.get("1.0", tk.END).strip()
    entered_passcode = pass_entry.get().strip()
    shift_value = shift_entry.get().strip()

    if not encrypted_message:
        messagebox.showwarning("Warning", "Please enter encrypted text.")
        return

    if not shift_value.isdigit():
        messagebox.showwarning("Warning", "Shift must be a number.")
        return

    shift = int(shift_value)

    entered_hash = hashlib.sha256(
        entered_passcode.encode()
    ).hexdigest()

    if entered_hash != saved_passcode:
        messagebox.showerror("Error", "Incorrect passcode.")
        return

    decrypted = decrypt_text(encrypted_message, shift)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, decrypted)

    messagebox.showinfo("Success", "Message decrypted successfully.")


# =========================================================
# Copy Output
# =========================================================
def copy_output():

    text = output_box.get("1.0", tk.END).strip()

    if text:
        root.clipboard_clear()
        root.clipboard_append(text)

        messagebox.showinfo(
            "Copied",
            "Output copied successfully."
        )


# =========================================================
# Reset All
# =========================================================
def reset_all():

    global saved_passcode

    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)

    pass_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)

    saved_passcode = ""


# =========================================================
# Save Output To File
# =========================================================
def save_output():

    text = output_box.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning(
            "Warning",
            "No output to save."
        )
        return

    file = filedialog.asksaveasfile(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file:
        file.write(text)
        file.close()

        messagebox.showinfo(
            "Saved",
            "Output saved successfully."
        )


# =========================================================
# Brute Force Attack Demo
# =========================================================
def brute_force():

    encrypted_message = input_box.get("1.0", tk.END).strip()

    if not encrypted_message:
        messagebox.showwarning(
            "Warning",
            "Enter encrypted message first."
        )
        return

    output_box.delete("1.0", tk.END)

    for shift in range(1, 26):

        decrypted = decrypt_text(
            encrypted_message,
            shift
        )

        output_box.insert(
            tk.END,
            f"Shift {shift}: {decrypted}\n"
        )


# =========================================================
# Main Window
# =========================================================
root = tk.Tk()

root.title("CaesarCrypt Basic Pro")
root.geometry("950x760")
root.config(bg="#1e293b")

# =========================================================
# Header
# =========================================================
title = tk.Label(
    root,
    text="🔐 CAESARCRYPT BASIC PRO",
    font=("Arial", 24, "bold"),
    bg="#1e293b",
    fg="#38bdf8"
)

title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Cybersecurity Internship Project",
    font=("Arial", 12),
    bg="#1e293b",
    fg="white"
)

subtitle.pack()

# =========================================================
# Passcode + Shift
# =========================================================
top_frame = tk.Frame(root, bg="#1e293b")
top_frame.pack(pady=15)

# Passcode
tk.Label(
    top_frame,
    text="Passcode:",
    font=("Arial", 12),
    bg="#1e293b",
    fg="white"
).grid(row=0, column=0, padx=5)

pass_entry = tk.Entry(
    top_frame,
    show="*",
    width=20,
    font=("Arial", 12)
)

pass_entry.grid(row=0, column=1, padx=10)

# Shift
tk.Label(
    top_frame,
    text="Shift:",
    font=("Arial", 12),
    bg="#1e293b",
    fg="white"
).grid(row=0, column=2, padx=5)

shift_entry = tk.Entry(
    top_frame,
    width=10,
    font=("Arial", 12)
)

shift_entry.grid(row=0, column=3, padx=10)

# =========================================================
# Input Box
# =========================================================
tk.Label(
    root,
    text="Enter Message:",
    font=("Arial", 14, "bold"),
    bg="#1e293b",
    fg="white"
).pack()

input_box = scrolledtext.ScrolledText(
    root,
    width=80,
    height=8,
    font=("Consolas", 12),
    bg="#0f172a",
    fg="white",
    insertbackground="white"
)

input_box.pack(pady=10)

# =========================================================
# Buttons
# =========================================================
button_frame = tk.Frame(root, bg="#1e293b")
button_frame.pack(pady=15)

buttons = [
    ("Encrypt", generate_secret, "#2563eb"),
    ("Decrypt", reveal_secret, "#0ea5e9"),
    ("Copy Output", copy_output, "#14b8a6"),
    ("Save File", save_output, "#22c55e"),
    ("Brute Force", brute_force, "#f59e0b"),
    ("Reset", reset_all, "#475569")
]

for i, (text, command, color) in enumerate(buttons):

    btn = tk.Button(
        button_frame,
        text=text,
        command=command,
        bg=color,
        fg="white",
        font=("Arial", 11, "bold"),
        width=13
    )

    btn.grid(row=0, column=i, padx=8)

# =========================================================
# Output Box
# =========================================================
tk.Label(
    root,
    text="Output:",
    font=("Arial", 14, "bold"),
    bg="#1e293b",
    fg="white"
).pack()

output_box = scrolledtext.ScrolledText(
    root,
    width=80,
    height=12,
    font=("Consolas", 12),
    bg="#0f172a",
    fg="#38bdf8",
    insertbackground="white"
)

output_box.pack(pady=10)

# =========================================================
# Footer
# =========================================================
footer = tk.Label(
    root,
    text="Designed for Cybersecurity Internship Demonstration",
    font=("Arial", 10),
    bg="#1e293b",
    fg="#94a3b8"
)

footer.pack(pady=15)

# =========================================================
# Run Application
# =========================================================
root.mainloop()
