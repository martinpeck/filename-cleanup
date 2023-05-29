import os

filename = "ignore.txt"

while len(filename) != 0:
    filename = input("Enter text: ")
    filename = filename.lower().replace(" ", "-")
    
    cmd = 'echo %s | tr -d "\n" | pbcopy' % filename
    os.system(cmd)  
    print(filename)
