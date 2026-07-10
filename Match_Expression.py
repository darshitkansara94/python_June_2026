# Match :
#     Match condition is simar to the if..elif..else. But it is more simplified version to write
#         multiple conditions.
#     In match we need to write a condition once and based on that case get executed.

#     Syntax :
#         match expression:
#             case 1:
#                 pyton statement
#             case 2 :
#                 python statement
#             .
#             .
#             case n:
#                 python statement            

#       Example :

number = 3

if number == 1:
    print("Number is equal to 1")
elif number == 2:
    print("Number is equal to 2")
elif number == 3:
    print("Number is equal to 3")
elif number == 4:
    print("Number is equal to 4")
else:
    print("Number is equal to 5")

print("With match expression")

match number:
    case 1: # 3 == 1
        print("Number is equal to 1")
    case 2: # 3 == 2
        print("Number is equal to 2")
    case 3: # 3 == 3
        print("Number is equal to 3")
    case 4:
        print("Number is equal to 4")
    case 5:
        print("Number is equal to 5")

fruit = "Mango"

match fruit: # We can convert into lower case or pipe symbol.
    case "Banana" | "banana":
        print("Fruit is Banana")
    case "mango" | "Mango" | "MANGO":
        print("Fruit is Mango")
    case "Apple":
        print("Fruit is Apple")
    case _:
        print("Invalid choice")

if fruit == "Banana":
    print("Fruit is Banana")
elif fruit == "Mango":
    print("Fruit is Mango")
elif fruit == "Apple":
    print("Fruit is Apple")
else :
    print("Invalid")

marks = int(input("Enter marks :"))

match marks: #85
    case m if marks >= 90 and marks <=100: # 85 >= 90 And 85 <= 100 = false
        print("Grade A")
    case m if marks >= 75 and marks <= 89: # 85 >= 75 And 85 <= 89 = true
        print("Grade B")
    case m if marks >= 65 and marks <= 74:
        print("Grade C")
    case m if marks >= 55 and marks <= 64:
        print("Grade D")
    case m if marks >= 35 and marks <= 54:
        print("Grade E")
    case m if marks < 35:
        print("Grade F")
    case _:
        print("Invalid choice")

