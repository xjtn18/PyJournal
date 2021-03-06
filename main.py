# main script to start the journal
from journal import *
from constants import *

def parse_command(c : str, jn : Journal) -> None:
    # check what the command is and if its valid
    global EXIT_JOURNAL, SAVE_ON_EXIT

    if c is "q":
        EXIT_JOURNAL = True # set the global exit flag to true
        SAVE_ON_EXIT = yes_no("Do you want to save your changes to the journal?")

    elif c is "w":
        jn.add_entry()

    elif c is "s":
        jn.show_journal()

    elif c is "f":
        search_str = input("Enter search phrase: ")
        indexes = jn.get_entries_with(search_str, whole_word = yes_no("Whole word only?"))
        if indexes: # matches found
            jn.show_entries(indexes)
        else:
            print("No matches found")
            pause(PAUSE_TIME)
    
    elif c is "d":
        try:
            entry_id = int(input("Enter the ID of the entry you want to remove: "))
            jn.remove_entry(entry_id)
        except ValueError:
            print("Not a valid integer ID")
            pause(PAUSE_TIME)

    elif c is "h":
        print("Commands:")
        for info in COMMAND_INFO:
            print(info)
        print("")

    else: #invalid command
        print("not a valid command; type 'h' for list of commands")
        pause(PAUSE_TIME)


def command_loop() -> None:
    print("Type 'h' for list of commands\n")

    # main command loop
    while not EXIT_JOURNAL:
        command = input("~")
        screen_clear()
        parse_command(command, jn)


    if SAVE_ON_EXIT:
        pickle.dump(jn,open(JRNL_FILENAME, 'wb')) # store the journal
        print("Journal saved.")
    else:
        print("Changes discarded.")

    


if __name__ == "__main__":
    # load journal if it exists, else create it
    if os.path.isfile(JRNL_FILENAME):
        jn = pickle.load(open(JRNL_FILENAME, 'rb'))
        print("Journal loaded.")
    else: # first time creating the journal
        jn = Journal()
        print("No journal found. Fresh journal created.")

    command_loop() # run the command loop


