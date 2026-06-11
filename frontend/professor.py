import os
from tkinter import *
from tkinter import filedialog, Toplevel, messagebox
from course_management import course as course


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(BASE_DIR, "puplogo.ico")
# WINDOW
root = Tk()
root.title("Learning Management System Dashboard")
root.iconbitmap(icon_path)
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

    # COURSE NAME
    Label(
        popup,
        text="Course Name",
        bg="white",
        font=("Poppins", 10)
    ).pack(anchor="w", padx=20, pady=(20, 5))

    ent_name = Entry(
        popup,
        font=("Poppins", 11)
    )
    ent_name.pack(
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

    ent_desc = Text(
        popup,
        height=8,
        font=("Poppins", 11)
    )
    ent_desc.pack(
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
        name = ent_name.get().strip()
        desc = ent_desc.get("1.0", END).strip()

        try:
            course.create_course(name, desc)
            
            messagebox.showinfo("Success", "Course successfully saved to database!", parent=popup)
            popup.destroy()
            
            show_courses()
            
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=popup)
        
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

def open_edit_course(course_item):

    original_name = course_item["course_name"]

    popup = Toplevel()
    popup.title("Edit Course")
    popup.geometry("650x700")
    popup.configure(bg="white")

    Label(
        popup,
        text="Edit Course",
        font=("Poppins", 18, "bold"),
        bg="white"
    ).pack(pady=15)

    Label(popup, text="Course Name", bg="white", font=("Poppins", 10)).pack(anchor="w", padx=20, pady=(20, 5))
    ent_name = Entry(popup, font=("Poppins", 11))
    ent_name.pack(fill="x", padx=20, ipady=8)
    
    ent_name.insert(0, original_name)  

    Label(popup, text="Course Description", bg="white", font=("Poppins", 10)).pack(anchor="w", padx=20, pady=(15, 5))
    ent_desc = Text(popup, height=8, font=("Poppins", 11))
    ent_desc.pack(fill="both", expand=True, padx=20)
    
    ent_desc.insert("1.0", course_item["course_description"])

    def save_changes():
        new_name = ent_name.get().strip()
        new_desc = ent_desc.get("1.0", END).strip()

        if not new_name:
            messagebox.showerror("Validation Error", "Course Name must not be left blank.", parent=popup)
            return

        try:
            
            all_courses = course.load_courses()
            
            if new_name != original_name:
                for c in all_courses:
                    if c["course_name"] == new_name:
                        messagebox.showerror("Validation Error", f"Course: {new_name} already exists.", parent=popup)
                        return

            for c in all_courses:
                if c["course_name"] == original_name:
                    c["course_name"] = new_name          
                    c["course_description"] = new_desc   
            
            course.save_courses(all_courses)
            
            messagebox.showinfo("Success", "Course changes successfully saved!", parent=popup)
            popup.destroy()
            
            show_courses()
            
        except Exception as e:
            messagebox.showerror("Database Error", f"An unexpected error occurred: {e}", parent=popup)

    button_frame = Frame(popup, bg="white")
    button_frame.pack(fill="x", padx=20, pady=20)

    Button(
        button_frame, text="Cancel", command=popup.destroy,
        bg="#d9d9d9", relief="flat", font=("Poppins", 10)
    ).pack(side="left", ipadx=20, ipady=10)

    Button(
        button_frame, 
        text="SAVE CHANGES",
        bg="#7b1d2e", fg="white", relief="flat",
        font=("Poppins", 10, "bold"), command=save_changes
    ).pack(side="left", fill="x", expand=True, padx=(10, 0), ipady=10)

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
    def dashboard_card(parent, icon, title, value, bg_color):

        card = Frame(
            parent,
            bg=bg_color,
            width=1200,
            height=180
        )

        card.pack(side="left", padx=10, expand=True, fill="x")
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

    try:
        total_courses = len(course.load_courses())
    except Exception:
        total_courses = 0

    dashboard_card(
        cards_frame,
        "📚",
        "Total Courses",
        str(total_courses),
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
        command=show_courses
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


# CARD TEMPLATE CREATOR
def create_course_card(parent, title, description, delete_btn, edit_btn):

    card = Frame(
        parent,
        bg="white",
        bd=0
    )
    card.pack(
        fill="x",
        pady=10,
    )

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
        cursor="hand2",
        command=edit_btn
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
        cursor="hand2",
        command=delete_btn
    ).pack(side="left")

    # DESCRIPTION
    Label(
        card,
        text=description,
        font=("Arial", 11),
        fg="gray",
        bg="white",
        wraplength=800,
        justify="left",
        anchor="w"
    ).pack(
        fill="x",
        padx=25,
        pady=(5, 20),
    )

# COURSES MANAGEMENT VIEW
def show_courses():
    clear_content()

    def delete_course(course_name):
        confirm = messagebox.askyesno(
            "Delete Course",
            f"Are you sure you want to delete '{course_name}'"
        )

        if confirm:
            try:
                all_courses = course.load_courses()
                updated_course = [] 
                for c in all_courses:
                    if c['course_name'] != course_name:
                        updated_course.append(c)
                course.save_courses(updated_course)
                messagebox.showinfo("Succes", f"'{course_name}' has been deleted.")
                show_courses()
            except Exception as e:
                messagebox.showerror("Error", f"Couldn't delete course: {e}")   
    
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

    Button(
        page_header,
        text="➕ Add Course",
        bg="#7b1d2e",
        fg="white",
        relief="flat",
        font=("Poppins", 10, "bold"),
        command=open_manage_courses
    ).pack(side="right", fill="x", padx=5, ipady=8)

    try:
        all_courses = course.load_courses()
        for course_item in all_courses:
            create_course_card(
                main_content,
                course_item["course_name"],       
                course_item["course_description"],
                delete_btn=lambda name=course_item["course_name"]: delete_course(name),
                edit_btn=lambda item=course_item: open_edit_course(item)
            )
    except Exception as e:
        messagebox.showerror("Error", e)
   
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

def logout():
    confirm = messagebox.askyesno(
        "Logout",
        "Are you sure you want to logout?"
    )
    if confirm:
       root.destroy()
       import homepage
        


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