load_and_reverse_index.py: Loads cvs data into Firebase and creates a reverse index for the events i.e. Dinner, Lunch, etc. To change the reverse index, take this script and change the index variable on line 34.

To Run: python load_and_reverse_index.py menu-136.csv

simple_search.py: uses key word search to find menus (or records more generally) with events with any of the inputted key words. The search looks at the direct children of each menu. To search deeper, change the get call on line 14.

Run: python simple_search.py “dinner breakfast”