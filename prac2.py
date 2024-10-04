def genaratePass(m) :
    if(len(m) >10) :
        length = len(m)
        ascii_value = ord(m[0])
        uppercase_last_three = m[-3 : 0].upper()
        lowercase_first_four = m[ : 4].lower()
        special = '@' * (length - 7)
        password = f'{length}{ascii_value}{uppercase_last_three}{lowercase_first_four}{special}'
        print(password)
        
genaratePass('Sheikh Negar')