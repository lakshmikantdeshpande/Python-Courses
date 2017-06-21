# function with no parameters
def demo_function():
    print("Hello functions :)")
    return


demo_function()


# parameterized function
def param_function(str):
    print("You passed", str)
    return


param_function('sac')


# example of keyword parameters
def keyword_function(firstName, lastName=24):
    print("Hello ", firstName, lastName)
    return


keyword_function('sachin', 'd')
keyword_function(lastName='d', firstName='s')
keyword_function('s')


# variable arguments
def varargs(*name):
    for n in name:
        print(n)
    return


varargs('p')
varargs('a', 'b')
