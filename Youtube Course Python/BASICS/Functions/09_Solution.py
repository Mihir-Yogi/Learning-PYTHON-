# yield => this keyword simmiler as return keyword but it dose not terminate the function exucution.

def even(n):
    for i in range(2,n+1,2):
        yield i

for i in even(10):
    print(i)