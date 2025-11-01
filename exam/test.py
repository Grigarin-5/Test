user = str(input("Enter a word : "))
with open("ex.txt","r") as file :
    r = file.read()
    i = r.split()
    count = 0 
    for t in i:
        for user in i:
            if user in t :
                count += 1
    print(count)