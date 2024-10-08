#!/usr/bin/python3
"""
Add all arguments to a Python list, and then save them to a file.
"""


import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing items if the file exists
items = load_from_json_file(filename) if os.path.exists(filename) else []
# Add all arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
