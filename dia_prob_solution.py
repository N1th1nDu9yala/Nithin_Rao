Msg = input('enter the msg')# input function for reading the msg from the user
#Initialize variables
Compressed_msg = ""
index = 1
count = 1
# while loop for iterate over characters in the message
while index < len(Msg):
    if Msg[index] == Msg[index-1]:
        count += 1
        
    else:
        if count > 1:
            Compressed_msg += Msg[index - 1] + str(count)
        else:
            Compressed_msg += Msg[index - 1]
        count = 1
    index += 1

# Handling the last character in the message
if count > 1:
    Compressed_msg += Msg[-1] + str(count)
else:
    Compressed_msg += Msg[-1]

# Print the compressed message
print(Compressed_msg)  