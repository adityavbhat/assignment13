while True:
    try:
        age = int(input("Enter age: "))
        if age < 18:
            raise AgeTooSmallError
        break
    except AgeTooSmallError:
        print("Age should be more than 18")
    except ValueError:
        print("Age should be an integer")

class AgeTooSmallError(Exception):
    pass
