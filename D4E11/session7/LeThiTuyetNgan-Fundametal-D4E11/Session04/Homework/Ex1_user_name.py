input_name = input('Your full name: ').lower().split(' ')
name = [char for char in input_name if char != '']
for i in range(len(name)):
    name[i] = name[i].title()
print('Updated:', ' '.join(name))