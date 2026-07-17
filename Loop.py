# Loop :
#     Loop is iterative object which use to execute code based on condition.
#     It will execute the code until the condition is true and when condition is false compiler
#         will execute code outsode of the loop if written.

#     Types of loop :
#         while :
            # While loop is use when we need to iterate the code based on some condition.
            # We need to manually increase the numbers otherwise it will end with infinite loop.
            # Infinite loop is something which is never end until user manually break it.

            # Syntax :
                # while condition:
                #     Execution code
                #     Incremental Number

            # Example :
i = 0
while i < 6:
    print(i)
    i += 1

print("End of loop")

# Infinite loop
# a = 0
# while a < 6:
#     print(a)

# Break:
#    Break statement stop the loop execution and execute code outside of the loop.
#    We can use the break statement with or without condition or with any other statement.

    # Example :
print("With break statement")
j = 0
while j < 6:
    print(j)
    j += 1
    break

h = 0
while h < 6:
    break
    print(h)
    h += 1

print("Loop end with break statement")

# Continue :
#   Continue statement use to execute the loop continue but when condition fulfill with that
#       it will skip that statement and jump to the next statement.

    # Example 
k = 0
while k <= 6:
    if k == 5: 
        k+= 1       
        continue   
    print(k)
    k += 1


#         for