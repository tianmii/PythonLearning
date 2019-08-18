#functions from before
#learning that functions need a name or default values
def prints_message(pokemon):
    print("\nYou caught a {new_pokemon}!".format(new_pokemon=pokemon.title()))

#
prints_message('haunter')
prints_message('rowlett')
prints_message('blaziken')
#prints_message()
# WILL GET ERROR: prints_message() missing 1 required
# positional argument: 'pokemon'

### even more specific version
# will have a positional argument with a default value
# and no error if () is left empty!
def prints_evo_message(name='pokemon'):
    print("{new_pokemon} evolved!".format(new_pokemon=name.title()))

prints_evo_message('ghastly')
prints_evo_message('torchic')
prints_evo_message('rowlett')
prints_evo_message()

#positional arguments, works if you follow the set order

def print_monster_info(monster_name, monster_class, monster_type):
    print("\nMonster: {monster_name}".format(monster_name=monster_name.title()))
    print("Class: {monster_class}".format(monster_class=monster_class.title()))
    print("Type: {monster_type}\n".format(monster_type=monster_type.title()))

print_monster_info('gore magala', 'flying wyvern', 'frenzy virus')
print_monster_info('tigrex', 'wyvern', 'none')
print_monster_info('zinogre', 'quadraped wyvern', 'electric')
# when you print and have the order wrong, python doesnt know that
# for example
print_monster_info('flying wyvern', 'rathalos', 'fire')


#### a better version, more readble and you write it in any order......

def print_new_monster_info(monster_name, monster_class, monster_type):
    print("\nMonster: {monster_name}".format(monster_name=monster_name.title()))
    print("Class: {monster_class}".format(monster_class=monster_class.title()))
    print("Type: {monster_type}\n".format(monster_type=monster_type.title()))

print_new_monster_info(
    monster_name='deviljho',
    monster_class='brute wyvern',
    monster_type='dragon',
)


# lesson from gabe when eventually your function gets more complicated than printing simple statements
# if there is math involved, you want to seperate into class
from dataclasses import dataclass

@dataclass
class MonsterInfo:
    name: str
    m_class: str
    m_type: str


def print_new_monster_info_dc(monster_info: MonsterInfo):
    print("\nMonster: {monster_name}".format(monster_name=monster_info.name.title()))
    print("Class: {monster_class}".format(monster_class=monster_info.m_class.title()))
    print("Type: {monster_type}\n".format(monster_type=monster_info.m_type.title()))


print_new_monster_info_dc(
    MonsterInfo(
        name='deviljho',
        m_class='brute wyvern',
        m_type='dragon',
    )
)


# arbitrary number of arguments
def subtracter(num_1, num_2):
    sum = num_1 - num_2
    print("The sum of the numbers is {numsum}.".format(numsum=sum))

subtracter(999, 363)
subtracter(-7, 2)
subtracter(-50,-60)

# accepting a sequence of arbitrary length
# if place argument at end list of arguments with an *
# argument will collect any remaing values from the
# calling statement into a tuple
def example_function(arg_1, arg_2, *arg_3):
    print('\narg_1:', arg_1)
    print('arg_2:', arg_2)
#for loop to process the remaining arguments after arg_2
    for value in arg_3:
        print('arg_3 value:', value)

example_function(1, 2)
example_function(1, 2, 3)
example_function(1, 2, 3, 4)
example_function(1, 2, 3, 4, 5)
example_function(-1, 0, 1, 2)


#### TUPLE ####
# stores the first value in the calling statement in the argument num_1
# stores the second value in the calling statement in the argument num_2
# stores all other values in the calling statement as a TUPLE in the argument nums
# we can "unpack" these values
def subtracter2(num_1, num_2, *nums):
    sum = num_1 - num_2
    for num in nums:
        sum = num - sum
    print("\nThe sum of your numbers is {final_sum}".format(final_sum=sum))

subtracter2(1, 2, 3)
subtracter2(-4, -3, -2)
subtracter2(50, 20, 70)

##### KWARGS #########
#### Accepting an arbitrary number of key-value arguments
## key-values stored in a dictionary and looped
# Two asteriks '**' tells Python to collect all remaing
def example_function_kwarg(arg_1, arg_2, **kwargs):
    print('\narg_1:', arg_1)
    print('arg_2:', arg_2)
    # dealing with Tuples, only cared about value, not key
    # replaced 'key' vairable with '_' so no linting problem
    # yellow squiggle of an unued variable
    for _, value in kwargs.items():
        print('arg_3 value:', value)

        #
example_function_kwarg('a', 'b')
example_function_kwarg('a', 'b', value_3='c')
example_function_kwarg('a', 'b', value_3='c', value_4='d')


################
