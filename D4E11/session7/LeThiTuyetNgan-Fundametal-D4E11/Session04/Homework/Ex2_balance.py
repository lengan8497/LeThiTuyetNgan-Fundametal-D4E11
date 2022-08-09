input_balance = int(input('Enter your balance: '))
def place_value(input_balance): 
    return ("{:,}".format(input_balance)) 
  
print('Your updated balance: $',place_value(input_balance))