def fopen2(filename):
    file = open(filename, "w")
    file.write("Hello Python Programming...")
    file.close()

def fopen1(filename):
    with open(filename, "w") as f:
        f.write("Hello Python Programming...")


#fopen1("basic3.txt")
#fopen2("basic4.txt")


#read
def fread(filename):
    with open(filename, "r") as f:
        contents = f.read()
    return contents


print(fread("basic3.txt"))
