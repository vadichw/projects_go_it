def get_name(name):
    name = input("Enter name ")
    return name
def greet(name):
    print(f"Hello, my Lord {name}")
def main():
    name = get_name()
    greet(name)