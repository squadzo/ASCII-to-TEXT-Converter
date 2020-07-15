msg = input("Enter Your ASCII Number: ")
msg = msg.split()

text = ""
for i in msg:
    text += chr(int(i))
    
print("Result is : {}".format(text))
