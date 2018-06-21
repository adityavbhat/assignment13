a=3
if a<4:
    try:
        a=a/(a-3)
        print(a)
        '''Try'''
    except ZeroDivisionError:
        print("Not possible")
        #Exception 
