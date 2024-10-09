# Create a simple username and password authentication.
# If the username and password specified are correct, then print
# a success message, else print "You're are wrong!" five times.
# Basic ratelimiting failed sign-in attempts counts to 3

import os

db_name = "db.txt"
max_sign_in_failed_attempts = 3


def main():
    action = get_user_input("Do you want to (1) Sign up or (2) Sign in? Enter 1 or 2: ")

    if action == "1":
        sign_up()
    elif action == "2":
        sign_in()
    else:
        print("Invalid option selected.")


def sign_up():
    db_lines = read_file_lines(db_name)

    while True:
        username, password = get_credentials()
        if username_exists(username, db_lines):
            print("Username already exists! Please try again.")
        else:
            add_user_to_db(username, password)
            print("Signup successful!")
            break


def sign_in():
    db_lines = read_file_lines(db_name)

    for attempt in range(1, max_sign_in_failed_attempts + 1):
        username, password = get_credentials()

        if username_exists(username, db_lines) and compare_password(password, db_lines):
            print(f"Welcome back, {username}!")
            return

        print(f"Invalid credentials. You have {max_sign_in_failed_attempts - attempt} attempts left.")

    print("Access blocked. Too many failed attempts.")


def read_file_lines(file_name):
    if os.path.isfile(file_name):
        with open(file_name, "r") as f:
            lines = []
            for line in f:
                lines.append(line.strip())
            return lines
    return []


def write_lines_to_file(file_name, lines):
    with open(file_name, "a") as f:
        for line in lines:
            f.write(f"{line}\n")


def is_empty_str(s):
    return s.strip() == ""


def username_exists(username, db_lines):
    for line in db_lines:
        if line == f"username:{username}":
            return True
    return False


def compare_password(password, db_lines):
    for line in db_lines:
        if line == f"password:{password}":
            return True
    return False


def add_user_to_db(username, password):
    write_lines_to_file(db_name, [f"username:{username}", f"password:{password}"])


def get_user_input(prompt):
    return input(prompt).strip()


def get_credentials():
    while True:
        username = get_user_input("Enter valid username: ")
        password = get_user_input("Enter valid password: ")

        if is_empty_str(username) or is_empty_str(password):
            print("Invalid username or password! Please try again.")
        else:
            return username, password


if __name__ == "__main__":
    main()
