import psycopg2

# ------------------------ Way 1 (preffered) -------------------------
# connection_string = "host='localhost' dbname='example' user='postgres' password='root'"
# connection = psycopg2.connect(connection_string)


# ------------------------------ Way 2  -------------------------
connection = psycopg2.connect('host=localhost dbname=example user=postgres password=root')

cursor = connection.cursor()


cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

data = {
    'id': 2,
    'completed': False
}
SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'
cursor.execute(SQL, data)

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (3, True))

cursor.execute('SELECT * FROM table2;')

result1 = cursor.fetchmany(2)
print('fetchmany(2)',result1)

result2 = cursor.fetchone()
print('fetchone', result2)

cursor.execute('SELECT * FROM table2;')

result3 = cursor.fetchall()
print('fetchall', result3)

connection.commit()

connection.close()

cursor.close()