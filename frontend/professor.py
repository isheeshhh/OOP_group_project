from tkinter import *

# WINDOW
root = Tk()
root.title("Learning Management System Dashboard")
root.iconbitmap("puplogo.ico")
root.state("zoomed")
root.configure(bg="#f4e8e8")

# FUNCTIONS
def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()


# SIDEBAR
sidebar = Frame(root, width=300, bg="#7b1d2e")
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

# LOGO
try:
    logo = PhotoImage(
        file="C:\\Users\\E14 GEN 7 ULTRA 5\\OneDrive\\Desktop\\OOP FILES\\samples\\edulearn.png"
    )
    logo = logo.subsample(6, 6)
except:
    logo = None

logo_frame = Frame(sidebar, bg="#7b1d2e")
logo_frame.pack(anchor="w", pady=(20, 10), padx=20)

if logo:
    logo_label = Label(
        logo_frame,
        image=logo,
        bg="#7b1d2e"
    )
    logo_label.image = logo
    logo_label.pack(side="left")

text_logo = Frame(
    logo_frame,
    bg="#7b1d2e"
)
text_logo.pack(side="left", padx=10)

Label(
    text_logo,
    text="EduLearn",
    font=("Arial", 18, "bold"),
    fg="yellow",
    bg="#7b1d2e"
).pack(anchor="w")

Label(
    text_logo,
    text="Learning Management System",
    font=("Inter", 9),
    fg="white",
    bg="#7b1d2e"
).pack(anchor="w")

# RIGHT SIDE
right_frame = Frame(root, bg="#f4e8e8")
right_frame.pack(fill="both", expand=True)

# HEADER
header = Frame(right_frame, bg="#f4e8e8")
header.pack(fill="x", padx=20, pady=20)

text_frame = Frame(header, bg="#f4e8e8")
text_frame.pack(side="left")

Label(
    text_frame,
    text="Welcome back,",
    font=("Arial", 14),
    fg="Gray",
    bg="#f4e8e8"
).pack(anchor="w")

Label(
    text_frame,
    text="Prof. Eunice Blanco",
    font=("Arial", 20, "bold"),
    fg="Black",
    bg="#f4e8e8"
).pack(anchor="w")

# PROFILE
profile = Frame(
    header,
    width=200,
    height=50,
    bg="white"
)
profile.pack(side="right")
profile.pack_propagate(False)

Label(
    profile,
    text="EB",
    bg="#F5C842",
    fg="black",
    width=3,
    height=3
).pack(side="left", padx=10, pady=10)

info = Frame(profile, bg="white")
info.pack(side="left", pady=8)

Label(
    info,
    text="Prof. Eunice Blanco",
    bg="white",
    font=("Arial", 11, "bold")
).pack(anchor="w")

Label(
    info,
    text="Instructor",
    bg="white",
    fg="gray",
    font=("Arial", 9)
).pack(anchor="w")

# CONTENT FRAME
content_frame = Frame(
    right_frame,
    bg="#f4e8e8"
)

content_frame.pack(
    fill="both",
    expand=True
)

from tkinter import filedialog, Toplevel

# DASHBOARD PAGE
def show_dashboard():

    clear_content()

    cards_frame = Frame(
        content_frame,
        bg="#f4e8e8"
    )

    cards_frame.pack(
        fill="x",
        pady=(20, 20),
        padx=20
    )

    # DASHBOARD CARD
