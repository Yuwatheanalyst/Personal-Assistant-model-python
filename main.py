from notes import note_menu
name= input("whats your name?: ")
def menu():
    print(f"welcome {name}")
    print("what do you want to do?")
    print("1. Notes")
    print("2. Calculator")
    print("3. Timer")
    print("4. Alarm")
    print("5. Exit")
    print("select an option: ")
    return input(" ")

def calculator():
    pass
def timer():
    pass
def alarm():
    pass
choice = menu()
if choice == '1':
    note_menu()
if choice == '2':
    pass
