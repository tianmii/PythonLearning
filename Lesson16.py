# Filled list and EMPTY LIST
unconfirmed_avengers = ['captain america', 'thor', 'iron man', 'hulk']
confirmed_avengers = []
#length of the list is 4, evaluate on each turn until false
while len(unconfirmed_avengers) > 0:
    #Literally POPPING the unconfirmed list items INTO Current
    #BEcause the while condition is True
    current_avenger = unconfirmed_avengers.pop(0)
    print("Confirming avenger {x}...confirmed.".format(x=current_avenger))
    #appending the current avengers into confirmed
    confirmed_avengers.append(current_avenger)
# Returns as empty because the while condition ran through and emptied unconfirmed list
# looks like this:
# unconfirmed_avengers = []
# confirmed avengers = ['captain america', 'thor', 'iron man', 'hulk']
print("\nUnconfirmed avengers:")
for avenger in unconfirmed_avengers:
    print("- {y}".format(y=avenger))
print("\nConfirmed avangers:")
for avenger in confirmed_avengers:
    print("- {z}". format(z=avenger))



#####
current_numba = 1
#count up to 6, printing the number each time
while current_numba <= 6:
    print(current_numba)
#Very important line or else it runs forever without adding +1,
# it will print 1 forever
    current_numba += 1

current_numba = 3
while current_numba >= -4:
    print(current_numba)
    current_numba -= 1

print("Hello.")
print("Hello April")