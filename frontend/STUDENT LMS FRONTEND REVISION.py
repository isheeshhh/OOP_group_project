import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tkinter import *
from tkinter import messagebox
from pathlib import Path
from course_management import course


root = Tk()
root.title("Learning Management System Dashboard")
root.state("zoomed")
root.configure(bg="#f4e8e8")


############# SIDEBAR ############
sidebar = Frame(root, width=300, bg="#7b1d2e")
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

# LOGO
BASE_DIR = Path(__file__).resolve().parent

logo = PhotoImage(file=BASE_DIR / "edulearn.png")
logo = logo.subsample(6, 6)

logo_frame = Frame(sidebar, bg="#7b1d2e")
logo_frame.pack(anchor="w", pady=(20, 10), padx=20)

logo_label = Label(logo_frame, image=logo, bg="#7b1d2e")
logo_label.image = logo
logo_label.pack(side="left")

text_logo = Frame(logo_frame, bg="#7b1d2e")
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

def create_scrollable_page(parent):

    container = Frame(parent, bg="#f4e8e8")
    container.pack(fill="both", expand=True)

    canvas = Canvas(
        container,
        bg="#f4e8e8",
        highlightthickness=0
    )
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = Scrollbar(
        container,
        orient="vertical",
        command=canvas.yview
    )
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    scrollable_frame = Frame(canvas, bg="#f4e8e8")

    window_id = canvas.create_window(
        (0, 0),
        window=scrollable_frame,
        anchor="nw"
    )

    canvas.bind(
        "<Configure>",
        lambda e: canvas.itemconfig(
            window_id,
            width=e.width
        )
    )

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.bind_all(
    "<MouseWheel>",
    lambda e:
    canvas.yview_scroll(
        int(-1*(e.delta/120)),
        "units"
    )
)

    return scrollable_frame


############# RIGHT SIDE CONTAINER ############
right_container = Frame(root, bg="#f4e8e8")
right_container.pack(side="left", fill="both", expand=True)


############# HEADER ############
header = Frame(right_container, bg="#f4e8e8")
header.pack(fill="x", padx=20, pady=20)

text_frame = Frame(header, bg="#f4e8e8")
text_frame.pack(side="left")

Label(
    text_frame,
    text="Welcome back, Iskolar ng Bayan",
    font=("Regular", 14),
    fg="Gray",
    bg="#f4e8e8"
).pack(anchor="w")

Label(
    text_frame,
    text="Christian Bergola",
    font=("Plus Jakarta Sans", 20, "bold"),
    fg="Black",
    bg="#f4e8e8"
).pack(anchor="w")


############# PROFILE ############
profile = Frame(header, width=200, height=50, bg="white")
profile.pack(side="right")
profile.pack_propagate(False)

Label(
    profile,
    text="CB",
    bg="#F5C842",
    fg="black",
    width=3,
    height=3
).pack(side="left", padx=10, pady=10)

info = Frame(profile, bg="white")
info.pack(side="left", pady=5)

Label(
    info,
    text="Christian Bergola",
    bg="white",
    font=("Arial", 11, "bold")
).pack(anchor="w")

Label(
    info,
    text="Student",
    bg="white",
    fg="gray",
    font=("Arial", 9)
).pack(anchor="w")

############# PAGE CONTAINER ############

page_container = Frame(right_container, bg="#f4e8e8")
page_container.pack(fill="both", expand=True)

############# PAGES ############
dashboard_page = Frame(page_container, bg="#f4e8e8")
mycourses_page = Frame(page_container, bg="#f4e8e8")
browse_page = Frame(page_container, bg="#f4e8e8")
resources_page = Frame(page_container, bg="#f4e8e8")


for page in (
    dashboard_page,
    mycourses_page,
    browse_page,
    resources_page
):
    page.place(relx=0, rely=0, relwidth=1, relheight=1)

dashboard_content = create_scrollable_page(dashboard_page)

mycourses_content = create_scrollable_page(mycourses_page)

browse_content = create_scrollable_page(browse_page)

