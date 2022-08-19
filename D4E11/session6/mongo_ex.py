from pymongo import MongoClient
client = MongoClient()
db = client.get_database('mongo_practice')
movie_collection = db.get_collection('movies')

data = [
    {
        'title' : 'Fight Club',
        'writer' : 'Chuck Palahniuk',
        'year' : 1999,
        'actors' : [
        'Brad Pitt',
        'Edward Norton',
        ]
    },
    {
        'title' : 'Pulp Fiction',
        'writer' : 'Quentin Tarantino',
        'year' : 1994,
        'actors' : [
        'John Travolta',
        'Uma Thurman',
        ]
    },
    {
        'title' : 'Inglorious Basterds',
        'writer' : 'Chuck Palahniuk',
        'year' : 2009,
        'actors' : [
        'Brad Pitt',
        'Diane Kruger',
        'Eli Roth'
        ]
    },
    {
        'title' : 'The Hobbit: An Unexpected Journey',
        'writer' : 'J.R.R. Tolkein',
        'year' : 2012,
        'franchise' : 'The Hobbit'
    },
    {
        'title' : 'The Hobbit: The Desolation of Smaug',
        'writer' : 'J.R.R. Tolkein',
        'year' : 2013,
        'franchise' : 'The Hobbit'
    },
    {
        'title' : 'The Hobbit: The Battle of the Five Armies',
        'writer' : 'J.R.R. Tolkein',
        'year' : 2012,
        'franchise' : 'The Hobbit',
        'synopsis': 'Bilbo and Company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness.'
    },
    {
        'title' : "Pee Wee Herman's Big Adventure",
    },
    {
        'title' : 'Avatar',
    },
]

# movie_collection.insert_many(data)

# all_movies = movie_collection.find({
#   '$or': [
#     {'year': {'$lt': 2000}},
#     {'year': {'$gt': 2010}}
#   ]
# })

# # for movie in all_movies:
# #   print(movie)


# movie_collection.update(
#   {'title': 'The Hobbit: An Unexpected Journey'}, 
#   {
#     '$push': {
#       'synopsis': 'A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug.'
#     }
#   }
# )


# movie_collection.update(
#   {'title': 'The Hobbit: The Desolation of Smaug'}, 
#   {
#     '$push': {
#       'synopsis': 'The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring.'
#     }
#   }
# )

# movie_collection.update(
#   {'title': 'Pulp Fiction'}, 
#   {
#     '$push': {
#       'actors': 'Samuel L. Jackson'
#     }
#   }
# )

# movie_found = movie_collection.find({
#   '$and': [
#     {
#       'synopsis': {'$regex': '.*gold.*'}
#     },
#     {
#       'synopsis': {'$regex': '.*dragon.*'}
#     }
#   ]
  
# })

# for movie in movie_found:
#   print(movie)

# movie_collection.delete_one({'title': 'Avatar'})