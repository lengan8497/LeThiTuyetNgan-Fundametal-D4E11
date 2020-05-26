teencode = {
    'hc': 'học',
    'nc': 'nói chuyện',
    'vk': 'vũ khí',
    'ck': 'chuyển khoản'
}
while True:
    for key in teencode:
        print(key, end='\t')
    print()
    print('*'*30)

    input_key = input('Enter the word you want to search: ')
    if input_key in teencode:
        print('It means:', teencode[input_key])
    else:
        prompt = input('Word not found, would you like to contribute its meaning? (Y/N)? ')
        if prompt == 'y':
            teencode[input_key] = input('Enter the meaning: ')
            print(teencode)
        else:
            print('Bye')
            break