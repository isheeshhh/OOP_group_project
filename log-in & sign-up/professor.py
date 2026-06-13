import os
import subprocess
import sys
from tkinter import *
from tkinter import filedialog, Toplevel, messagebox

# Store the script directory path used for asset resolution.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(SCRIPT_DIR, "assets")

def asset(name):
    return os.path.join(ASSET_DIR, name)

# Hardcoded professor name and ID used in place of session data.
prof_name = "Prof. Professor"
professor_id = "professor"

# In-memory course list used instead of loading from a JSON database.
courses = []

# WINDOW
root = Tk()
root.title("Learning Management System Dashboard")
try:
    root.iconbitmap(asset("puplogo.ico"))
except TclError:
    pass
root.state("zoomed")
root.configure(bg="#fdece6")

# FUNCTIONS
def clear_content():
    # Clears the main content area before loading another page.
    for widget in content_frame.winfo_children():
        widget.destroy()

# SIDEBAR
sidebar = Frame(root, width=300, bg="maroon")
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

# LOGO
try:
    logo = PhotoImage(file=asset("edulearn.png")).subsample(6, 6)
except TclError:
    logo = None

logo_frame = Frame(sidebar, bg="maroon")
logo_frame.pack(anchor="w", pady=(20, 10), padx=20)

if logo:
    logo_label = Label(logo_frame, image=logo, bg="maroon")
    logo_label.image = logo
    logo_label.pack(side="left")

text_logo = Frame(logo_frame, bg="maroon")
text_logo.pack(side="left", padx=10)

Label(
    text_logo,
    text="EduLearn",
    font=("Plus Jakarta Sans", 18, "bold"),
    fg="#f7c948",
    bg="maroon"
).pack(anchor="w")

Label(
    text_logo,
    text="Learning Management System",
    font=("Inter", 9),
    fg="#FFFFF0",
    bg="maroon"
).pack(anchor="w")

# RIGHT SIDE
right_frame = Frame(root, bg="#fdece6")
right_frame.pack(fill="both", expand=True)

# HEADER
header = Frame(right_frame, bg="#fdece6")
header.pack(fill="x", padx=20, pady=20)

text_frame = Frame(header, bg="#fdece6")
text_frame.pack(side="left")

Label(
    text_frame,
    text="Welcome back,",
    font=("Inter", 14),
    fg="Gray",
    bg="#fdece6"
).pack(anchor="w")

Label(
    text_frame,
    text=prof_name,
    font=("Plus Jakarta Sans", 20, "bold"),
    fg="Black",
    bg="#fdece6"
).pack(anchor="w")

# PROFILE
profile = Frame(header, width=200, height=50, bg="white", highlightbackground="#D3D3D3", highlightthickness=1)
profile.pack(side="right")
profile.pack_propagate(False)

Label(
    profile,
    text="EB",
    bg="#f7c948",
    fg="black",
    width=3,
    height=3,
    font=("Inter", 9, "bold")
).pack(side="left", padx=10, pady=10)

info = Frame(profile, bg="white")
info.pack(side="left", pady=8)

Label(
    info,
    text=prof_name,
    bg="white",
    font=("Plus Jakarta Sans", 11, "bold")
).pack(anchor="w")

Label(
    info,
    text="Instructor",
    bg="white",
    fg="gray",
    font=("Inter", 9)
).pack(anchor="w")

# CONTENT FRAME
content_frame = Frame(right_frame, bg="#fdece6")
content_frame.pack(fill="both", expand=True)

# --- GLOBAL POPUP FUNCTIONS ---

