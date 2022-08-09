Dis = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']

Min_po = [150300, 247100, 333300, 266800, 420900, 318000]

#1
print('Quận có đông dân nhất với số dân:', max(Min_po))
print('Quận có ít dân nhất với số dân:', min(Min_po))

#2
x = max(Min_po)
Index_max = Min_po.index(x)
print('Quận có đông dân nhất:', Dis[Index_max], 'với số dân là', max(Min_po))

y = min(Min_po)
Index_min = Min_po.index(y)
print('Quận có ít dân nhất:', Dis[Index_min], 'với số dân là', min(Min_po))


#3
Min_po = [150300, 247100, 333300, 266800, 420900, 318000]
Squa = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
mat_do = []
for i in range(len(Min_po)):
    Pop_den = Min_po[i]/ Squa[i]
    mat_do.append(Pop_den)
print('Mật độ dân cư:', mat_do)


#4
Tong_mat_do = sum(mat_do)
ave_pop_den = Tong_mat_do/len(Dis)
print('Mật độ dân cư trung bình:', ave_pop_den)