# Example file for Advanced Python: Language Features by Joe Marini
# The assignment expression operator := (or the "walrus" operator)

import pprint


# regular assignment statements assign a value
x = 5
print(x)

# TODO: the assignment operator is part of an expression
# while (thestr := input("Value? ")) != "exit":
#     print(thestr)

# TODO: The assignment expression is useful for writing concise code


# TODO: The walrus operator can help reduce redundant function calls
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
val_data = {
    "length": (l := len(values)),
    "total": (s := sum(values)),
    "average": s / l
}
pprint.pp(val_data)
# pep 572
