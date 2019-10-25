"""
Reading and writing to files

"r" ---> Open file in read-only mode
"w" ---> Opens the file in write-only mode. And, or creates a new file
"w+" --> Opens a file in reading and writing mode

with-as statement --> Automatically closes the file for you
"""

"""
read_only = open("peanut.txt", "r")
print(read_only.read())
"""

"""
# Automatically closes file with "with-as"
with open("peanut.txt", "r") as file_name:
    print(str(file_name.read()))
"""

# using ".readline" feature
read_line = open("peanut.txt", "r")
# only read the first line
print(read_line.readline())
# will read the second if you add this
print(read_line.readline())
