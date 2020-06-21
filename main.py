# main script to start the journal
from os import system, name
import os.path
import pickle
import time
from datetime import datetime
from re import search
import helper

# Constants
JRNL_FILENAME = 'journal.pkl'
EXIT_JOURNAL = False
SAVE_ON_EXIT = True


class Entry():
    def __init__(self, text):
        self.text = text
        self.date_time = datetime.now()


class Journal():
    def __init__(self):
        self.entries = []

    def add_entry(self) -> None:
        print("Write your journal entry below; press enter when you're done")
        self.entries.append(Entry(input()))

    def show_journal(self) -> None:
        print("\nAll journal entries:\n")
        for e in self.entries:
            print(e.date_time.strftime("%m/%d/%Y %H:%M"))
            print(e.text + "\n")

    def show_entry(self, idx) -> None:
        e = self.entries[idx]
        print(e.date_time.strftime("%m/%d/%Y %H:%M"))
        print(e.text + "\n")

    def find_substr(self, search_str : str) -> [int]:
        indexes = [] # stores the indexes of the journal entries that contain the search string
        for n in range(len(self.entries)):
            e = self.entries[n]
            if search(search_str, e.text): # if this entries text contains the search string
                indexes.append(n)
        for i in indexes:
            self.show_entry(i)

def screen_clear():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def yes_no(question : str) -> bool:
    while True:
        response = input(question + " (y/n) ")
        if response is "y":
            return True
        elif response is "n":
            return False
        else:
            print("invalid: 'y' or 'n'")
            time.sleep(0.75)


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
        jn.find_substr(search_str)
    elif c is "h":
        print("\nCommands:", "'q' to close journal", "'s' to show journal", "'w' to add to journal", sep = "\n")
        print("")
    else: #invalid command
        print("not a valid command; type 'h' for list of commands")
        time.sleep(0.75)


def command_loop() -> None:

    # load journal if it exists, else create it
    if os.path.isfile(JRNL_FILENAME):
        jn = pickle.load(open(JRNL_FILENAME, 'rb'))
        print("Journal loaded.")
    else: # first time creating the journal
        jn = Journal()
        print("No journal found. Fresh journal created.")

    print("Type 'h' for list of commands")

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

    time.sleep(1)



if __name__ == "__main__":
    command_loop()


