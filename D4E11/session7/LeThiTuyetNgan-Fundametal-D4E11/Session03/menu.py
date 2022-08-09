monan1 = 'phở'
monan2 = 'bún chả'
monan3 = 'trứng rán'
monan4 = 'thịt chó'
monan5 = 'cơm'

monan = ['phở', 'bún chả', 'trứng rán', 'thịt chó']
for i in range(len(monan)):
    print(monan[i])
monan.pop(0)  #DELETE by index
monan.remove('bún chả')  #DELETE by value
print(monan)

