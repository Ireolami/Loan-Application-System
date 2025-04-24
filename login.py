from utils import hash_password, validate_email, input_password
from database import get_connection
from borrow import borrow_loan
import time
def get_user_info(username_or_email):
    conn = get_connection('i_loan')
    cursor = conn.cursor()
    try:
        query = 'SELECT Username, Password, Email FROM customers WHERE Username = %s OR Email = %s'
        cursor.execute(query, (username_or_email, username_or_email))
        result = cursor.fetchone()
    except Exception as e:
        print(f'❌ Error fetching information: {e}')
        result = None
    finally:
        cursor.close()
        conn.close()

    if result:
        user, pwd, email = result
        return user, pwd, email
    else:
        print("❌ No match found.")
        return None

def user_login():
    user_input = input("Enter your username or email: ")
    user_data = get_user_info(user_input)

    if not user_data:
        return  # Stop if no user was found

    user, hashed_pwd, email = user_data

    password = input("Enter your password: ")
    
    if hash_password(password) == hashed_pwd:
        print(f"✅ Login successful! Welcome back, {user}.\nWhat would you like to do?\nEnter 1 to borrow loan\nEnter 2 to Pay your loan")
        time.sleep(3)
    else:
        print("❌ Incorrect password.")

user_login()
