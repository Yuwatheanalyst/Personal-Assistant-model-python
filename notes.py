#ToDO:
#improve the delete notes in whichever order
# display notes in order
#store username inside notes object

class Notes:
    def note_menu(self):
        while True:
            print("1. create notes")
            print("2. view notes")
            print("3. delete notes")
            print("4. back to main menu")
            choice = input("whats your selection: ")
            if choice == '1':
                self.new_note()
            elif choice == '2':
                self.view_notes()
            elif choice == '3':
                self.delete_notes()
            elif choice == '4':
                break
            else:
                print(f"I dont understand you")

    def new_note(self):
        note = input("whats on your mind?: ")
        with open("data/note.txt", "a") as note_file:
            note_file.write(note + 'n')
            print('understood')

    def view_notes(self):
        with open("data/note.txt", "r") as note_file:
            notes = note_file.read()
            if notes == " ":
                print("you haven't told me anything")
            else:
                print('YOUR NOTES HERE')
                print(notes)

    def delete_notes(self):
        confirm = input("Do you really want to delete? (y/n): ")
        if confirm.lower() == 'y':
            with open("data/note.txt", "w") as note_file:
                notes = note_file.write("")
                print('All is forgotten')
        else:
            print("we will talk about again later")

