# **kwargs => It used to take key and values in the function as a argument.

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    
print_kwargs(name = "superhero", power = "lazer" )
print_kwargs(name = "superhero", power = "lazer" , villen = "supervillen" )

