from database import get_connection
from bvnn import get_all_bvns as single, get_all_users
from utils import validate_email, validate_phone, hash_password, input_password
import sys
import time
from Bank_verification import create as bvn_create
from login import user_login as account_login


get_info =[]
# from single_bvn import get_single as single_bvn

user_found = get_all_users()
all_usernames = [user[10] for user in user_found]
all_emails = [user[9] for user in user_found]
all_bvns = [user[8] for user in user_found]
def register_user():
    print("📋 Fill in your details to continue:")
    

    fields = [
        'email', 'username', 'password'
    ]

    #Looping of information needed to register
    for field in fields:
        while True:
            if field == "password":
                #if the loop is password, the password is hashed
                hashed = input_password()
                get_info.append(hashed)
                break

            value = input(f"{field}: ").strip()
            
            if field == 'Email':
                if not validate_email(value):
                    print("❌ Invalid email address.")
                    continue
                if value in all_emails:
                    print("❌ Email already in use")
                    continue

            elif field =='username':
                if value in all_usernames:
                    print("❌ Username taken")
                    continue
                else:
                    print("Username is valid")
            

            get_info.append(value)
            break

    insert_to_database(get_info)

def insert_to_database(data):
    conn = get_connection("i_loan")
    cursor = conn.cursor()
    query = """
    INSERT INTO customers
    (FirstName, LastName, Address, PhoneNumber,NOK, NOKN, Occupation, BVN, Email, Username, Password )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)
    """
    try:
        """This confirms if there is no error and commits into database"""
        cursor.execute(query, data)
        conn.commit()
        print("✅ Registration successful!")
        account_login()
    except Exception as e:
        #if there is an error, this prints the error
        print(f"❌ Failed to register: {e}")
    finally:
        cursor.close()
        conn.close()
 
def start():
    print("Welcome to i-Loan App 🚀")
    has_bvn = input("Do you have a BVN? (yes/no): ").lower()
    if has_bvn in ['yes', 'y']:
        """If user has BVN, this code directs user to Loan Registration portal"""
        global bvn_search
        bvn_search = int(input('Enter your bvn: '))
        if bvn_search:
            bvn= single(bvn_search)
            if bvn not in all_bvns:
                for each in bvn[1:]:
                    get_info.append(each)
                print(f'Dear {get_info[1]}, you are being redirected to the i_Loan Registration App')
                time.sleep(3)
                register_user()
            else:
                print('BVN in use\nYou are being redirected to login page....')
                time.sleep(3)
                account_login() 
        else:
            bvn_search = int(input('Enter your bvn: '))
        # print("Kindly wait while we direct you to the Registration portal")
        # time.sleep(3)
        # register_user()
    elif has_bvn in ['no', 'n']:
        decision = input("Would you like to register for BVN now? (yes/no): ").lower()
        if decision in ['yes', 'y']:
            print("Redirecting to BVN creation...")
            # This part calls redirects user to BVN creation portal...
            bvn_create()
            print("Welcome Back... you can proceed to register...")
            register_user()
        else:
            print("You need a BVN to proceed.")
            sys.exit()
    else:
        print("Invalid input.")
        start()

if __name__ == "__main__":
    start()
