# Defining your own functions
# for example, the print function print 2 lines


def thanks(name):
    print(f"Thanks, I hate it, {name}.")
    print("You did it.\n")


thanks('Jesse')
thanks('Wallace')
thanks('Yolanda')

# --------------- Two different methods of sorting a list -------------
# First method
trio = ['harry', 'hermione', 'ron']
trio.sort()
print("The Hogwarts trio in alphabetical order.")
for people in trio:
    print(people.title())
trio.sort(reverse=True)
print("\nOur Hogwarts trio in reverse alphabetical order.")
for people in trio:
    print(people.title())


# Second Method
def show_trio(message, people_person):
    print(message)
    for person in people_person:
        print(person.title())


people = ['harry', 'hermione', 'ron']
people.sort()
show_trio("\nOur Howarts trio in alphabetical order.", trio)
trio.sort(reverse=True)
show_trio("\nOur Hogwarts trio in reverse alphabetical order.", trio)


# --------------Cleaner code, defined 'show_trio()'-------------------
# Gave a list and message with a loop
# After defining, can sort list and call function
# Gabe's note: Order of importance>
# def function_name([1]important_variable, [2]less_variable)

# -------------Returning a value--------------
# Takes in a numerical value and returns
# Word corresponding to that number
# added else clause when python sees a
# number out of range
def get_numba_word(numba):
    if numba == 0:
        return 'zero'
    elif numba == 1:
        return 'one'
    elif numba == 2:
        return 'two'
    elif numba == 3:
        return 'three'
    else:
        return "I'm sorry. I don't know that numba."


for current_numba in range(0, 6):
    numba_word = get_numba_word(current_numba)
    print(current_numba, numba_word)


# Greeter
# WRITE A FUNCTION: person name and greeting
# Store 3 names in a list
# call function in a for loop

def show_names(message):
    for name in names:
        print(message.format(kirby_name=name.title()))


names = ['kirby', 'waddle dee', 'meta knight']
show_names(
    # names,
    "Hello {kirby_name}, citizen of Popstar!"
)


# Original def "def show_names(names, message):"
# But took out b/c it did nothing


# Full names
def fullname_message(message):
    for name in full_names:
        print(message.format(full_name=name.title()))


full_names = ['frodo baggins', 'homer simpson', 'peter quill']
fullname_message(
    "Hello, {full_name}."
)
