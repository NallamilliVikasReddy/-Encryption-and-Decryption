import tkinter as tk

def encrypt_text():
    shift = int(shift_entry.get())
    plaintext = plaintext_entry.get()
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            ciphertext += char

    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(0, ciphertext)

def decrypt_text():
    shift = int(shift_entry.get())
    ciphertext = ciphertext_entry.get()
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            plaintext += char

    plaintext_entry.delete(0, tk.END)
    plaintext_entry.insert(0, plaintext)

root = tk.Tk()
root.title("Text Encryption/Decryption")

plaintext_label = tk.Label(root, text="Plaintext:")
plaintext_label.grid(row=0, column=0, padx=10, pady=5)
plaintext_entry = tk.Entry(root, width=30)
plaintext_entry.grid(row=0, column=1, padx=10, pady=5)

shift_label = tk.Label(root, text="Shift:")
shift_label.grid(row=1, column=0, padx=10, pady=5)
shift_entry = tk.Entry(root, width=30)
shift_entry.grid(row=1, column=1, padx=10, pady=5)

ciphertext_label = tk.Label(root, text="Ciphertext:")
ciphertext_label.grid(row=2, column=0, padx=10, pady=5)
ciphertext_entry = tk.Entry(root, width=30)
ciphertext_entry.grid(row=2, column=1, padx=10, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)


root.mainloop()
