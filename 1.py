f = open(" \nexample.txt", "a+")
f.write("This is read and write ")
f.seek(0)
print(f.read())
f.close()