resources_content = create_scrollable_page(resources_page)


 ############ PAGE SWITCHER ############
def show_page(page):
    page.tkraise()

############# SIDEBAR MENU ############
menu_items = [
    ("🏠  Dashboard", dashboard_page),
    ("📖  My Courses", mycourses_page),
    ("🔍  Browse Courses", browse_page),
    ("📂  Resources", resources_page)
]

for text, page in menu_items:

    Button(
        sidebar,
        text=text,
        command=lambda p=page: show_page(p),
        font=("Inter", 14),
        fg="White",
        bg="#7b1d2e",
        activebackground="#F5C842",
        relief="flat",
        width=60,
        height=2,
        anchor="w",
        padx=30
    ).pack(anchor="w", pady=2, padx=20)

def logout():
    confirm = messagebox.askyesno(
        "Logout", 
        "Are you sure you want to logout?")
    if confirm:
        root.destroy()
        import homepage    

logout_btn = Button(
    sidebar,
    text="[→   Logout",
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
)

logout_btn.pack(anchor="w", pady=(10, 0), padx=20)

#==============================================================

############ DEFAULT PAGE ############

show_page(dashboard_page)

############ DASHBOARD PAGE ############

# TILE SECTION
tile_container = Frame(
    dashboard_content,
    bg="#f4e8e8"
)
tile_container.pack(anchor="nw", padx=20, pady=10)

Label(
    tile_container,
    text="Dashboard",
    bg="#f4e8e8",
    fg="#1d2235",
    font=("Arial", 28, "bold")
).pack(anchor="w", pady=(10, 0))

Label(
    tile_container,
    text="View the overview of your courses and progress.",
    bg="#f4e8e8",
    fg="gray",
    font=("Arial", 11)
).pack(anchor="w", pady=(0, 20))


def create_dashboard_tile(parent, bg, icon_text, title, number):

    tile = Frame(parent, width=1600, height=180, bg=bg)
    tile.pack(side="top", expand=True, fill='x', padx=10, pady=10)
    tile.pack_propagate(False)

    Label(
        tile,
        text=icon_text,
        bg=bg,
        font=("Arial", 24)
    ).pack(anchor="w", padx=15, pady=(15, 0))

    Label(
        tile,
        text=title,
        bg=bg,
        fg="gray",
        font=("Arial", 10)
    ).pack(anchor="w", padx=15, pady=(10, 0))

    Label(
        tile,
        text=number,
        bg=bg,
        fg="black",
        font=("Arial", 24, "bold")
    ).pack(anchor="w", padx=15, pady=10)

try:
    total_courses = len(course.load_data(course.COURSES_DATABASE))
except Exception:
    total_courses = 0

tiles = [
    ("📚", "#F5E3CC", "Enrolled Courses", str(total_courses))
]

for icon, bg, title, number in tiles:
    create_dashboard_tile(
        tile_container,
        bg,
        icon,
        title,
        number
    )

############ MAIN CONTENT ############
dashboard_main = Frame(
    dashboard_content,
    bg="#f4e8e8"
)
dashboard_main.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

########### LEFT SIDE ############
dashboard_left = Frame(
    dashboard_main,
    bg="#f4e8e8"
)

dashboard_left.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 20)
)

dashboard_header = Frame(
    dashboard_left,
    bg="#f4e8e8"
)

dashboard_header.pack(fill="x")

Label(
    dashboard_header,
    text="Resources",
    font=("Arial", 16, "bold"),
    bg="#f4e8e8"
).pack(side="left")

Button(
    dashboard_header,
    text="View all resources >",
    font=("Arial", 10),
    fg="#7b1d2e",
    bg="#f4e8e8",
    relief="flat",
    activebackground="#f4e8e8",
    activeforeground="#7b1d2e",
    cursor="hand2"
).pack(side="right")


