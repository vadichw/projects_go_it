# \r
#print("vadimius", end= "\r")
#print(2001)



#start_ind = string.find("[")
#end_ind = string.find("]")
#new_string = string[:start_ind] + string[end_ind + 1:]

#string = "Виключити із цієї [групи] символи [розташовані між] дужками [, ]"

def sanitize(string):
    new_string = string[:]
    while True:
        start_ind = new_string.find("[")
        end_ind = new_string.find("]")
        if start_ind == -1:
            break
        new_string = new_string[:start_ind] + new_string[end_ind + 1:]
    return new_string
print(sanitize("Виключити із цієї [групи] символи [розташовані між] дужками [, ]"))