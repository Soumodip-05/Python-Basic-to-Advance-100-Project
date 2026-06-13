import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordGenerator(tk.Tk):

    def __init__(self):
        super().__init__()

        # WINDOW
        self.title("Password Generator")
        self.geometry("650x500")
        self.config(bg="#ffffff")
        self.resizable(False, False)

        # COLORS
        self.bg_color = "#ffffff"
        self.blue = "#0364D3"
        self.light_gray = "#F4F4F5"
        self.text_color = "#151616"

        # VARIABLES
        self.password_type = tk.StringVar(value="random")

        self.letters_var = tk.IntVar(value=1)
        self.digits_var = tk.IntVar(value=1)

        # TITLE
        title = tk.Label(
            self,
            text="Choose password type",
            font=("Arial", 12, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        title.pack(anchor="w", padx=30, pady=(20, 10))

        # TYPE FRAME
        type_frame = tk.Frame(self, bg=self.light_gray)
        type_frame.pack(fill="x", padx=140)

        # RANDOM BUTTON
        self.random_btn = tk.Button(
            type_frame,
            text="⟢Random",
            font=("Arial", 12, "bold"),
            bg="white",
            fg=self.text_color,
            relief="flat",
            width=15,
            command=self.select_random
        )
        self.random_btn.grid(row=0, column=0, padx=(8,15), pady=8)

        # PIN BUTTON
        self.pin_btn = tk.Button(
            type_frame,
            text="♯PIN",
            font=("Arial", 12, "bold"),
            bg=self.light_gray,
            fg=self.text_color,
            relief="flat",
            width=15,
            command=self.select_pin
        )
        self.pin_btn.grid(row=0, column=1, padx=(15,8), pady=8)

        # CUSTOMIZE TITLE
        customize = tk.Label(
            self,
            text="Customize your new password",
            font=("Arial", 16, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        customize.pack(anchor="w", padx=30, pady=(30, 10))

        # SLIDER FRAME
        slider_frame = tk.Frame(self, bg=self.bg_color)
        slider_frame.pack(fill="x", padx=30)

        tk.Label(
            slider_frame,
            text="Characters",
            font=("Arial", 14),
            bg=self.bg_color
        ).pack(side="left")

        self.length_slider = tk.Scale(
            slider_frame,
            from_=4,
            to=50,
            orient="horizontal",
            length=300,
            bg=self.bg_color,
            highlightthickness=0
        )
        self.length_slider.set(20)
        self.length_slider.pack(side="left", padx=20)

        # CHECKBOX FRAME
        self.option_frame = tk.Frame(self, bg=self.bg_color)
        self.option_frame.pack(anchor="w", padx=30, pady=20)

        self.letter_check = tk.Checkbutton(
            self.option_frame,
            text="Letters",
            variable=self.letters_var,
            font=("Arial", 13),
            bg=self.bg_color
        )
        self.letter_check.grid(row=0, column=0, padx=10)

        self.digit_check = tk.Checkbutton(
            self.option_frame,
            text="Digits",
            variable=self.digits_var,
            font=("Arial", 13),
            bg=self.bg_color
        )
        self.digit_check.grid(row=0, column=1, padx=10)

        # GENERATED PASSWORD
        password_title = tk.Label(
            self,
            text="Generated password",
            font=("Arial", 16, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        password_title.pack(anchor="w", padx=30, pady=(20, 10))

        self.password_entry = tk.Entry(
            self,
            font=("Consolas", 22, "bold"),
            justify="center",
            relief="solid",
            bd=1
        )
        self.password_entry.pack(fill="x", padx=30, ipady=20)

        # BUTTON FRAME
        btn_frame = tk.Frame(self, bg=self.bg_color)
        btn_frame.pack(fill="x", padx=30, pady=25)

        # COPY BUTTON
        copy_btn = tk.Button(
            btn_frame,
            text="Copy Password",
            font=("Arial", 14, "bold"),
            bg=self.blue,
            fg="white",
            relief="flat",
            command=self.copy_password
        )
        copy_btn.pack(side="left", expand=True, fill="x", padx=(0, 10), ipady=12)

        # REFRESH BUTTON
        refresh_btn = tk.Button(
            btn_frame,
            text="Refresh Password",
            font=("Arial", 14, "bold"),
            bg="white",
            fg=self.blue,
            relief="solid",
            bd=1,
            command=self.generate_password
        )
        refresh_btn.pack(side="left", expand=True, fill="x", padx=(10, 0), ipady=12)

        # FIRST PASSWORD
        self.generate_password()

    # RANDOM MODE
    def select_random(self):

        self.password_type.set("random")

        self.random_btn.config(bg="white")
        self.pin_btn.config(bg=self.light_gray)

        self.option_frame.pack(anchor="w", padx=30, pady=20)

        self.generate_password()

    # PIN MODE
    def select_pin(self):

        self.password_type.set("pin")

        self.pin_btn.config(bg="white")
        self.random_btn.config(bg=self.light_gray)

        self.option_frame.pack_forget()

        self.generate_password()

    # GENERATE PASSWORD
    def generate_password(self):

        length = self.length_slider.get()

        # PIN PASSWORD
        if self.password_type.get() == "pin":

            password = ""

            for i in range(length):
                password += random.choice(string.digits)

        # RANDOM PASSWORD
        else:

            characters = ""

            if self.letters_var.get():
                characters += string.ascii_letters

            if self.digits_var.get():
                characters += string.digits

            if characters == "":
                messagebox.showwarning(
                    "Warning",
                    "Select at least one option"
                )
                return

            password = ""

            for i in range(length):
                password += random.choice(characters)

        # DISPLAY PASSWORD
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    # COPY PASSWORD
    def copy_password(self):

        password = self.password_entry.get()

        if password:
            self.clipboard_clear()
            self.clipboard_append(password)

            messagebox.showinfo(
                "Copied",
                "Password copied to clipboard"
            )


# RUN APP
app = PasswordGenerator()
app.mainloop()