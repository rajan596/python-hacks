# python3
# file operations

# write mode
text="Oh here \nI have made a simple file document\n"
file=open('file.txt','w')
file.write(text)
file.close()

# append mode
appendText="This text will be appended\n"
file=open('file.txt','a')
file.write(appendText)
file.close()

# reading from file
file=open('file.txt','r')
text=file.read()
print(text)

# reading line by line and store as a list
file=open('file.txt','r')
text=file.readlines()
print(text)
