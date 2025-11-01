# open the file in read mode
with open("data.txt", "r") as file:
    # read all lines into a list
    lines = file.readlines()
    
    # count how many lines
    line_count = len(lines)
    
    print("Total number of lines:", line_count)
