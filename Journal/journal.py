# Prompt used: A simple application made in python that allows people to add comments or write journal entries. It can allow comments or not and timestamps for all entries
# Also used: Also make the script read from a specific file and add the stuff from the file to entries

import datetime

# Journal class to hold journal entries
class Journal:
  def __init__(self):
    # Initialize an empty list to store entries
    self.entries = []
  
  # Method to add an entry to the journal
  def add_entry(self, entry, comments=None):
    # Get the current timestamp
    timestamp = datetime.datetime.now()
    
    # If comments are provided, add them to the entry
    # Otherwise, set the comments to an empty string
    if comments:
      entry_with_comments = f"{entry}\nComments: {comments}"
    else:
      entry_with_comments = f"{entry}\nComments: "
    
    # Add the entry with comments and timestamp to the journal
    self.entries.append(f"{timestamp}: {entry_with_comments}")
  
  # Method to show all entries in the journal
  def show_entries(self):
    # Loop through all entries and print them
    for entry in self.entries:
      print(entry)

# Create a new instance of the Journal class
journal = Journal()

# Read the entries from the file
with open("entries.txt") as f:
  # Loop through all lines in the file
  for line in f:
    # Split the line into the entry and comments (if provided)
    entry, *comments = line.strip().split("|")
    
    # Add the entry and comments (if provided) to the journal
    journal.add_entry(entry, " ".join(comments))

# Show all entries in the journal
journal.show_entries()

# This code is similar to the previous example, but it adds a new step to read the entries from a file. The file should contain one entry per line, with the entry and comments (if provided) separated by a | character.
# To use this code, save the entries in a file named entries.txt and run the script. It will read the entries from the file and add them to the journal, and then print all entries in the journal.