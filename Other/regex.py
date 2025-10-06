from re import *
pattern = compile( '(^|) [-a-z]+@([-a-z]) + [a-z] {2, 6} (| $)' )

def get_pass():
    address = input("Enter address: ")
    is_valid = pattern.match(address)

    if is_valid:
        print("Valid: ", is_valid.group())
    else:
        print("Invalid")
get_pass()