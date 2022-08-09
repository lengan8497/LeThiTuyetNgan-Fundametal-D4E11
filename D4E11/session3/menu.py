monan1 = 'phở'
monan2 = 'bún chả'
monan3 = 'trứng rán'
monan4 = 'thịt chó'
monan5 = 'cơm'

# monan = ['phở', 'bún chả', 'trứng rán', 'thịt chó', 'cơm']
# print(monan[-4])


# monan = ['phở', 'bún chả', 'trứng rán', 'thịt chó', 'cơm']
# for i in range (5):
#     print(monan[i])


# monan = ['phở', 'bún chả', 'trứng rán', 'thịt chó', 'cơm']
# for i in range (len(monan)):
#     print(monan[i])   # READ


# monan = ['phở', 'bún chả', 'trứng rán', 'thịt chó', 'cơm']
# monan.append('bơ')   # CREATE
# for i in range (len(monan)):
#     print(monan[i])   # READ


# monan = ['phở', 'bún chả', 'trứng rán', 'thịt chó']
# monan[0] = 'cơm'   # UPDATE
# print(monan)


# monan = ['phở', 'bún chả', 'trứng rán', 'thịt chó', 'cơm']
# print(monan.index('trứng rán'))
# print(monan)


# monan = ['phở', 'bún chả', 'trứng rán', 'thịt chó', 'cơm']
# print('trứng' in monan)



# monan = ['phở', 'bún chả', 'trứng rán', 'thịt chó']
# for i in range(len(monan)):
#     print(i+1, monan[i])

# update_value = input('nhập tên món ăn muốn đổi: ')
# if update_value in monan:
#     index = monan.index(update_value)
#     monan[index] = input('nhập tên món ăn mới: ')
#     print(monan)
# else:
#     print('Không tìm thấy món đó đâu mannn')



monan = ['phở', 'bún chả', 'trứng rán', 'thịt chó']
for i in range(len(monan)):
    print(monan[i])   # READ
monan[0] = 'cơm'   # UPDATE
print(monan)
monan.pop(0)   # DELETE by index
print(monan)
monan.remove('bún chả')   # DELETE by value
print(monan)