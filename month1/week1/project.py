# Create a simple username and password authentication.
# If the username and password specified are correct, then print
# a success message, else print "You're are wrong!" five times.

def is_empty_str(s):
    return not s.strip()

db = {}

def sign_up(username, password):
    if is_empty_str(username) or is_empty_str(password):
        print("Invalid username or password")
        return

    if username in db:
        print("Username already exists")
        return

    db[username] = password

    print("Signup successful")


def sign_in(username, password):
    if is_empty_str(username) or is_empty_str(password) or username not in db or db[username] != password:
        for _ in range(5):
            print("You're are wrong!")
        return

    print("Signin successful")


sign_up("hackbit", "hackbit256")
sign_up("hackbit", "hackbit256")
sign_in("hackbit", "hackbit256")
sign_in("hackbit", "hackbit255")
print(f"users: {db}")
