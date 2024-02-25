def example_function(a, b, c):
    print(a, b, c)
    
    
example_function(1, 2, 3) # positional arguments
example_function(a=1, b=2, c=3) # keyweord arguments


# a and b must be passed as positional arguments, c is optional
def example_function_2(a, b, /, c): 
    print(a, b, c)
    
    
example_function_2(1, 2, c=3) 


# after * everything most be keyword argument
def example_function_3(a, b, *, c):
    print(a, b, c)
    
    
example_function_3(1, 2, c=3) 