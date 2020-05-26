input_bac = int(input('How many B bacterias are there? '))
input_time = int(input('How much time in minutes will we wait? '))
n = input_time//2
bac = input_bac*(2**n)
print('After', input_time,'minutes, we would have', bac, 'bacterias')