def open_manage_courses(edit_idx=None):
    # Opens a popup form for adding or editing course information.
    popup = Toplevel(root)
    popup.title("Manage Course")
    popup.geometry("650x700")
    popup.configure(bg="white")

    # Grab focus so user cannot interact with main window behind it.
    popup.grab_set()

    is_edit = edit_idx is not None
    title_text = "Edit Course" if is_edit else "Add New Course"

    Label(
        popup,
        text=title_text,
        font=("Plus Jakarta Sans", 18, "bold"),
        bg="white"
    ).pack(pady=15)

    # COURSE NAME
    Label(popup, text="Course Name", bg="white", font=("Inter", 10)).pack(anchor="w", padx=20, pady=(20, 5))
    course_name = Entry(popup, font=("Inter", 11), bg="#FAF9F6", relief="flat")
    course_name.pack(fill="x", padx=20, ipady=8)

    # COURSE DESCRIPTION
    Label(popup, text="Course Description", bg="white", font=("Inter", 10)).pack(anchor="w", padx=20, pady=(15, 5))
    course_desc = Text(popup, height=8, font=("Inter", 11), bg="#FAF9F6", relief="flat")
    course_desc.pack(fill="both", expand=True, padx=20)

    file_data = {"path": None}

    # Placeholder student list used in place of loading from accounts file.
    student_accounts = []

    Label(popup, text="Included Students", bg="white", font=("Inter", 10)).pack(anchor="w", padx=20, pady=(15, 5))
    student_listbox = Listbox(popup, selectmode=MULTIPLE, height=5, font=("Inter", 10), bg="#FAF9F6", relief="flat")
    student_listbox.pack(fill="x", padx=20)
    if student_accounts:
        for student in student_accounts:
            student_listbox.insert(END, student.get("fullname", "Student"))
    else:
        student_listbox.insert(END, "No registered student accounts yet")
        student_listbox.config(state=DISABLED)

    # Pre-fill fields if editing an existing course.
    if is_edit:
        c_data = courses[edit_idx]
        course_name.insert(0, c_data["title"])
        course_desc.insert("1.0", c_data["description"])
        if c_data.get("file_path"):
            file_data["path"] = c_data["file_path"]

    def upload_pdf():
        path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if path:
            file_data["path"] = path
            upload_label.config(text=os.path.basename(path))

    Label(popup, text="Course Material (PDF)", bg="white", font=("Inter", 10)).pack(anchor="w", padx=20, pady=(15, 5))
    Button(popup, text="Click to Upload PDF", bg="#FAF9F6", relief="flat", font=("Inter", 10), command=upload_pdf).pack(pady=5)

    display_file = os.path.basename(file_data["path"]) if file_data["path"] else "No file selected"
    upload_label = Label(popup, text=display_file, fg="gray", bg="white")
    upload_label.pack()

    def save_course():
        title = course_name.get().strip()
        desc = course_desc.get("1.0", END).strip()
        f_path = file_data["path"]
        f_name = os.path.basename(f_path) if f_path else "No file attached"

        if not title:
            messagebox.showwarning("Validation Error", "Course Name is required.", parent=popup)
            return

        if is_edit:
            # Update existing course in the in-memory list.
            courses[edit_idx]["title"] = title
            courses[edit_idx]["description"] = desc
            courses[edit_idx]["students"] = []
            courses[edit_idx]["file_name"] = f_name
            courses[edit_idx]["file_path"] = f_path
        else:
            # Add a new course entry to the in-memory list.
            new_course = {
                "title": title,
                "description": desc,
                "students": [],
                "file_name": f_name,
                "file_path": f_path,
                "date": "N/A"
            }
            courses.append(new_course)

        popup.destroy()
        show_courses() # Refresh view to show changes

    # BOTTOM BUTTONS
    button_frame = Frame(popup, bg="white")
    button_frame.pack(fill="x", padx=20, pady=20)

    Button(button_frame, text="Cancel", command=popup.destroy, bg="#FAF9F6", relief="flat", font=("Inter", 10)).pack(side="left", ipadx=20, ipady=10)
    Button(button_frame, text="SAVE COURSE", bg="maroon", fg="white", relief="flat", font=("Inter", 10, "bold"), command=save_course).pack(side="left", fill="x", expand=True, padx=(10, 0), ipady=10)

