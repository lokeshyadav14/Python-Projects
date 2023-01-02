import mysql.connector as sql
'''
mysql> CREATE DATABASE telephone_book;
Query OK, 1 row affected (0.44 sec)

mysql> CREATE TABLE contacts(
     S_no int PRIMARY KEY AUTO_INCREMENT,
     Full_Name VARCHAR(30),
     Mobile_Number VARCHAR(10) NOT NULL,
     Address VARCHAR(50),
     E_Mail VARCHAR(50),
     Genre VARCHAR(20));
Query OK, 0 rows affected (1.66 sec)

'''

# NOTE: table is already created

def add(full_name='', mobile_number='', address='', email='', genre=''):
    # creating connection object
    conn = sql.connect( host = "localhost",
                        user = "root",
                        password = "1412",
                        database='telephone_book')
    # creating instance of cursor to execute query
    cur = conn.cursor()
    # since mobile number is unique for all
    if mobile_number != 'Null':
        cur.execute("INSERT INTO contacts(Full_Name, Mobile_Number, Address, E_Mail, Genre) VALUES (%s, %s, %s, %s, %s);", (full_name, mobile_number, address, email, genre))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
    
    

def search(full_name='', mobile_number='', address='', email='', genre=''):
    # creating connection object
    conn = sql.connect( host = "localhost",
                        user = "root",
                        password = "1412",
                        database='telephone_book')
    # creating instance of cursor to execute query
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE Full_Name=%s OR Mobile_Number=%s OR Address=%s OR E_Mail=%s OR Genre=%s;", (full_name, mobile_number, address, email, genre))
    rows = cur.fetchall()
    conn.close()
    if len(rows)>0:
        return rows
    else:
        return ["Data Not Found"]

def delete(mobile_number=''):
    # creating connection object
    conn = sql.connect( host = "localhost",
                        user = "root",
                        password = "1412",
                        database='telephone_book')
    # creating instance of cursor to execute query
    cur = conn.cursor()
    
    cur.execute("DELETE FROM contacts WHERE Mobile_Number=%s",(mobile_number,))
    conn.commit()
    conn.close()

def view_all():
    # creating connection object
    conn = sql.connect( host = "localhost",
                        user = "root",
                        password = "1412",
                        database='telephone_book')
    # creating instance of cursor to execute query
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts;")
    rows = cur.fetchall()
    conn.close()
    return rows