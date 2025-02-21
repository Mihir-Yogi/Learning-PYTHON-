# open() => using open method you can open file.
# try and finally => using try and finally you can file errors handling 
# with as => using with as it also used to hendle error of file but only works on files   

file = open('Youtube_managment/test.md','w')

try:
    file.write("Hello World!")
finally:
    file.close()


with open('Youtube_managment/test2.md','w') as file:
    file.write("Hello User!")

