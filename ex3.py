file1 = open("C:\\Bhaskar\ex3.txt", 'w+')
print("the file in reality")
print(file1.read())
file1.write("\nthis is my addition and it is: PYTHON is FUCKING FUN ")
print("reading again after write")
file1.seek(0)
print(file1.read())
file1.close()
