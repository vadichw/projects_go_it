from random import randint

def get_random_password():
    password = ""

    for i in range(8):
        random_pass = chr(randint(40, 126))
        password += random_pass
    return password


def is_valid_password(password):
    #if not password:
        #return False
    if len(password) != 8:
        return False
    
    big = False
    small = False
    num = False
    
    for element in password:
        if element.isupper():
            big = True
        elif element.islower():
            small = True
        elif element.isdigit():
            num = True

    #big = any(i.isupper() for i in password)
    #small = any(i.islower() for i in password)
    #num = any(i.isdigit() for i in password)

    return big and small and num

def get_password():
    max_attempts = 100
    attempts = 0 
    while attempts < max_attempts:
        password = get_random_password()
        if is_valid_password(password):
            return password
        attempts += 1

print(get_password())

