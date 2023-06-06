import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet

# Generate a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Encrypt the selected file
def encrypt_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path.endswith(".txt"):
        with open("key.key", "rb") as key_file:
            key = key_file.read()
        cipher_suite = Fernet(key)
        with open(file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = cipher_suite.encrypt(file_data)
        encrypted_file_path = file_path + ".encrypted"
        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
        result_label.config(text="File encrypted successfully!")
    else:
        result_label.config(text="Invalid file format. Please select a .txt file.")

# Decrypt the selected file
def decrypt_file():
    file_path = filedialog.askopenfilename(filetypes=[("Encrypted files", "*.encrypted")])
    if file_path.endswith(".encrypted"):
        with open("key.key", "rb") as key_file:
            key = key_file.read()
        cipher_suite = Fernet(key)
        with open(file_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        decrypted_file_path = file_path[:-10]  # Remove the ".encrypted" extension
        with open(decrypted_file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)
        result_label.config(text="File decrypted successfully!")
    else:
        result_label.config(text="Invalid file format. Please select an .encrypted file.")

# Create the UI
window = tk.Tk()
window.title("Text File Encrypter/Decrypter")

# Generate Key button
generate_key_button = tk.Button(window, text="Generate Key", command=generate_key)
generate_key_button.pack(pady=10)

# Encrypt File button
encrypt_file_button = tk.Button(window, text="Encrypt File", command=encrypt_file)
encrypt_file_button.pack(pady=10)

# Decrypt File button
decrypt_file_button = tk.Button(window, text="Decrypt File", command=decrypt_file)
decrypt_file_button.pack(pady=10)

# Result label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
