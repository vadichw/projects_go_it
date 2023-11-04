def is_valid_pin_codes(pin_codes):
    if not pin_codes:
        return False

    list = set(pin_codes)

# Перевірка на дублікати та валідність пін-кодів
    if len(list) != len(pin_codes):
        return False
    for pin_codes in list:
        if len(pin_codes) != 4 or not pin_codes.isdigit():
            return False

    return True
    

    







print(is_valid_pin_codes(["1111", "2123"]))