import requests
from pymongo import MongoClient
mongo_client = MongoClient()
db = mongo_client.get_database('d4e11')
collection = db.get_collection('police_call')

# client = requests.get('https://data.baltimorecity.gov/resource/xviu-ezkt.json')
# data = client.json()
# collection.insert_many()

# total_false_call = collection.count_documents({'priority': 'Non-Emergency'})
# total_call = collection.count_documents()

# print(total_false_call * 100/ total_call)



all_district = collection.distinct('district')

count_call_by_district = {}
for district in all_district:
    count_call_by_district[district] = collection.count_documents({district: district})
print(count_call_by_district)

max = 0
name = ''
for key in count_call_by_district:
    if count_call_by_district[key] > max:
        max = count_call_by_district[key]
        name = key

print(name, max)