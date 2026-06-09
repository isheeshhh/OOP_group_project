import json
import os

DATABASE_FILE = "users.json"

def load_users():
    with open(DATABASE_FILE, "r") as file:
        return json.load(file)


def save_users(data):
    
    #Saves updated data to users.json.
    

    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)


def username_exists(username):
    
    # Checks if a username already exists.
    

    data = load_users()

    for user in data["users"]:

        if user["username"] == username:
            return True

    return False


def register_user(fullname, username, password, role):
   
    # Creates a new account.
    

    if username_exists(username):
        return False

    data = load_users()

    new_user = {
        "fullname": fullname,
        "username": username,
        "password": password,
        "role": role
    }

    data["users"].append(new_user)

    save_users(data)

    return True


def login_user(username, password):
   
    # Verifies login credentials.
    

    data = load_users()

    for user in data["users"]:

        if (
            user["username"] == username and
            user["password"] == password
        ):
            return user

    return None


def get_user(username):
    
    #Returns a user record.
    

    data = load_users()

    for user in data["users"]:

        if user["username"] == username:
            return user

    return None


initialize_database()
