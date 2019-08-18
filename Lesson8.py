#For loop on strings of indv letters
says = "Hebdo"
for x in says:
    print(x)

#Slicing strings
says = "What's a habwaded?"
first = says[:4]
last = says[-4:]
print(first, last)

#"in" keyword to find a particular 
#substring in a string, "false" or "true" output

says = "I like toitles and kets."
x = 'kets' in says
print(x)


###How to print if return is false and add a sentence
#saying "I like eating ____. Says no one."
says = "I like pancaeks and donutts."
x = 'olives' in says
print(x)

#index of substring
says = "I like Ann and waffles."
index = says.find('waffles')
print(index)

#Replace substring
says = "I like Witcher and Skyrim, but I'd much rather play Witcher."
says = says.replace('Skyrim', 'Pokemon')
print(says)

#Counting substring
says = "I like Geralt and Cirilla, Geralt and Ciri make a good team."
x = says.count('Geralt')
print(x)

#Splitting strings
#let python format the string into a list format
games = "stardew valley, pokemon, binding of isaac"
games = games.split(',')
print(games)

###Exercise###
#Listing a sentence
says = "Me gey."
for x in says:
    print (x)

#Sentence list
says = "DAT ASS IS THICC"
x = list(says)
print (x)

