import tkinter as tk
import secrets
import string

root = tk.Tk()
root.title("Password Generator")
root.geometry("360x400")
root.resizable(False, False)
root.configure(bg="#202020")

password = tk.StringVar()
length = tk.IntVar(value=16)

def generate():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password.set("".join(secrets.choice(chars) for _ in range(length.get())))

def copy():
    if password.get():
        root.clipboard_clear()
        root.clipboard_append(password.get())
        status.config(text="Password copied!")

tk.Label(root, text="Password Generator", font=("Segoe UI", 20, "bold"), bg="#202020", fg="white").pack(pady=25)

tk.Label(root, text="Password Length", font=("Segoe UI", 11), bg="#202020", fg="white").pack()

tk.Scale(root, from_=6, to=32, variable=length, orient="horizontal", length=260, bg="#202020", fg="white", highlightthickness=0).pack(pady=10)

tk.Entry(root, textvariable=password, font=("Segoe UI", 13), justify="center", width=28, bg="#333333", fg="white", insertbackground="white", relief="flat").pack(pady=15, ipady=10)

tk.Button(root, text="Generate Password", command=generate, font=("Segoe UI", 12), bg="#0078D4", fg="white", relief="flat", width=22).pack(pady=8)

tk.Button(root, text="Copy Password", command=copy, font=("Segoe UI", 11), bg="#404040", fg="white", relief="flat", width=22).pack(pady=5)

status = tk.Label(root, text="", bg="#202020", fg="#4CC2FF", font=("Segoe UI", 10))
status.pack(pady=10)

generate()
root.mainloop()
