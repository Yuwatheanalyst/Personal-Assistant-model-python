#ToDO:
#improve the delete notes in whichever order
# display notes in order


def note_menu():
    print("1. create notes")
    print("2. view notes")
    print("3. delete notes")
    print("4. back to main menu")
    choice = input("whats your selection: ")
    if choice == '1': new_note()
    elif choice == '2': view_notes()
    elif choice == '3': delete_notes()
    elif choice == '4':
        return
    else: print("invalid input")
def new_note():
    note = input("whats on your mind: ")
    with open("data/note.txt", "a") as note_file:
        note_file.write(note +'n')
        print('understood')
def view_notes():
    with open("data/note.txt", "r") as note_file:
          notes = note_file.read()
          if notes == " ":
              print("you haven't told me anything")
          else:
            print('YOUR NOTES HERE')
            print(notes)
def delete_notes():
  confirm=input("Do you really want to delete? (y/n): ")
  if confirm.lower() == 'y':
       with open("data/note.txt", "w") as note_file:
        notes = note_file.write("")
        print('All is forgotten')
  else:print("we will talk about again later")
