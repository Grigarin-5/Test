# open the file in read mode
with open("data.txt", "r") as file:
    # read the entire file content
    content = file.read()
    
    # split the text into words
    words = content.split()
    
    # count the number of words
    word_count = len(words)
    
    print("Total number of words:", word_count)
