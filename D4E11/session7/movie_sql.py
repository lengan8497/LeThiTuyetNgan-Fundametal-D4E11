import pymysql

## Ket noi voi du lieu MongoClient ##
from pymongo import MongoClient

mongo_client = MongoClient()
mongo_db = mongo_client.get_database('mongo_practice')
movie_collection = mongo_db.get_collection('movies')


## Ket noi voi du lieu MySQL ##
mysql_client = pymysql.connect(
    host='localhost',
    user='root',
    password='Inuka4682!',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = mysql_client.cursor()


## Tao bang trong MySQL ##
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movie.movie(
        id VARCHAR(255) PRIMARY KEY,
        title VARCHAR(255),
        writer VARCHAR(255),
        year VARCHAR(255)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS movie.actor(
        name VARCHAR(255) PRIMARY KEY
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS movie.movie_actor(
        movie_id VARCHAR(255),
        actor_name VARCHAR(255),
        PRIMARY KEY(movie_id, actor_name)
    )
''')


# ## Upload du lieu tu MongoDB sang MySQL ##
# query = {
#     'title': {'$ne': None},
#     'writer': {'$ne': None},
#     'year': {'$ne': None},
#     'actors': {'$ne': None}
# }
# for movie in movie_collection.find(query):   # EXTRACT
#     # TRANSFORM
#     movie_id = str(movie['_id'])
#     movie_title = movie['title']
#     movie_writer = movie['writer']
#     movie_year = movie['year']
#     # LOAD
#     cursor.execute(f'''
#         INSERT INTO movie.movie(id, title, writer, year)
#         VALUES ('{movie_id}', '{movie_title}', '{movie_writer}', '{movie_year}')
#     ''')

query = [
  {
    '$match': {
        'actors': {'$ne': None}
        }
  },
  {
    '$unwind': '$actors'
  },
  {
    '$group': {
        '_id': '$actors',
    }
  }
]
# for actor in movie_collection.aggregate(query):
#     print(actor)


for actor in movie_collection.aggregate(query):
    print(actor['_id'])
    cursor.execute(f'''
    INSERT INTO movie.actor(name)
    VALUES('{actor['_id']}')
    ''')

mysql_client.commit()