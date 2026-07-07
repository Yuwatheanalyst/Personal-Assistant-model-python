from notes import note_menu
from calculator import calculator
from timer import timer
from alarm import alarm

name= input("whats your name?: ")


def menu(name):
    print(f"welcome {name}")
    print("what do you want to do?")
    print("1. Notes")
    print("2. Calculator")
    print("3. Timer")
    print("4. Alarm")
    print("5. Exit")
    print("select an option: ")
    return input(" ")
while True:
 choice = menu(name)
 if choice == '1':
    note_menu(name)
 elif choice == '2':
     calculator()
 elif choice == '3':
    timer()
 elif choice == '4':
     alarm()
 elif choice == '5':
    break
print(f"Hate to see you go",name)

