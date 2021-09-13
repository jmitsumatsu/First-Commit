#declare variables to store values for the following:
First_Name = 'Joshua'
Last_Name = 'Mitsumatsu'
Favorite_color = 'Blue'
Favorite_Meal = ("Chinese Food")

#print out a sentence in Python that references your variables and say "My First Name is.....My Last Name is.....
# My favorite color is.....and my favorite meal is".

#Repeat this using:
    #a. F-String

print(f"my first name is {First_Name} my last name {Last_Name} my favorite color is {Favorite_color} my favorite meal is {Favorite_Meal}")
    
    #b. Concatenation

solution = "my first name is " + First_Name + " my last name is " +  Last_Name + " my favorite color is " + Favorite_color + " my favorite meal is " + Favorite_Meal + "."
print(solution)
    
    #c. Argument by Position

solution2 = "My first name is {0} my last name is {1} my favorite meal is {2} my favorite color is {3}.".format('Joshua','Mitsumatsu','Blue','chinese')
print(solution2)
    
    #d. Argument by Name

solution3 = "My first name is {a} my last name is {b} My favorite color is {c} My favorite food is {d}".format(a='joshua',d="Chinese food",b='mitsumatsu',c='blue')
print(solution3)