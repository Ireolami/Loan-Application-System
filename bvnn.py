from database import get_connection

def get_all_bvns(bvn):
    conn = get_connection("i_loan")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Bvn where Bvn=%s", (bvn,))
    bvns = cursor.fetchone()
    cursor.close()
    conn.close()
    if bvns:
        print('Match found')
    else:
        print("Not found")
    return bvns

# bv=get_all_bvns()
# for i in bv:
#     print(i)

def get_all_users():
    conn = get_connection('i_loan')
    cursor = conn.cursor()
    cursor.execute('SELECT * from customers')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    if users:
        print(users)
    else:
        print('No User found')
    return users
get_all_users()