# COURSE CARD
def dashboard_course_card(parent, title, course, uploader):

    card = Frame(parent, bg="white", height=100)
    card.pack(fill="x", pady=10)
    card.pack_propagate(False)

    icon = Frame(
        card,
        width=60,
        height=60,
        bg="#7b1d2e"
    )

    icon.pack(
        side="left",
        padx=10,
        pady=10
    )

    icon.pack_propagate(False)

    Label(
        icon,
        text="📄",
        font = 15,
        fg="white",
        bg="#7b1d2e"
    ).pack(expand=True)

    text = Frame(card, bg="white")
    text.pack(
        side="left",
        fill="both",
        expand=True,
        pady=10
    )

    Label(
        text,
        text=title,
        font=("Arial", 12, "bold"),
        bg="white"
    ).pack(anchor="w", pady=(10,0))

    Label(
        text,
        text=course,
        font = ("Arial", 10),
        bg = "white"
    ).pack(anchor="w")


    Label (
        text,
        text = uploader,
        fg="gray",
        bg="white"
    ).pack(anchor="w")

    Button(
        card,
        text="⬇",
        relief="flat",
        font = ("Arial", 12),
        fg = "#7b1d2e",
        bg="white"
    ).pack(side="right", padx=(0, 30))

    Button(
        card,
        text="Open",
        bg="#7b1d2e",
        fg="white",
        relief="flat"
    ).pack(side="right", padx=10)

dashboard_course_card(
    dashboard_left,
    "Assignment Guidelines.pdf",
    "Discrete Mathematics",
    "Author: Luisito Lacatan "
)

dashboard_course_card(
    dashboard_left,
    "Midterms Coverage.pdf",
    "Object Oriented Programming",
    "Author: Godofredo Avena"
)

dashboard_course_card(
    dashboard_left,
    "Lecture 5 Presentation",
    "Computer Hardware Fundamentals",
    "Author: John Paul Avila "
)

dashboard_course_card(
    dashboard_left,
    "Project Requirement.docx",
    "CWTS 2 (Cycle 3)",
    "Author: Arnold Rodriquez"
)

dashboard_course_card(
    dashboard_left,
    "Chapter Quizzes Consilidation.pdf",
    "Physics for Engineers",
    "Author: Elizabethe Biza"
)

#2. MY COURSES

# MAIN CONTENT
main = Frame(mycourses_content, bg="#f4e8e8")
main.pack(fill="both", expand=True, padx=20)

# Breadcrumb
Label(
    main,
    text="Dashboard   >   My Courses",
    bg="#f4e8e8",
    fg="gray",
    font=("Arial", 10)
).pack(anchor="w")

# Title
Label(
    main,
    text="My Courses",
    bg="#f4e8e8",
    fg="#1d2235",
    font=("Arial", 28, "bold")
).pack(anchor="w", pady=(10, 0))

Label(
    main,
    text="View and manage all your enrolled courses.",
    bg="#f4e8e8",
    fg="gray",
    font=("Arial", 12)
).pack(anchor="w", pady=(0, 20))

# COURSE CARD FUNCTION
def create_course_card(parent, title, description, last_lesson, file_name):

    card = Frame(
        parent,
        bg="white",
        height=160,
        bd=0
    )
    card.pack(fill="x", pady=10)
    card.pack_propagate(False)

    # TOP SECTION
    top = Frame(card, bg="white")
    top.pack(fill="x", padx=25, pady=(20, 0))

    Label(
        top,
        text=title,
        font=("Arial", 18, "bold"),
        bg="white",
        fg="#1d2235"
    ).pack(side="left")


    # DESCRIPTION
    Label(
        card,
        text=description,
        font=("Arial", 11),
        fg="gray",
        bg="white"
    ).pack(anchor="w", padx=25, pady=(10, 0))

    # DETAILS
    details = Frame(card, bg="white")
    details.pack(anchor="w", padx=25, pady=(18, 0))

    Label(
        details,
        text=last_lesson,
        font=("Arial", 11),
        bg="white"
    ).pack(side="left")

    Label(
        details,
        text=f"     📄  {file_name}",
        font=("Arial", 11),
        fg="gray",
        bg="white"
    ).pack(side="left")

    Button(
        card,
        text="Continue",
        bg="#7b1d2e",
        fg="white",
        relief="flat",
        width=15,
        height=2
    ).place(relx=0.92, rely=0.5, anchor="center")

