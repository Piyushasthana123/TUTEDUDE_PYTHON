import psycopg2
connect = psycopg2.connect(dbname = "postgres", user = "postgres",password = "post@444", host = "localhost", port = "5432")
print("successfully connected")
cursor = connect.cursor()