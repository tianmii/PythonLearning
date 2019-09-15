kitties = 5
while kitties > 1:
    print(f"{kitties} kitties jumping on the wall, {kitties} kitties jumping on the wall.")
    print("One takes a pounce,")
    kitties = kitties - 1
    if kitties == 1:
        print(f"{kitties} kitty jumping on the wall!\n")
        print(f"{kitties} kitty jumping on the wall, {kitties} kitty jumping on the wall.")
        print("One takes a pounce,")
        print("No more kitties jumping on the wall!")
    elif kitties > 2:
        print(f"{kitties} kitties jumping on the wall!\n")