# COURSES LIST
create_course_card(
    main,
    "Object Oriented Programming",
    "Learn the basics of HTML, CSS, JavaScript, and modern web development practices.",
    "Last lesson: Python",
    "web-dev-programming.pdf",
)

create_course_card(
    main,
    "Computer Hardware Fundamentals",
    "Master the fundamentals of user interface and user experience design.",
    "Last lesson: CPU",
    "cpu-principles.pdf"
)

create_course_card(
    main,
    "Discrete Mathematics",
    "Learn the fundamental concepts of discrete mathematics, including logic, sets, relations, functions, and graph theory.",
    "Last lesson: Sets",
    "sets.pdf"
)

create_course_card(
    main,
    "Calculus 2",
    "Master integration, sequences, series, and parametric equations to solve complex problems.",
    "Last lessons: Not Started",
    "integration by parts.pdf"
)

create_course_card(
    main,
    "Physics for Engineers",
    "Explore the laws of physics that underpin modern engineering and technology.",
    "Last lesson: Electro Dynamics",
    "motion.pdf"
)

create_course_card(
    main,
    "Engineering data Analysis",
    "Analyze engineering data using statistical methods and computational tools to support informed decisions.",
    "Last lesson: Electro Dynamics",
    "descriptive analysis.pdf"
)


#3. BROWSE COURSES

# MAIN CONTENT
main_content = Frame(
    browse_content,
    bg="#f4e8e8"
)
main_content.pack(fill="both", expand=True, padx=20)

# LOCATION
Label(
    main_content,
    text="Dashboard > Browse Courses",
    bg="#f4e8e8",
    fg="gray",
    font=("Arial",10)
).pack(anchor="w")


# TITLE
Label(
    main_content,
    text="Course Catalog",
    font=("Arial", 28, "bold"),
    bg="#f4e8e8",
    fg="#1d2235"
).pack(anchor="w", pady=(10, 0))

Label(
    main_content,
    text="Browse and enroll in available courses",
    font=("Arial", 12),
    bg="#f4e8e8",
    fg="gray"
).pack(anchor="w", pady=(0, 15))


# COURSES AREA

courses_frame = Frame(main_content, bg="#f4e8e8")
courses_frame.pack(fill="both", expand=True)

left_column = Frame(courses_frame, bg="#f4e8e8")
left_column.pack(side="left", fill="both", expand=True, padx=(0, 10))

right_column = Frame(courses_frame, bg="#f4e8e8")
right_column.pack(side="left", fill="both", expand=True)

def course_card(parent,
    title,
    #instructor,
    description,
    enrolled=False):

    card = Frame(
        parent,
        bg="white",
        height=190,
        width=550
    )

    card.pack(fill="x", pady=10)
    card.pack_propagate(False)

    Label(
        card,
        text=title,
        font=("Arial", 16, "bold"),
        bg="white",
        fg="#1d2235"
    ).pack(anchor="w", padx=20, pady=(15, 5))

    # Label(
    #     card,
    #     text=f"Prof. {instructor}",
    #     font=("Arial", 10),
    #     bg="white",
    #     fg="gray"
    # ).pack(anchor="w", padx=20)

    Label(
        card,
        text=description,
        font=("Arial", 10),
        bg="white",
        fg="gray"
    ).pack(anchor="w", padx=20)

    if enrolled:
        Button(
            card,
            text="Already Enrolled",
            bg="#eadede",
            fg="#666",
            relief="flat"
        ).pack(
            fill="x",
            padx=20,
            pady=15)
        
    else:
        enroll_button = Button(
            card,
            text="+  Enroll Now",
            bg="#86192b",
            fg="white",
            relief="flat"
        )

        enroll_button.config(
            command=lambda: enroll_button.config(
                text="Already Enrolled",
                bg="#eadede", fg="#666",
                state="disabled"))
        enroll_button.pack(
            fill="x",
            padx=20,
            pady=15)

