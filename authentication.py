from db_connection import db_Connection
conn = db_Connection()
cur = conn.cursor()

def register_user():
    u_name = input("Enter username: ")
    u_pswd = input("Enter password: ")
    u_role = input("Enter role (admin/customer): ")
    cur.execute("insert into users(user_name,password,user_role) values (%s,%s,%s)", (u_name, u_pswd, u_role))
    print(f"{u_name} is registered as {u_role} successfully")

    cur.execute("select * from users where user_name=%s", (u_name,))
    data = cur.fetchone()
    print(data, "userData")

    conn.commit()
    conn.close()

def login_user():
    u_name = input("Enter username to login: ")
    u_pswd = input("Enter password to login: ")
    cur.execute("select * from users where user_name=%s and password=%s", (u_name, u_pswd))
    data = cur.fetchone()
    if not data:
        print("Invalid credentials")
    else:
        return data
