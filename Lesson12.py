# rating through EVERY item in the list, that's
# the first answer was wrong "50"
# if statement is a branching statements is a tool
# lets you execute conditional logic in your program
# conditional in this case is based on truthiness of the statement
# boolean means a value that is true or false
# current_value = current_value + 5 VS
# current_value += 5 (special assignment statement)

aliens = ["r", "g", "b", "g", "b", "r", "r", "b", "g", "b"]
current_score = 0
for alien in aliens:
    if alien == "r":
        current_score += 5
    if alien == "g":
        current_score += 10
    if alien == "b":
        current_score += 15
print(current_score)
print()
# While loop
# Tests the initial condition, if condition is true
# loop starts executing. Everytime loop finishes, the
# condition is reevaluated. As long as the condition
# remains true, the loop keeps executing until false.

# initial condition
# game_active = True
# set up while loop
# while game_active:
# run the game. at some point game ends
# game_active will be set to false. loop ends.
# Do anything else you want done after loop runs

energy = 5
while energy > 0:
    print(f"Your power is {energy}.")
    energy = energy - 1
print("\nOh no, you're ded. Stay determined!")

strength = 5
while strength < 12:
    print(f"Your current power is {strength}.")
    strength += 2
print("\nYou're too strong.")

# input function "input('')" = standard input or TERMINAL interaction
# standard output is printing something
# botw = ["link", "zelda", "sidon"]
# new_botw = input("please tell tell me someone I should know:")
# botw.append(new_botw)
# print(botw)


#

botw = ["link", "zelda", "sidon"]
done = False
while not done:
    new_botw = input("Please tell tell me someone I should know in botw:")
    if new_botw == "mario":
        done = True
    else:
        botw.append(new_botw)
        print(botw)

#
