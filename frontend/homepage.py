import os
from tkinter import *
from PIL import Image, ImageTk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(BASE_DIR, "puplogo.ico")

def create_window():
    left_frame = Tk()
    right_frame = Tk()

# WINDOW 
window = Tk()
window.title("Learning Management System")
window.iconbitmap(icon_path)
window.geometry("1200x800")

# FRAMES
left_frame = Frame(window, bg="maroon")
left_frame.pack(side="left", fill="both", expand=True)

right_frame = Frame(window, bg="#fdece6")
right_frame.pack(side="right", fill="both", expand=True)

# HELPERS 
def load(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size))

def txt(parent, text, x, y, **kw):
    Label(parent, text=text, bg=parent["bg"], **kw).place(x=x, y=y)

def placeholder(entry, text):
    entry.insert(0, text)
    entry.config(fg="gray")

    def focus_in(e):
        if entry.get() == text:
            entry.delete(0, END)
            entry.config(fg="black")

    def focus_out(e):
        if entry.get() == "":
            entry.insert(0, text)
            entry.config(fg="gray")

    entry.bind("<FocusIn>", focus_in)
    entry.bind("<FocusOut>", focus_out)

def put_img(parent, img, x, y):
    lbl = Label(parent, image=img, bg="maroon", bd=0)
    lbl.image = img
    lbl.place(x=x, y=y)

# BACKGROUND    
pup = Image.open("pupbg.ico").convert("RGBA").resize((800, 800))
alpha = pup.getchannel("A").point(lambda p: int(p * 0.20))
pup.putalpha(alpha)
pup_logo = ImageTk.PhotoImage(pup)

bg_logo = Label(left_frame, image=pup_logo, bg="maroon", bd=0)
bg_logo.image = pup_logo
bg_logo.place(relx=0.5, rely=0.5, anchor="center")
bg_logo.lower()

# LEFT CONTENT
put_img(left_frame, load("hatlogo.ico", (45, 45)), 60, 60)

txt(left_frame, "EduLearn", 110, 55,
    font=("Plus Jakarta Sans", 18, "bold"), fg="white")

txt(left_frame, "Learning Management System", 110, 90,
    font=("Inter", 11), fg="#FFFFF0")

txt(left_frame, "Learn.\nGrow.", 60, 130,
    font=("Plus Jakarta Sans", 40, "bold"), fg="white")

canvas = Canvas(left_frame, bg="maroon", highlightthickness=0, width=400, height=120)
canvas.place(x=60, y=250)
canvas.create_text(0, 30, text="Succeed.",
                   font=("Plus Jakarta Sans", 40, "bold"),
                   fill="#f7c948", anchor="w")
canvas.create_line(0, 70, 25, 70, fill="#f7c948", width=3)

txt(left_frame,
    "Your all-in-one learning platform.\nAccess courses, track progress,\nand achieve your goals anytime.",
    60, 340,
    font=("Inter", 14), fg="#FFFFF0")

# FEATURES
def feature(icon, title, desc, y):
    put_img(left_frame, load(icon, (45, 45)), 60, y)
    txt(left_frame, title, 110, y,
        font=("Plus Jakarta Sans", 14, "bold"), fg="#f8f8f8")
    txt(left_frame, desc, 110, y+25,
        font=("Inter", 11), fg="#FFFFF0")

feature("access.ico", "ACCESS QUALITY COURSES",
        "Explore thousands of courses", 430)

feature("track.ico", "TRACK YOUR PROGRESS",
        "Monitor learning achievements", 500)

feature("engage.ico", "ENGAGE & COLLABORATE",
        "Connect with peers and instructors", 570)

# RIGHT FRAME 
inner = Frame(right_frame, bg="white", width=400, height=600)
inner.place(relx=0.5, rely=0.5, anchor="center")
inner.pack_propagate(False)

def clear_inner():
    for w in inner.winfo_children():
        w.destroy()

# ROLE SELECTOR
def role_selector(parent, y):
    txt(parent, "I am a", 20, y, font=("Inter", 12))

    def role_box(x, name, icon):
        f = Frame(parent, bg="white",
                  width=150, height=100,
                  highlightbackground="#D3D3D3",
                  highlightthickness=1)
        f.place(x=x, y=y+30)

        img = load(icon, (40, 40))

        btn = Button(f, image=img, text=name,
                     compound="top",
                     bg="white", bd=0,
                     cursor="hand2")
        btn.image = img
        btn.place(relx=0.5, rely=0.5, anchor="center")

    role_box(35, "Student", "Student.ico")
    role_box(215, "Professor", "Professor.ico")

