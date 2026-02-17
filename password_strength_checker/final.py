import tkinter as tk
import re

# -------------------------
# Backend Logic (Same)
# -------------------------

def check_password_strength(password):
    if len(password) < 8:
        return "Guru password chikkudhu, innu swalpa udha irbekku.", "#ff4d6d"
    if not any(char.isdigit() for char in password):
        return "Maanyare nimmaa password nalli sankhe annu balisiri", "#c77dff"
    if not any(char.isupper() for char in password):
        return "Uppercase irli guru", "#c77dff"
    if not any(char.islower() for char in password):
        return "Poojyare lowercase irli", "#c77dff"
    if not re.search(r'[!@#$%^&*()_{}:"<>?/.,;]', password):
        return "Special char irbekku guru", "#c77dff"
    
    return "Masth password crazy 🔥", "#9d4edd"


# -------------------------
# GUI Setup
# -------------------------

root = tk.Tk()
root.title("PASSWORD RAKSHAKA")
root.geometry("1000x800")
root.configure(bg="#0d0c1d")


# -------- Lock Graphic --------
canvas = tk.Canvas(root, width=80, height=80, bg="#0d0c1d", highlightthickness=0)
canvas.pack(pady=10)

canvas.create_rectangle(20, 35, 60, 70, outline="#9d4edd", width=3)
canvas.create_arc(20, 5, 60, 55, start=0, extent=180, outline="#9d4edd", width=3)


# -------- Title --------
title = tk.Label(root,
                 text="PASSWORD RAKSHAKA",
                 font=("Orbitron", 32, "bold"),
                 bg="#0d0c1d",
                 fg="#c77dff")
title.pack()

tagline = tk.Label(root,
                   text="Strong Illandre Reject 😎",
                   font=("Consolas", 16, "bold"),
                   bg="#0d0c1d",
                   fg="#9d4edd")
tagline.pack(pady=(0, 20))


# -------- Password Entry --------
entry = tk.Entry(root,
                 show="*",
                 width=30,
                 font=("Consolas", 16, "bold"),
                 bg="#1a1a2e",
                 fg="#f8f9fa",
                 insertbackground="#c77dff",
                 relief="flat")
entry.pack(pady=10)


# -------- Show / Hide Toggle --------
def toggle_password():
    if entry.cget('show') == "*":
        entry.config(show="")
        toggle_btn.config(text="Hide")
    else:
        entry.config(show="*")
        toggle_btn.config(text="Show")

toggle_btn = tk.Button(root,
                       text="Show",
                       command=toggle_password,
                       bg="#1a1a2e",
                       fg="#9d4edd",
                       font=("Consolas", 10, "bold"),
                       relief="flat")
toggle_btn.pack()


# -------- Strength Indicator --------
strength_bar = tk.Frame(root, bg="#1a1a2e", width=300, height=10)
strength_bar.pack(pady=15)

strength_fill = tk.Frame(strength_bar, bg="#ff4d6d", width=0, height=10)
strength_fill.pack(side="left")


# -------- Result Display --------
result_label = tk.Label(root,
                        text="",
                        wraplength=500,
                        font=("Consolas", 20, "bold"),
                        bg="#0d0c1d",
                        fg="#f8f9fa")
result_label.pack(pady=15)


# -------- Check Function --------
def check_password():
    password = entry.get()
    message, color = check_password_strength(password)
    result_label.config(text=message, fg=color)

    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if re.search(r'[!@#$%^&*()_{}:"<>?/.,;]', password):
        score += 1

    strength_fill.config(width=score * 60)

    if score <= 2:
        strength_fill.config(bg="#ff4d6d")
    elif score == 3:
        strength_fill.config(bg="#c77dff")
    else:
        strength_fill.config(bg="#9d4edd")


check_btn = tk.Button(root,
                      text="ANALYZE PASSWORD",
                      command=check_password,
                      bg="#9d4edd",
                      fg="white",
                      font=("Consolas", 12, "bold"),
                      relief="flat",
                      padx=15,
                      pady=8)
check_btn.pack(pady=10)


# -------- Hover Message Label --------
hover_label = tk.Label(root,
                       text="",
                       font=("Consolas", 16, "bold"),
                       bg="#0d0c1d",
                       fg="#ff4d6d")
hover_label.pack(pady=5)


# -------- Exit Function --------
def exit_app():
    root.destroy()


# -------- Hover Events --------
def on_enter(e):
    hover_label.config(text="ISHTU BEGGA HOGBEKKAA CHINNU 😏",
                       font=("Consolas", 24, "bold"))

def on_leave(e):
    hover_label.config(text="")


# -------- Exit Button --------
exit_btn = tk.Button(root,
                     text="EXIT",
                     command=exit_app,
                     bg="#ff4d6d",
                     fg="white",
                     font=("Consolas", 12, "bold"),
                     relief="flat",
                     padx=15,
                     pady=8)

exit_btn.pack(pady=10)

exit_btn.bind("<Enter>", on_enter)
exit_btn.bind("<Leave>", on_leave)

root.mainloop()
