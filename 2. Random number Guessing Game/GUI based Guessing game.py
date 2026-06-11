from tkinter import *
import random

# ================= WINDOW =================
root = Tk()
root.title("Number Guessing Game")
root.geometry("700x600")
root.config(bg="#0f172a")
root.resizable(False, False)

# ================= COLORS =================
BG_COLOR = "#0f172a"
CARD_COLOR = "#1e293b"
TEXT_COLOR = "#f8fafc"
NEON_BLUE = "#38bdf8"
NEON_GREEN = "#22c55e"
NEON_RED = "#ef4444"
INPUT_BG = "#334155"

# ================= GAME VARIABLES =================
jackpot = random.randint(1, 100)
chance = 7

name_var = StringVar()
guess_var = StringVar()
message_var = StringVar()

# ================= FUNCTIONS =================
def check_guess():
    global chance
    global jackpot

    name = name_var.get()

    try:
        guess = int(guess_var.get())
    except:
        message_var.set("⚠ Enter a valid number!")
        return

    if chance > 0:
        if guess == jackpot:
            message_var.set(f"🎉 Awesome {name}! {jackpot} is correct!")

        elif guess > jackpot:
            chance -= 1
            message_var.set(f"Too High! Attempts left: {chance}")

        else:
            chance -= 1
            message_var.set(f"Too Low! Attempts left: {chance}")

    else:
        message_var.set(f"💀 Game Over! Number was {jackpot}")

# ================= RESTART GAME =================
def restart_game():
    global jackpot
    global chance

    jackpot = random.randint(1, 100)
    chance = 7

    # Clear variables
    name_var.set("")
    guess_var.set("")
    message_var.set("🎮 New Game Started!")

    # Reset placeholders
    name_entry.delete(0, END)
    guess_entry.delete(0, END)

    add_placeholder(name_entry, "Enter your name")
    add_placeholder(guess_entry, "Enter your guess")


# ================= TITLE =================
display_label = Label(
    root,
    text="NUMBER GUESSING GAME",
    bg=BG_COLOR,
    fg=NEON_BLUE,
    font=("Orbitron", 24, "bold")
)
display_label.pack(pady=20)

# ================= MAIN CARD =================
card = Frame(
    root,
    bg=CARD_COLOR,
    bd=0,
    highlightthickness=2,
    highlightbackground=NEON_BLUE
)

card.pack(padx=40, pady=20, fill="both", expand=True)

# ================= SUBTITLE =================
Label(
    card,
    text="Guess a number between 1 and 100",
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    font=("Poppins", 14)
).pack(pady=(30, 20))

# ================= PLACEHOLDER FUNCTION =================
def add_placeholder(entry, placeholder):

    entry.insert(0, placeholder)
    entry.config(fg="#94a3b8")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.config(fg="white")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="#94a3b8")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# ================= NAME ENTRY =================
name_entry = Entry(
    card,
    textvariable=name_var,
    font=("Poppins", 16),
    bg=INPUT_BG,
    fg="#94a3b8",
    insertbackground="white",
    relief=FLAT,
    justify="center",
    width=20
)

name_entry.pack(pady=10, ipady=8)

# Placeholder text
add_placeholder(name_entry, "Enter your name")

# ================= GUESS ENTRY =================
guess_entry = Entry(
    card,
    textvariable=guess_var,
    font=("Poppins", 16),
    bg=INPUT_BG,
    fg="white",
    insertbackground="white",
    relief=FLAT,
    justify="center",
    width=20
)
guess_entry.pack(pady=10, ipady=8)

add_placeholder(guess_entry, "Enter your guess")

# ================= BUTTON =================
submit_btn = Button(
    card,
    text="🚀 SUBMIT GUESS",
    command=check_guess,
    bg=NEON_GREEN,
    fg="black",
    activebackground="#4ade80",
    activeforeground="black",
    relief=FLAT,
    cursor="hand2",
    font=("Poppins", 14, "bold"),
    padx=20,
    pady=10
)

submit_btn.pack(pady=25)


# ================= HOVER EFFECT =================
def on_enter(e):
    submit_btn.config(bg="#4ade80")

def on_leave(e):
    submit_btn.config(bg=NEON_GREEN)

submit_btn.bind("<Enter>", on_enter)
submit_btn.bind("<Leave>", on_leave)

# ================= MESSAGE LABEL =================
Label(
    card,
    textvariable=message_var,
    bg=CARD_COLOR,
    fg=NEON_BLUE,
    font=("Poppins", 15, "bold"),
    wraplength=500
).pack(pady=10)

# ================= RESTART BUTTON =================
restart_btn = Button(
    card,
    text="🔄 RESTART GAME",
    command=restart_game,
    bg=NEON_RED,
    fg="white",
    activebackground="#f87171",
    activeforeground="white",
    relief=FLAT,
    cursor="hand2",
    font=("Poppins", 13, "bold"),
    padx=10,
    pady=5
)

restart_btn.pack(pady=10)

# ================= HOVER EFFECT =================
def restart_enter(e):
    restart_btn.config(bg="#f87171")

def restart_leave(e):
    restart_btn.config(bg=NEON_RED)

restart_btn.bind("<Enter>", restart_enter)
restart_btn.bind("<Leave>", restart_leave)


# ================= FOOTER =================
Label(
    root,
    text="Python Tkinter Mini Project",
    bg=BG_COLOR,
    fg="#64748b",
    font=("Poppins", 10)
).pack(pady=10)

# ================= RUN =================
root.mainloop()