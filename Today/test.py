with open("data.txt", "r") as file:
    r = file.readlines()  # Read all lines
    r.reverse()            # Reverse the list in place

with open("copy.txt", "w") as file:
    file.writelines(r) 