# FOOTER
def add_footer():
    footer = Label(right_frame,
        text="© 2026 EduLearn LMS. All rights reserved.",
        font=("Inter", 10),
        fg="gray",
        bg="#fdece6")
    footer.place(relx=0.5, rely=0.95, anchor="center")

# LOGIN
def login_screen():
    clear_inner()

    def forgot_password_screen():
        clear_inner()

        txt(inner, "Forgot Password", 20, 20,
            font=("Inter", 20), fg="black")

        txt(inner, "Reset your password", 20, 60,
            font=("Inter", 12), fg="#696969")

        txt(inner, "Email or Username", 20, 100,
            font=("Inter", 12))

        entry = Entry(inner)
        entry.place(x=30, y=125, width=340, height=40)


# FORGOT PASSWORD
        Button(
            inner,
            text="Send Reset Link",
            bg="maroon",
            fg="white",
            bd=0,
            font=("Inter", 12)
        ).place(x=30, y=190)

        Button(
            inner,
            text="← Back to Login",
            bg="white",
            fg="maroon",
            bd=0,
            command=login_screen
        ).place(x=30, y=250)

        add_footer()

    txt(inner, "Welcome Back Iskolar!", 20, 20,
        font=("Inter", 20), fg="black")

    txt(inner, "Sign in to continue", 20, 60,
        font=("Inter", 12), fg="#696969")

    txt(inner, "Username", 20, 100, font=("Inter", 12))

    f1 = Frame(inner, bg="#FAF9F6",
               highlightbackground="#D3D3D3",
               highlightthickness=1)
    f1.place(x=30, y=125, width=340, height=40)

    user = Entry(f1, bg="#FAF9F6", bd=0)
    user.place(x=10, y=7, width=320, height=25)
    placeholder(user, "Enter username")

    txt(inner, "Password", 20, 190, font=("Inter", 12))

    Button(
        inner,
        text="Forgot Password?",
        bg="white",
        fg="maroon",
        bd=0,
        font=("Inter", 12, "underline"),
        cursor="hand2",
        command=forgot_password_screen
    ).place(x=245, y=190)

    f2 = Frame(inner, bg="#FAF9F6",
               highlightbackground="#D3D3D3",
               highlightthickness=1)
    f2.place(x=30, y=220, width=340, height=40)

    pwd = Entry(f2, bg="#FAF9F6", bd=0, show="")
    pwd.place(x=10, y=7, width=320, height=25)
    placeholder(pwd, "Enter password")

    role_selector(inner, 300)

    Button(
        inner,
        text="Sign In →",
        bg="maroon",
        fg="white",
        bd=0,
        font=("Inter", 14),
        width=30
    ).place(x=32, y=460)

    Label(
        inner,
        text="Don't have an account?",
        bg="white",
        fg="gray",
        font=("Inter", 12)
    ).place(x=80, y=540)

    Button(
        inner,
        text="Sign Up",
        bg="white",
        fg="maroon",
        bd=0,
        font=("Inter", 12, "underline"),
        cursor="hand2",
        command=signup_screen
    ).place(x=245, y=538)

    add_footer()

# SIGNUP
def signup_screen():
    clear_inner()

    txt(inner, "Create Account", 20, 20,
        font=("Inter", 20), fg="black")

    txt(inner, "Sign up to start your learning journey", 20, 60,
        font=("Inter", 12), fg="#696969")

    def box(y, label, ph):
        txt(inner, label, 20, y, font=("Inter", 12))

        f = Frame(inner, bg="#FAF9F6",
                  highlightbackground="#D3D3D3",
                  highlightthickness=1)
        f.place(x=30, y=y+25, width=340, height=40)

        e = Entry(f, bg="#FAF9F6", bd=0)
        e.place(x=10, y=7, width=320, height=25)
        placeholder(e, ph)

    box(100, "Full Name", "Enter name")
    box(175, "Username", "Enter username")
    box(250, "Password", "Enter password")

    role_selector(inner, 340)

    Button(inner, text="Create Account →",
           bg="maroon", fg="white",
           bd=0, font=("Inter", 14),
           width=30).place(x=32, y=500)

    Label(inner, text="Already have an account?",
          bg="white", fg="gray",
          font=("Inter", 12)).place(x=70, y=560)

    Button(inner, text="Sign In",
           bg="white", fg="maroon",
           bd=0, font=("Inter", 12, "underline"),
           cursor="hand2",
           command=login_screen).place(x=250, y=558)

    add_footer()

# START 
main_home_window = window
login_screen()
window.mainloop()


