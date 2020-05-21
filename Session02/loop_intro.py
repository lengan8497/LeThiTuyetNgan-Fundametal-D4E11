# for i in ['a', 'b', 'c']:
#   print(i)

from getpass import getpass

username = 'mindx'
password = 'password'
count = 0
while True:
  if count > 7:
    print('hết lượt thử r bạn eii')
    break
  username_input = input('username = ')
  password_input = input('password = ')
  if username_input == username and password_input == password:
    print('Welcome')
    break
  else:
    count += 1