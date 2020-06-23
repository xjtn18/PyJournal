from datetime import datetime
from re import search
from helper import *
from constants import *


class Entry():
    def __init__(self, text):
        self.text = text
        self.date_time = datetime.now()


class Journal():
    def __init__(self):
        self.entries = []

    def add_entry(self) -> None:
        print("Write your journal entry below; press enter when you're done:")
        self.entries.append(Entry(input()))

    def show_journal(self) -> None:
        print("All journal entries:\n")
        for e in self.entries:
            print(e.date_time.strftime("%m/%d/%Y %H:%M"))
            print(e.text + "\n")

    def show_entry(self, idx) -> None:
        e = self.entries[idx]
        print(e.date_time.strftime("%m/%d/%Y %H:%M"))
        print(e.text + "\n")

    def show_entries(self, indexes) -> None:
        print("")
        for i in indexes:
            self.show_entry(i)

    def get_entries_with(self, search_str : str, whole_word = False) -> [int]:
        indexes = [] # stores the indexes of the journal entries that contain the search string
        search_string = add_escapes(search_str) # add the escape sequences in case keyword contains regex sensitive symbols
        if whole_word:
            search_string = ' ' + search_string + ' ' # add white space at front and end of keyword
        for n in range(len(self.entries)):
            e = self.entries[n]
            if search(search_string, e.text): # if this entries text contains the search string
                indexes.append(n)
        return indexes

    def remove_entry(self, entry_id : int):
        # removes the entry with the given index (input expected to be 1-indexed) from the journal
        if 0 < entry_id <= len(self.entries): # if the ID is valid
            del self.entries[entry_id - 1]
            print(f"Deleted journal entry {entry_id}")
        else:
            print("ID invalid")


