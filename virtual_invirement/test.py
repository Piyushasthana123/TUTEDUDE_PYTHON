import psycopg2
def table():
    connect = psycopg2.connect(dbname = "postgres", user = "postgres",password = "post@444", host = "localhost", port = "5432")
    cursor = connect.cursor()
    cursor.execute('''create table employees(name text , id int , age int);''')
    print("Table created successfully")
    connect.commit()
    connect.close()

def data():
    connect = psycopg2.connect(dbname="postgres", user="postgres", password="post@444", host="localhost", port="5432")
    cursor = connect.cursor()

    name  = input("Enter employee name: ")
    id= int(input("Enter employee id: "))
    age = int(input("Enter employee age: "))
    query="""insert into employees(name,id,age) values(%s,%s,%s);"""
    cursor.execute(query,(name,id,age))
    print("data created successfully")
    connect.commit()
    connect.close()


def extract():
    connect = psycopg2.connect(dbname="postgres", user="postgres", password="post@444", host="localhost", port="5432")
    cursor = connect.cursor()
    cursor.execute("""select * from employees;""")
    print(cursor.fetchall(),type(cursor.fetchall()))
    # show = cursor.fetchone()
    # print(show[0])
    connect.commit()
    connect.close()
extract()
# table()
# data()