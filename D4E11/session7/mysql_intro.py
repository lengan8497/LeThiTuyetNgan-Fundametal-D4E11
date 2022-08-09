import pymysql

# client = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='Inuka4682!'
# )

# cursor = client.cursor()

# cursor.execute('CREATE DATABASE d4e11')


## CREATE bang trong MySQL ##
# cursor.execute('''
#     CREATE TABLE d4e11.user (
#         id INT(11) AUTO_INCREMENT PRIMARY KEY,
#         username VARCHAR(255),
#         age INT(11)
#     )
# ''')


## INSERT du lieu vao bang ##
# cursor.execute(''' 
# INSERT INTO d4e11.user (username, age)
# VALUES ('data', '96'), ('tada', '98');
# ''')

# cursor.execute(''' SELECT * FROM d4e11.user ''')
# data = cursor.fetchall()
# print(data)
# client.commit()



## Lay giu lieu ra tu MySQL ##
client = pymysql.connect(
    host='localhost',
    user='root',
    password='Inuka4682!',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = client.cursor()


## Lay het tat ca du lieu trong bang ##
# cursor.execute('''SELECT * FROM d4e11.user''')
# data = cursor.fetchall()
# print(data)
# client.commit()


## Chi lay du lieu trong truong chi dinh ##
# cursor.execute('''SELECT username FROM d4e11.user''')
# data = cursor.fetchall()
# print(data)
# client.commit()



# cursor.execute('''SELECT username, id FROM d4e11.user''')
# data = cursor.fetchall()
# print(data)
# client.commit()



# cursor.execute('''SELECT SUM(id) FROM d4e11.user''')
# data = cursor.fetchall()
# print(data)
# client.commit()



# cursor.execute('''SELECT COUNT(id) FROM d4e11.user''')
# data = cursor.fetchall()
# print(data)
# client.commit()


# cursor.execute('''SELECT COUNT(id) AS count FROM d4e11.user''')
# data = cursor.fetchall()
# print(data)
# client.commit()


# cursor.execute('''SELECT MAX(age) AS max FROM d4e11.user''')
# data = cursor.fetchall()
# print(data)
# client.commit()



# cursor.execute('''SELECT MAX(age) AS max FROM d4e11.user''')
# data = cursor.fetchone()
# print(data)
# print(data['max'])
# client.commit()

