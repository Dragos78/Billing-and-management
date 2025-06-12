import psycopg2

connection = psycopg2.connect(host="localhost", dbname="FirstApp", user="postgres", password="admin", port=5432)

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    chooses_user VARCHAR (50),
    first_name VARCHAR (255),
    last_name VARCHAR (255),
    e_mail VARCHAR (255),
    password VARCHAR (50),
    date TIMESTAMP NOT NULL DEFAULT NOW()
    );
""")

cursor.execute("""
INSERT INTO 
users ( chooses_user, first_name, last_name, e_mail, password) 
values ('Administrator', 'Niculae', 'Dragos-Catalin', 'niculaedragos@gmail.com', 'Admin1234!')
""")


connection.commit()
cursor.close()
connection.close()
