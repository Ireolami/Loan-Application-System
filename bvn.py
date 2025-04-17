from database import get_connection

def get_all_bvns():
    conn = get_connection("bvn_creation")
    cursor = conn.cursor()
    cursor.execute("SELECT BVN FROM Bvn")
    bvns = [str(row[0]) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return bvns

# bv=get_all_bvns()
# for i in bv:
#     print(i)