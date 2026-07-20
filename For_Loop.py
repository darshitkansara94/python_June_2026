# For :
#     For loop is use to iterate a values just like a while loop.
#     Using for loop we cab iterate value for tuple, disctionary or list.
#     In for loop we don't need to increment number manually instead for loop handle this thing by itself.

#       Syntax :
            # for loop_var_name in var_name:
            #     python statement

# Example :
list = ["Potato","Tomato"]
i = 0
while i < len(list):
    print(list[i])
    i += 1

print("Loop Ends")

for listitem in list:
    print(listitem)

# Range :
# Range method use to iterate a loop no of time that is provide by user or system.
# Default starting index of range method is 0.

# Example :
for i in range(6):
    print(i)
print("With manual range")

for j in range(2,6):
    print(j)

print("Dynamic generation")
numberofcontrol = int(input("Enter values to generate control : "))
for k in range(numberofcontrol):
    print("Control generated", k) 

print("Print dictionary keys")
person = {
    "name" : "Harshil",
    "age" : 23,
    "address" : "Vadodara"
}

for keys in person.keys():
    print(keys)

for values in person.values():
    print(values)

print("Access keys and values")
for keys,values in person.items():
    print(keys, "->", values)    
