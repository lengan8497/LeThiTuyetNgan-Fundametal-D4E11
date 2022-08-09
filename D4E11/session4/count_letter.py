# from itertools import count

# sentence = 'adsewwfsfdgery'

# count_dictionary = {}
# for char in sentence:
#     if char in count_dictionary:
#         count_dictionary[char] = count_dictionary[char] + 1
#     else:
#         count_dictionary[char] = 1
# print(count_dictionary)


# for key in count_dictionary:
#     print(key, count_dictionary[key])



## Sort item
# Cach 1:
# sentence = 'adsewwfsfdgery'

# sorted_sentence = sorted(sentence)
# count_dictionary = {}
# for char in sentence:
#     if char in count_dictionary:
#         count_dictionary[char] = count_dictionary[char] + 1
#     else:
#         count_dictionary[char] = 1
# print(count_dictionary)


# for key in count_dictionary:
#     print(key, count_dictionary[key])



# Cach 2:
# sentence = 'adsewwfsfdgery'

# count_dictionary = {}
# for char in sentence:
#     if char in count_dictionary:
#         count_dictionary[char] = count_dictionary[char] + 1
#     else:
#         count_dictionary[char] = 1

# items = count_dictionary.items()
# print(sorted(items))

# for key in count_dictionary:
#     print(key, count_dictionary[key])



sentence = 'adsewwfsfdgery'

count_dictionary = {}
for char in sentence:
    if char in count_dictionary:
        count_dictionary[char] = count_dictionary[char] + 1
    else:
        count_dictionary[char] = 1

key_value_list = sorted(count_dictionary.items())

# for key_value in key_value_list:
#     print(key_value)

for key_value in key_value_list:
    print(key_value[0], key_value[1])