def open_manage_files():
    popup = Toplevel(root)
    popup.title("Managing Files")
    popup.geometry("650x450")
    popup.configure(bg="white")
    popup.grab_set()

    Label(popup, text="Managing Files", font=("Plus Jakarta Sans", 18, "bold"), bg="white").pack(pady=20)

    if not courses:
        Label(popup, text="Create a course first before managing files.", font=("Inter", 11), fg="gray", bg="white").pack(pady=60)
        Button(popup, text="Close", relief="flat", bg="#FAF9F6", command=popup.destroy).pack(pady=20)
        return

    body = Frame(popup, bg="white")
    body.pack(fill="both", expand=True, padx=30)

    course_list = Listbox(body, height=10, font=("Inter", 11), bg="#FAF9F6", relief="flat")
    course_list.pack(side="left", fill="both", expand=True, padx=(0, 15))

    detail = Frame(body, bg="white", width=260)
    detail.pack(side="right", fill="y")
    detail.pack_propagate(False)

    selected_title = Label(detail, text="", font=("Plus Jakarta Sans", 12, "bold"), bg="white", wraplength=240, justify="left")
    selected_title.pack(anchor="w", pady=(5, 10))
    selected_file = Label(detail, text="", font=("Inter", 10), fg="gray", bg="white", wraplength=240, justify="left")
    selected_file.pack(anchor="w", pady=(0, 20))

    def refresh_list():
        course_list.delete(0, END)
        for course in courses:
            file_name = course.get("file_name") or "No file attached"
            course_list.insert(END, f"{course.get('title', 'Untitled Course')} - {file_name}")
        if courses:
            course_list.selection_set(0)
            show_selected_file()

    def get_selected_index():
        selected = course_list.curselection()
        if not selected:
            messagebox.showwarning("No Course Selected", "Please select a course first.", parent=popup)
            return None
        return selected[0]

    def show_selected_file(_event=None):
        index = get_selected_index()
        if index is None:
            return
        course = courses[index]
        selected_title.config(text=course.get("title", "Untitled Course"))
        selected_file.config(text="File: " + (course.get("file_name") or "No file attached"))

    def upload_file():
        index = get_selected_index()
        if index is None:
            return
        path = filedialog.askopenfilename(
            title="Select Course File",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if not path:
            return
        # Update the in-memory course entry with the new file path.
        courses[index]["file_path"] = path
        courses[index]["file_name"] = os.path.basename(path)
        refresh_list()
        course_list.selection_clear(0, END)
        course_list.selection_set(index)
        show_selected_file()
        show_courses()

    def remove_file():
        index = get_selected_index()
        if index is None:
            return
        # Clear the file path from the in-memory course entry.
        courses[index]["file_path"] = None
        courses[index]["file_name"] = "No file attached"
        refresh_list()
        course_list.selection_clear(0, END)
        course_list.selection_set(index)
        show_selected_file()
        show_courses()

    def open_file():
        index = get_selected_index()
        if index is None:
            return
        path = courses[index].get("file_path")
        if not path or not os.path.exists(path):
            messagebox.showwarning("File Not Found", "This course does not have a valid attached file.", parent=popup)
            return
        if sys.platform.startswith("win"):
            os.startfile(path)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

    Button(detail, text="Upload / Replace File", bg="maroon", fg="white", relief="flat", font=("Inter", 10, "bold"), command=upload_file).pack(fill="x", pady=6, ipady=8)
    Button(detail, text="Open File", bg="#FAF9F6", relief="flat", font=("Inter", 10), command=open_file).pack(fill="x", pady=6, ipady=8)
    Button(detail, text="Remove File", bg="#FAF9F6", fg="red", relief="flat", font=("Inter", 10), command=remove_file).pack(fill="x", pady=6, ipady=8)
    Button(popup, text="Close", relief="flat", bg="#FAF9F6", command=popup.destroy).pack(pady=20)

    course_list.bind("<<ListboxSelect>>", show_selected_file)
    refresh_list()


# --- DASHBOARD PAGE ---
def show_dashboard():
    clear_content()

    cards_frame = Frame(content_frame, bg="#fdece6")
    cards_frame.pack(fill="x", pady=(20, 20), padx=20)

    # DASHBOARD CARD
    def dashboard_card(parent, icon, title, value, bg_color):
        card = Frame(parent, bg=bg_color, width=1200, height=180, highlightbackground="#D3D3D3", highlightthickness=1)
        card.pack(side="left", padx=10)
        card.pack_propagate(False)

        Label(card, text=icon, font=("Inter", 22), bg=bg_color).pack(anchor="w", padx=20, pady=(20, 10))
        Label(card, text=title, font=("Inter", 12), fg="#696969", bg=bg_color).pack(anchor="w", padx=20)
        Label(card, text=value, font=("Plus Jakarta Sans", 28, "bold"), fg="black", bg=bg_color).pack(anchor="w", padx=20, pady=(10, 0))

    dashboard_card(cards_frame, "📚", "Total Courses", str(len(courses)), "white")

    # QUICK ACTIONS TITLE
    Label(
        content_frame,
        text="Quick Actions",
        font=("Plus Jakarta Sans", 16, "bold"),
        bg="#fdece6",
        fg="black"
    ).pack(anchor="w", padx=40, pady=(10, 10))

    quick_frame = Frame(content_frame, bg="#fdece6")
    quick_frame.pack(fill="x", padx=20)
    quick_frame.grid_columnconfigure(0, weight=1)
    quick_frame.grid_columnconfigure(1, weight=1)

    # Creates a clickable quick-action card on the dashboard.
    def quick_card(parent, col, icon, title, desc, command=None):
        card = Frame(parent, bg="white", height=120, highlightbackground="#D3D3D3", highlightthickness=1, cursor="hand2")
        card.grid(row=0, column=col, sticky="nsew", padx=10, pady=5)

        def on_click(event):
            if command:
                command()

        card.bind("<Button-1>", on_click)
        # Bind children too so clicks register everywhere on the card.
        for child in card.winfo_children():
            child.bind("<Button-1>", on_click)

        Label(card, text=icon, font=("Inter", 18), bg="white").pack(anchor="w", padx=15, pady=(15, 5))
        Label(card, text=title, font=("Plus Jakarta Sans", 12, "bold"), bg="white").pack(anchor="w", padx=15)
        Label(card, text=desc, font=("Inter", 9), fg="#696969", bg="white").pack(anchor="w", padx=15, pady=(2, 10))

    quick_card(quick_frame, 0, "📖", "Manage Courses", "Add a new course", command=lambda: open_manage_courses())
    quick_card(quick_frame, 1, "📁", "Managing Files", "Upload and edit course files", command=open_manage_files)

    # BOTTOM PANEL
    bottom_panel = Frame(content_frame, bg="white", height=200, highlightbackground="#D3D3D3", highlightthickness=1)
    bottom_panel.pack(fill="both", expand=True, padx=30, pady=30)
    Label(bottom_panel, text="Select a section from the sidebar to get started", font=("Inter", 12), fg="gray", bg="white").pack(expand=True)


# --- COURSE MANAGEMENT PAGE ---

def create_course_card(parent, idx, title, description, students, file_name, date):
    # Creates a course card shown on the Course Management page.
    card = Frame(parent, bg="white", height=140, highlightbackground="#D3D3D3", highlightthickness=1)
    card.pack(fill="x", pady=10)
    card.pack_propagate(False)

    # TOP
    top = Frame(card, bg="white")
    top.pack(fill="x", padx=25, pady=(20, 0))

    Label(top, text=title, font=("Plus Jakarta Sans", 18, "bold"), bg="white", fg="black").pack(side="left")

    actions = Frame(top, bg="white")
    actions.pack(side="right")

    def edit_course():
        open_manage_courses(edit_idx=idx)

    def delete_course():
        if messagebox.askyesno("Delete Course", f"Are you sure you want to delete '{title}'?"):
            courses.pop(idx)
            show_courses() # Refresh view

    Button(actions, text="✎", font=("Inter", 12), bg="#FAF9F6", fg="maroon", relief="flat", width=3, cursor="hand2", command=edit_course).pack(side="left", padx=5)
    Button(actions, text="🗑️", font=("Inter", 12), bg="#FAF9F6", fg="red", relief="flat", width=3, cursor="hand2", command=delete_course).pack(side="left")

    # DESCRIPTION
    Label(card, text=description, font=("Inter", 11), fg="gray", bg="white").pack(anchor="w", padx=25, pady=(10, 0))

    # DETAILS
    details = Frame(card, bg="white")
    details.pack(anchor="w", padx=25, pady=(18, 0))

    Label(details, text="Enrolled:", font=("Inter", 11), fg="gray", bg="white").pack(side="left")
    student_count = len(students) if isinstance(students, list) else int(students or 0)
    Label(details, text=f" {student_count} students", font=("Inter", 11, "bold"), bg="white").pack(side="left")
    Label(details, text=f"    📄 {file_name}", font=("Inter", 11), fg="gray", bg="white").pack(side="left")
    Label(details, text=f"    Created: {date}", font=("Inter", 11), fg="#444", bg="white").pack(side="left")

def show_courses():
    clear_content()

    main_content = Frame(content_frame, bg="#fdece6")
    main_content.pack(fill="both", expand=True, padx=25, pady=(0, 20))

    page_header = Frame(main_content, bg="#fdece6")
    page_header.pack(fill="x", pady=(20, 20))

    title_frame = Frame(page_header, bg="#fdece6")
    title_frame.pack(side="left")

    Label(title_frame, text="Course Management", font=("Plus Jakarta Sans", 24, "bold"), bg="#fdece6", fg="black").pack(anchor="w")
    Label(title_frame, text="Create, edit, and manage your courses", font=("Inter", 11), fg="gray", bg="#fdece6").pack(anchor="w", pady=(5, 0))

    # Right align an "Add Course" button at the top of the course list.
    Button(page_header, text="➕ Add Course", bg="maroon", fg="white", font=("Inter", 10, "bold"), relief="flat", padx=15, pady=8, cursor="hand2", command=lambda: open_manage_courses()).pack(side="right")

    # Render courses dynamically.
    if not courses:
        Label(main_content, text="No courses available. Click 'Add Course' to create one.", font=("Inter", 12), fg="gray", bg="#fdece6").pack(pady=50)
    else:
        for idx, course in enumerate(courses):
            create_course_card(
                parent=main_content,
                idx=idx,
                title=course.get("title", "Untitled Course"),
                description=course.get("description", ""),
                students=course.get("students", []),
                file_name=course.get("file_name", "No file attached"),
                date=course.get("date", "")
            )

# SIDEBAR BUTTONS
menu_items = [
    ("🏠    Dashboard", show_dashboard),
    ("📖    My Courses", show_courses),
]

for text, cmd in menu_items:
    Button(
        sidebar,
        text=text,
        font=("Inter", 14),
        fg="white",
        bg="maroon",
        activebackground="#f7c948",
        relief="flat",
        width=60,
        height=2,
        anchor="w",
        padx=30,
        cursor="hand2",
        command=cmd
    ).pack(anchor="w", pady=5, padx=20)

# Confirms and closes the professor dashboard when logging out.
def logout():
    confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if confirm:
        root.destroy() # Closes the application

Button(
    sidebar,
    text="→    Logout",
    font=("Inter", 14),
    fg="white",
    bg="maroon",
    activebackground="#f7c948",
    relief="flat",
    width=60,
    height=2,
    anchor="w",
    padx=30,
    cursor="hand2",
    command=logout
).pack(anchor="w", pady=(10, 0), padx=20)

# START PAGE
show_dashboard()

root.mainloop()