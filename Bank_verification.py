import mysql.connector as connection
import random
from database import get_connection
import time



conn = get_connection("i_loan")
    
cursor = conn.cursor()

def bvn_create():
    try:
       
        # cursor = conn.cursor()
        query = '''CREATE TABLE IF NOT EXISTS Bvn (
            id INT PRIMARY KEY AUTO_INCREMENT,
            FirstName CHAR(100),
            LastName CHAR (100),
            Address VARCHAR(100),
            PhoneNumber BIGINT,
            NOK CHAR (50),
            NOKN BIGINT,
            Occupation VARCHAR(50),
            BVN BIGINT
        )'''
        cursor.execute(query)
        conn.commit()
        print("Table created successfully!")
        cursor.close()
        conn.close()

    except connection.Error as err:
        print(f"Error: {err}")

# bvn_create()

def create():
    querry = """INSERT INTO Bvn ( FirstName, LastName,  Address, PhoneNumber, NOK, NOKN, Occupation, BVN) VALUES(%s,%s,%s,%s, %s,%s,%s,%s)
            """

    info= ['First Name', 'Last Name', 'Address','Phone Number', 'Next of Kin', 'Next of Kin Number', 'Occupation']
    val = []
    
    bvn = random.randrange(10102020301, 20203030432)
    # customer_id =20250421
    # val.append(customer_id)
    print("You are welcome to BVN Creation portal")
    time.sleep(3)
    for field in info:

        while True:
            information = input(f"Enter your {field}: ").strip()
            if not information:
                print(f"❌ {field} cannot be empty.")
                continue
            if field in ['Phone Number', 'Next of Kin Number']:
                if not (information.isdigit() and len(information) == 11):
                    print(f"❌ {field} must be 11 digits.")
                    continue
            val.append(information)
            break
    
    val.append(bvn)    
            

    cursor.execute(querry, val)
    conn.commit()
    cursor.close()
    print(f'Dear {val[0]}, you have successfully registered your BVN and your BVN number is {val[-1]}')
# create()


    
    
                
