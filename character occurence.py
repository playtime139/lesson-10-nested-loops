string = input("Please enter your chosen word: ")
char = input("please enter your chosen character: ")
i = 0
count = 0
while(i < len(string)):
    
    
    if (string[i] == char):
        count = count + 1
    i = i + 1

print("The total number of times", char, "has occured = ", count)