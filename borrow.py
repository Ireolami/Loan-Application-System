from database import get_connection
def create_table():
    conn= get_connection('i_loan')
    cursor =conn.cursor()
    try:
        query = """
        CREATE TABLE IF NOT EXISTS Loan (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT,
            BVN BIGINT,
            Amount_borrowed BIGINT,
            Amount_paid BIGINT,
            Payment_status VARCHAR(20),
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        );"""
        cursor.execute(query)
        conn.commit()
        print("Table created successfully")
    except:
        print("Error creating")
    finally:
        
        cursor.close()
    
# create_table()
def borrow_loan():
    