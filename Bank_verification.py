import mysql.connector as connection
import random
conn = connection.connect(
        host='127.0.0.1',
        user='root',
        password='DigitalWorld1.',   
        database='bvn_creation'
    )
cursor = conn.cursor()

# def bvn_create():
#     try:
#         conn = connection.connect(
#             host='127.0.0.1',
#             user='root',
#             password='DigitalWorld1.',   
#             database='bvn_creation'
#         )
#         cursor = conn.cursor()
#         query = '''CREATE TABLE IF NOT EXISTS Bvn (
#             id INT PRIMARY KEY,
#             Full_Name CHAR(100),
#             Address VARCHAR(100),
#             Occupation VARCHAR(50),
#             BVN BIGINT
#         )'''
#         cursor.execute(query)
#         conn.commit()
#         print("Table created successfully!")
#         cursor.close()
#         conn.close()

#     except connection.Error as err:
#         print(f"Error: {err}")



def create():
    querry = """INSERT INTO Bvn (Full_Name, Address,Occupation, BVN) VALUES(%s,%s,%s,%s)
            """

    info= ['Full Name', 'Address', 'Occupation']
    val = []
    
    bvn = random.randrange(10102020301, 20203030432)
    
    for inf in info:

        while True:
            information = input(f"Enter your {inf}: ")
            if information:
                val.append(information)
                break
            else:
                information = input(f" {inf} cannot be empty: ")
    
    val.append(bvn)    
            

    cursor.execute(querry, val)
    conn.commit()
    cursor.close()
    print(f'Dear {val[1]}, you have successfully registered your BVN and your BVN number is {val[-1]}')
# create()


    
    
                
