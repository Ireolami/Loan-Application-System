from database import get_connection
from bvn import get_all_bvns
from utils import validate_email, validate_phone, hash_password, input_password
import sys
import time

def register_user():
    print("📋 Fill in your details to continue:")

    fields = [
        'FirstName', 'LastName', 'Address',
        'PhoneNumber', 'Username', 'Password',
        'Email', 'Next_of_kin', 'Next_of_kin_Number', 'BVN'
    ]
    user_data = []

    for field in fields:
        while True:
            if field == "Password":
                hashed = input_password()
                user_data.append(hashed)
                break

            value = input(f"{field}: ").strip()

            if field in ['PhoneNumber', 'Next_of_kin_Number']:
                if not validate_phone(value):
                    print("❌ Phone number must be 11 digits.")
                    continue

            elif field == 'Email':
                if not validate_email(value):
                    print("❌ Invalid email address.")
                    continue

            elif field == 'BVN':
                print("🔎 Checking BVN registry...")
                time.sleep(2)
                valid_bvns = get_all_bvns()
                if value not in valid_bvns:
                    print("❌ BVN not found.")
                    decision = input("Enter 1 to retry, 2 to register BVN, 3 to exit: ")
                    if decision == '1':
                        continue
                    elif decision == '2':
                        print("Redirecting to BVN creation portal...")
                        # call your create() function here
                        return register_user()
                    elif decision == '3':
                        print("Goodbye.")
                        sys.exit()
                    else:
                        print("Invalid input.")
                        continue

            user_data.append(value)
            break

    insert_to_database(user_data)

def insert_to_database(data):
    conn = get_connection("i_loan")
    cursor = conn.cursor()
    query = """
    INSERT INTO customers
    (FirstName, LastName, Address, PhoneNumber, Username, pwd, Email, Next_of_kin, Next_of_kin_Number, BVN)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    try:
        cursor.execute(query, data)
        conn.commit()
        print("✅ Registration successful!")
    except Exception as e:
        print(f"❌ Failed to register: {e}")
    finally:
        cursor.close()
        conn.close()

def start():
    print("Welcome to i-Loan App 🚀")
    has_bvn = input("Do you have a BVN? (yes/no): ").lower()
    if has_bvn in ['yes', 'y']:
        register_user()
    elif has_bvn in ['no', 'n']:
        decision = input("Would you like to register for BVN now? (yes/no): ").lower()
        if decision in ['yes', 'y']:
            print("Redirecting to BVN creation...")
            # call your create() function here
            register_user()
        else:
            print("You need a BVN to proceed.")
            sys.exit()
    else:
        print("Invalid input.")
        start()

if __name__ == "__main__":
    start()
