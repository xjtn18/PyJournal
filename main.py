# main script to start the journal
from os import system, name
import os.path
import pickle
import time
from datetime import datetime
from re import search
import helper
from constants import *
from journal import *


def pause(sec : float):
    time.sleep(sec)


def screen_clear():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def yes_no(question : str) -> bool:
    while True:
        response = input(question + " (y/n) ")
        if response not in 'yn':
            print("invalid: 'y' or 'n'")
            pause(PAUSE_TIME)
            continue
        return response == 'y'


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
        entry_id = int(input("Enter the ID of the entry you want to remove: "))
        jn.remove_entry(entry_id)

    elif c is "h":
        print("Commands:")
        for info in COMMAND_INFO:
            print(info)
        print("")

    else: #invalid command
        print("not a valid command; type 'h' for list of commands")
        pause(PAUSE_TIME)


def command_loop() -> None:
    # load journal if it exists, else create it
    if os.path.isfile(JRNL_FILENAME):
        jn = pickle.load(open(JRNL_FILENAME, 'rb'))
        print("Journal loaded.")
    else: # first time creating the journal
        jn = Journal()
        print("No journal found. Fresh journal created.")

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

    pause(PAUSE_TIME)
    


if __name__ == "__main__":
    command_loop()


