import re
import bcrypt
import getpass

def validate_email(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email)

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 11

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def input_password():
    while True:
        password = getpass.getpass("Enter your Password: ")
        if len(password) < 8 or not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password) or not re.search(r'[0-9]', password):
            print("❌ Password must be at least 8 characters long, include uppercase, lowercase, and a number.")
        else:
            return hash_password(password)
