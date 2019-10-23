# try and except
"""
if you have an exception for a type of error, good for testing
by adding int() in the input method, that will mean it will ask
for a whole number
I added a finally to loop back until the user has answered correctly
"""
def get_user_info():
    try:
        str1 = input("First Name: ")
        int2 = int(input("Age: "))
        print(f"Hi {str1}. Your age is {int2}.")
    except ValueError:
        print("Please put an integer for your value.")
    finally:
        str1 = input("First Name: ")
        int2 = int(input("Age: "))
        print(f"Hi {str1}. Your age is {int2}.")

get_user_info()
