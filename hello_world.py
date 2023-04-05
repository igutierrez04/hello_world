# TASK 1 print "Hello World!"
print("Hello World!")

# TASK 2 print "Hello your name" with your name in a variable
name = "Rem"
print("Hello", name) # with a coma
print("Hello " + name) # with a +
print(f"Hello {name}") # f-string

# TASK 3 print "hello with a number" with the number stored in a variable
num = 4
print("Hello", str(num)) # with a coma
print("Hello " + str(num)) # with a +
print(f"Hello {4}") # f-string

# TASK 4 print "I love to eat 2 of your favorite foods" with the foods in a variable
food1 = "sushi"
food2 = "burritos"
print("I love to eat {} and {}".format(food1, food2)) # with .format()
print(f"I love to eat {food1} and {food2}")