try:
    all_courses = course.load_data(course.COURSES_DATABASE)
    for index, course_item in enumerate(all_courses):
        parent_column = left_column if index % 2 == 0 else right_column
        is_enrolled = False
        course_card(
            parent_column,
            course_item['course_name'],
            course_item['course_description'],
            enrolled=is_enrolled
        )
except Exception  as e:
    messagebox.showerror("Error", str(e))


#4. RESOURCES

# MAIN CONTENT
content = Frame(resources_content, bg="#f4e8e8")
content.pack(fill="both", expand=True, padx=20, pady=10)

# LEFT CONTENT
left = Frame(content, bg="#f4e8e8")
left.pack(side="left", fill="both", expand=True)

# RIGHT SIDEBAR
right = Frame(content, bg="#f4e8e8", width=300)
right.pack(side="right", fill="y", padx=(20,0))
right.pack_propagate(False)

########### PAGE HEADER ############
top_bar = Frame(left, bg="#f4e8e8")
top_bar.pack(fill="x")

Label(
    top_bar,
    text="Dashboard   >   Resources",
    bg="#f4e8e8",
    fg="gray",
    font=("Arial",10)
).pack(anchor="w")

Label(
    top_bar,
    text="Resources",
    bg="#f4e8e8",
    fg="#1d2235",
    font=("Arial",28,"bold")
).pack(anchor="w", pady=(10,0))

Label(
    top_bar,
    text="Access all your learning materials and resources.",
    bg="#f4e8e8",
    fg="gray",
    font=("Arial",12)
).pack(anchor="w", pady=(0,15))


############ RESOURCE TABLE ############
table = Frame(left,bg="white")
table.pack(fill="both", expand=True)

# Header Row
header_row = Frame(table,bg="#f7f7f7",height=45)
header_row.pack(fill="x")

headers = [
    ("Resource Name",40),
    ("Uploaded By",25),
    ("Actions",10)
]

for text,width in headers:
    Label(
        header_row,
        text=text,
        width=width,
        anchor="w",
        bg="#f7f7f7",
        font=("Arial",10,"bold"),
        padx=(30)
    ).pack(side="left")


############# RESOURCE DATA ############
resources = [
("Assignment Guidelines.pdf", "Prof. Luisito Lacatan"),
("Midterm Coverage.pdf", "Prof. Godofredo Avena"),
("Lecture 5 Presentation", "Prof. John Paul Avila"),
("Project Requirements.docx", "Prof. Arnold Rodriguez"),
("Chapter Quizzes Consolidated.pdf","Prof. Elizabeth Bisa"),
("Sample Exam Questions", "Prof. Manuelito Bengo"),
("Final Project Rubric", "Prof. Manuelito Bengo")
]

for name, uploader in resources:

    row = Frame(table,bg="white",height=60, pady=10)
    row.pack(fill="x")
    row.pack_propagate(False)

    Label(
        row,
        text="📄",
        bg="#F5E8B0",
        font=("Arial",18),
        width=2
    ).pack(side="left", padx=10)

    Label(
        row,
        text=name,
        width=28,
        anchor="w",
        bg="white",
        font=("Arial",11,"bold")
    ).pack(side="left")

    Label(
        row,
        text=uploader,
        bg="white",
        width=20,
        anchor="w",
    ).pack(side="left", padx=(90, 0))

    Button(
        row,
        text="⬇", font = 1,
        relief="flat",
        bg="white"
    ).pack(side="left", padx=(150))

############# PAGINATION ############
bottom = Frame(left,bg="#f4e8e8")
bottom.pack(fill="x", pady=15)

Label(
    bottom,
    text="Showing 1-7 of 48 resources",
    bg="#f4e8e8",
    fg="gray"
).pack(side="left")

Button(bottom,text="Previous",relief="flat").pack(side="right",padx=5)
Button(bottom,text="2",relief="flat").pack(side="right")
Button(bottom,text="1",bg="#8B1E3F",fg="white",relief="flat").pack(side="right")
Button(bottom,text="Next",relief="flat").pack(side="right",padx=5)

root.mainloop()