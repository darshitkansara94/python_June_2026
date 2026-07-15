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


#         for