def show_dashboard():

    clear_content()

    cards_frame = Frame(
        content_frame,
        bg="#f4e8e8"
    )

    cards_frame.pack(
        fill="x",
        pady=(20, 20),
        padx=20
    )
    
    # DASHBOARD CARD
    def dashboard_card(parent, icon, title, value, bg_color):

        card = Frame(
            parent,
            bg=bg_color,
            width=1200,
            height=180
        )

        card.pack(side="left", padx=10)
        card.pack_propagate(False)

        Label(
            card,
            text=icon,
            font=("Arial", 22),
            bg=bg_color
        ).pack(anchor="w", padx=20, pady=(20, 10))

        Label(
            card,
            text=title,
            font=("Arial", 12),
            fg="#666666",
            bg=bg_color
        ).pack(anchor="w", padx=20)

        Label(
            card,
            text=value,
            font=("Arial", 28, "bold"),
            fg="#1d2235",
            bg=bg_color
        ).pack(anchor="w", padx=20, pady=(10, 0))

    dashboard_card(
        cards_frame,
        "📚",
        "Total Courses",
        "6",
        "#f2e6cf"
    )

    # QUICK ACTIONS TITLE
    Label(
        content_frame,
        text="Quick Actions",
        font=("Arial", 16, "bold"),
        bg="#f4e8e8",
        fg="#1d2235"
    ).pack(
        anchor="w",
        padx=40,
        pady=(10, 10)
    )

    quick_frame = Frame(
        content_frame,
        bg="#f4e8e8"
    )

    quick_frame.pack(
        fill="x",
        padx=20
    )

    quick_frame.grid_columnconfigure(0, weight=1)
    quick_frame.grid_columnconfigure(1, weight=1)

    # MANAGE COURSES POPUP
    def open_manage_courses():

        popup = Toplevel()
        popup.title("Manage Courses")
        popup.geometry("650x700")
        popup.configure(bg="white")

        Label(
            popup,
            text="Manage Courses",
            font=("Poppins", 18, "bold"),
            bg="white"
        ).pack(pady=15)

        # TOP ACTION BUTTONS
        action_frame = Frame(
            popup,
            bg="white"
        )
        action_frame.pack(fill="x", padx=20)

        Button(
            action_frame,
            text="➕ Add Course",
            bg="#7b1d2e",
            fg="white",
            relief="flat",
            font=("Poppins", 10, "bold")
        ).pack(side="left", fill="x", expand=True, padx=5, ipady=8)

        Button(
            action_frame,
            text="✏️ Edit Course",
            bg="#d9d9d9",
            relief="flat",
            font=("Poppins", 10)
        ).pack(side="left", fill="x", expand=True, padx=5, ipady=8)

        Button(
            action_frame,
            text="🗑 Delete Course",
            bg="#d9d9d9",
            relief="flat",
            font=("Poppins", 10)
        ).pack(side="left", fill="x", expand=True, padx=5, ipady=8)

        # COURSE NAME
        Label(
            popup,
            text="Course Name",
            bg="white",
            font=("Poppins", 10)
        ).pack(anchor="w", padx=20, pady=(20, 5))

        course_name = Entry(
            popup,
            font=("Poppins", 11)
        )
        course_name.pack(
            fill="x",
            padx=20,
            ipady=8
        )

        # COURSE DESCRIPTION
        Label(
            popup,
            text="Course Description",
            bg="white",
            font=("Poppins", 10)
        ).pack(anchor="w", padx=20, pady=(15, 5))

        course_desc = Text(
            popup,
            height=8,
            font=("Poppins", 11)
        )
        course_desc.pack(
            fill="both",
            expand=True,
            padx=20
        )

        file_data = {"path": None}

        def upload_pdf():
            path = filedialog.askopenfilename(
                filetypes=[("PDF files", "*.pdf")]
            )

            if path:
                file_data["path"] = path
                upload_label.config(
                    text=path.split("/")[-1]
                )

        Label(
            popup,
            text="Course Material (PDF)",
            bg="white",
            font=("Poppins", 10)
        ).pack(anchor="w", padx=20, pady=(15, 5))

        Button(
            popup,
            text="Click to Upload PDF",
            command=upload_pdf
        ).pack(pady=5)

        upload_label = Label(
            popup,
            text="No file selected",
            fg="gray",
            bg="white"
        )
        upload_label.pack()

        def save_course():
            print("Course Name:", course_name.get())
            print("Description:", course_desc.get("1.0", END))
            print("PDF:", file_data["path"])

        # BOTTOM BUTTONS
        button_frame = Frame(
            popup,
            bg="white"
        )
        button_frame.pack(
            fill="x",
            padx=20,
            pady=20
        )

        Button(
            button_frame,
            text="Cancel",
            command=popup.destroy,
            bg="#d9d9d9",
            relief="flat",
            font=("Poppins", 10)
        ).pack(
            side="left",
            ipadx=20,
            ipady=10
        )

        Button(
            button_frame,
            text="SAVE COURSE",
            bg="#7b1d2e",
            fg="white",
            relief="flat",
            font=("Poppins", 10, "bold"),
            command=save_course
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(10, 0),
            ipady=10
        )

    # MANAGING FILES POPUP
    def open_manage_files():

        popup = Toplevel()
        popup.title("Managing Files")
        popup.geometry("500x350")
        popup.configure(bg="white")

        Label(
            popup,
            text="Managing Files",
            font=("Poppins", 18, "bold"),
            bg="white"
        ).pack(pady=20)

        Button(
            popup,
            text="⬆ Upload File",
            bg="#7b1d2e",
            fg="white",
            relief="flat",
            font=("Poppins", 10, "bold")
        ).pack(
            fill="x",
            padx=30,
            pady=10,
            ipady=10
        )

        Button(
            popup,
            text="✏️ Edit File",
            bg="#d9d9d9",
            relief="flat",
            font=("Poppins", 10)
        ).pack(
            fill="x",
            padx=30,
            pady=10,
            ipady=10
        )

        Button(
            popup,
            text="Close",
            command=popup.destroy
        ).pack(pady=20)

    # QUICK CARD
    def quick_card(parent, col, icon, title, desc, command=None):

        card = Frame(
            parent,
            bg="white",
            height=120,
            bd=0,
            relief="ridge"
        )

        card.grid(
            row=0,
            column=col,
            sticky="nsew",
            padx=10,
            pady=5
        )

        def on_click(event):
            if command:
                command()

        card.bind("<Button-1>", on_click)

        Label(
            card,
            text=icon,
            font=("Arial", 18),
            bg="white"
        ).pack(anchor="w", padx=15, pady=(15, 5))

        Label(
            card,
            text=title,
            font=("Arial", 12, "bold"),
            bg="white"
        ).pack(anchor="w", padx=15)

        Label(
            card,
            text=desc,
            font=("Arial", 9),
            fg="gray",
            bg="white"
        ).pack(anchor="w", padx=15, pady=(2, 10))

    quick_card(
        quick_frame,
        0,
        "📖",
        "Manage Courses",
        "Add, edit, or delete your courses",
        command=open_manage_courses
    )

    quick_card(
        quick_frame,
        1,
        "📁",
        "Managing Files",
        "Upload and edit course files",
        command=open_manage_files
    )

    # BOTTOM PANEL
    bottom_panel = Frame(
        content_frame,
        bg="white",
        height=200
    )

    bottom_panel.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=30
    )
    Label(
        bottom_panel,
        text="Select a section from the sidebar to get started",
        font=("Arial", 12),
        fg="gray",
        bg="white"
    ).pack(expand=True)

