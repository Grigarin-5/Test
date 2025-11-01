# open the file in read mode
with open("data.txt", "r") as file:
    # read and print each line one by one
    for line in file:
        # strip removes extra newline characters
        print(line.strip())
