from notes import Notes
from calculator import Calculator
from timer import Timer
from alarm import Alarm


class Daisy:

    def __init__(self):
        self.user= input("What's your name: ")
        self.notes = Notes()
        self.calculator = Calculator()
        self.timer = Timer()
        self.alarm = Alarm()

    def run(self):
       print(f'Welcome, {self.user}!, i am Daisy!')
       while True:
        print("""DAISY
        1. Notes
        2. Calculator
        3. Timer
        4. Alarm
        5. Exit""")
        choice = input("Choose an option: ")
        if choice == "1":
            self.notes.note_menu()
        elif choice == "2":
            self.calculator.calculator()
        elif choice == "3":
            self.timer.timer()
        elif choice == "4":
            self.alarm.alarm()
        elif choice == "5":
            print("Goodbye. ,{self.user}")
            break
        else:
            print("Invalid option.")