# COURSES PAGE
def create_course_card(
        parent,
        title,
        description,
):

    card = Frame(
        parent,
        bg="white",
        height=140,
        bd=0
    )

    card.pack(
        fill="x",
        pady=10
    )

    card.pack_propagate(False)

    # TOP

    top = Frame(
        card,
        bg="white"
    )

    top.pack(
        fill="x",
        padx=25,
        pady=(20, 0)
    )

    Label(
        top,
        text=title,
        font=("Arial", 18, "bold"),
        bg="white",
        fg="#1d2235"
    ).pack(side="left")

    actions = Frame(
        top,
        bg="white"
    )

    actions.pack(side="right")

    Button(
        actions,
        text="✎",
        font=("Arial", 12),
        bg="#f9f0f1",
        fg="#7b1d2e",
        relief="flat",
        width=3,
        cursor="hand2"
    ).pack(
        side="left",
        padx=5
    )

    Button(
        actions,
        text="🗑",
        font=("Arial", 12),
        bg="#f9f0f1",
        fg="#d9534f",
        relief="flat",
        width=3,
        cursor="hand2"
    ).pack(side="left")

    # DESCRIPTION

    Label(
        card,
        text=description,
        font=("Arial", 11),
        fg="gray",
        bg="white"
    ).pack(
        anchor="w",
        padx=25,
        pady=(10, 0)
    )

    # DETAILS
    details = Frame(
        card,
        bg="white"
    )

    details.pack(
        anchor="w",
        padx=25,
        pady=(18, 0)
    )

def show_courses():

    clear_content()

    main_content = Frame(
        content_frame,
        bg="#f4e8e8"
    )

    main_content.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=(0, 20)
    )

    page_header = Frame(
        main_content,
        bg="#f4e8e8"
    )

    page_header.pack(
        fill="x",
        pady=(20, 20)
    )

    title_frame = Frame(
        page_header,
        bg="#f4e8e8"
    )

    title_frame.pack(side="left")

    Label(
        title_frame,
        text="Course Management",
        font=("Arial", 24, "bold"),
        bg="#f4e8e8",
        fg="#1d2235"
    ).pack(anchor="w")

    Label(
        title_frame,
        text="Create, edit, and manage your courses",
        font=("Arial", 11),
        fg="gray",
        bg="#f4e8e8"
    ).pack(
        anchor="w",
        pady=(5, 0)
    )

    create_course_card(
        main_content,
        "Object Oriented Programming",
        "Learn the basics of HTML, CSS, JavaScript, and modern web development practices.",
        
    )

    create_course_card(
        main_content,
        "Computer Hardware Fundamentals",
        "Master the fundamentals of user interface and user experience design.",
        
    )

# SIDEBAR BUTTONS
menu_items = [
    ("🏠   Dashboard", show_dashboard),
    ("📖   My Courses", show_courses),
]

for text, cmd in menu_items:

    Button(
        sidebar,
        text=text,
        font=("Inter", 14),
        fg="White",
        bg="#7b1d2e",
        activebackground="#F5C842",
        relief="flat",
        width=60,
        height=2,
        anchor="w",
        padx=30,
        command=cmd
    ).pack(
        anchor="w",
        pady=5,
        padx=20
    )

from tkinter import messagebox

def logout():

    confirm = messagebox.askyesno(
        "Logout",
        "Are you sure you want to logout?"
    )

    if confirm:
        root.destroy() 
          # closes the application

Button(
    sidebar,
    text="→   Logout",
    font=("Inter", 14),
    fg="White",
    bg="#7b1d2e",
    activebackground="#F5C842",
    relief="flat",
    width=60,
    height=2,
    anchor="w",
    padx=30,
    command=logout
).pack(
    anchor="w",
    pady=(10, 0),
    padx=20
)

# START PAGE
show_dashboard()

root.mainloop()