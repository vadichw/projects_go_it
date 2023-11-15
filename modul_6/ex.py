# Alex Korp,3000
#Nikita Borisenko,2000
#Sitarama Raju,1000


def total_salary(path):
    salary = 0.0
    fh = open(path, 'r')
    line = fh.readline()
    
    while line:
        name, sumy = line.strip().split(',')
        salary += sumy
        return salary
    fh.close()
    
print(total_salary('text.txt'))