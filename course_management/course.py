import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

COURSES_DATABASE = os.path.join(BASE_DIR, "courses.json")

def load_courses():
    try:
        with open(COURSES_DATABASE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  

def save_courses(data):
    with open(COURSES_DATABASE, "w") as f:
        return json.dump(data, f, indent=4)

def create_course(course_name, course_description):
    if not course_name.strip():
        raise ValueError("Course Name must not be left blank.")
    
    courses = load_courses()
    for c in courses:
        if c['course_name'] == course_name.strip():
            raise ValueError(f"Course: {course_name} already exists.")
            
    new_course = {
        "course_name" : course_name.strip(),
        "course_description" : course_description.strip(),
        "course_files" : [] 
    }
    courses.append(new_course)
    save_courses(courses)