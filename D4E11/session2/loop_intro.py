# for i in range(5):
#     print('Hello')


# for i in range(5):
#     print(i)


# print(*range(5))


# print(*range(1, 5))


# print(*range(1, 10, 3))  


# for i in range(26):
#     print(i)


# for i in range(0, 101, 2):
#     print(i)


# for i in range(100, 0, -1):
#     print(i)


# for i in ['a', 'b', 'c']:
#     print(i)


# while True:   # Khi TRUE, in ra "you can't stop me"
#     print("you can't stop me")   # Nhan to hop phim Ctrl C de dung lai


# while True:
#     print("you can't stop me")
#     break   # chi in ket qua ra mot lan


# count = 0
# while True:
#     if count == 5:
#         break
#     print("you can't stop me")
#     count = count + 1


# for i in range (5):
#     print("you can't stop me")


# count = 0
# running = True
# while running:
#     if count == 5:
#         running = False
#     print("you can't stop me")
#     count = count + 1


from getpass import getpass

username = 'mindx'
password = 'password'
count = 0
while True:
    if count > 7:
        print('hết lần thử rồi bạn eii')
        break
    username_input = input('username = ')
    password_input = input('password = ')
    if username_input == username and password_input == password:
        print('Welcome')
        break
    else:
        count += 1