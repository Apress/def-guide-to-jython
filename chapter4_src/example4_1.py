def plus_five(func):
    x = func()
    return x + 5
    
@plus_five
def add_nums():
    return 1 + 2
    
    