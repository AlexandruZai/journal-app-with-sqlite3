# Personal journal app with Python and SQLite3

from database import create_table, add_entry, get_entries
menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit

Your selection: """

welcome = "Welcome to your personal personal_journal_app_with_sqlite3"
create_table()
def prompt_new_entry():
    entry_content = input("What have you learned today? ")
    entry_date = input("Enter the date: ")
    add_entry(entry_content, entry_date)

def view_entries(entries):
    for entry in entries:
        print(f"{entry[1]}\n{entry[0]}\n\n")

print(welcome)
user_input = input(menu)
while user_input != '3':
    if user_input == '1':
        prompt_new_entry()
    elif user_input == '2':
        view_entries(get_entries())
    else:
        print("Invalid option, please try again!")

    user_input = input(menu)
