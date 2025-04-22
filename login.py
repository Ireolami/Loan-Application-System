from utils import hash_password, validate_email, input_password
from database import get_connection

def get_all_access():
    conn = get_connection('i_loan')
    cursor =conn.cursor()
    querry = 'SELECT Username, pwd, Email from customers'
    cursor.execute(querry)
    result =  cursor.fetchall()
    cursor.close()
    conn.close()
    if result:
        for re in result:
            username, pwd, email =re
    
    print(f"This is the list of the Usernames: {username}")
get_all_access()
def login():
    
    email =input("Enter your email or username: ")
    password = input("Enter your password: ")

    if not validate_email(email):
        print("Email ")