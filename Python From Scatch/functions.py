def function(a, b):
    return a * b


# So what is happening here?
# def = function
# function = the name of the function
# parameters: a, b
# return a * b

# The way I think a function is, is basically a place to put reusable code
# to define a function use the *def* keyword followed by the function's name
# the parameters are things which can be accessed for certain reasons in this example its for multiplication
# the param a = 5 and b = 10. so the function will return / give you in return 5 X 10 = 50. it would return 50

# to use a function you have to call it ↓ ↓ ↓
function(5, 10)
# Input 5 and 10 ^^

# SIDENOTE I DIDN'T KNOW HOW TO EXPLAIN SO IN THE BUG SECTION OF GITHUB PUT A SUGGESTION OR SOMETHING IN THERE

# I will give another example on how a function is worked

questionA = input("What is a?")
questionB = input("What is b?")

# FUNCTIONS DO NOT HAVE TO HAVE THE RETURN STATEMENT
def multiply(a, b):
    print(a * b)
    return a * b
