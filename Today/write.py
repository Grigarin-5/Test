# open the file in append mode and add text
with open("notes.txt", "a") as file:
    file.write("\nThis is an appended line.")


# now open again to read and display content
with open("notes.txt", "r") as file:
    content = file.read()
    print("Full content of notes.txt:\n")
    print(content)
