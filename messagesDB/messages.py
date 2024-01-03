# def read_usernames_from_file(filename):
#     with open(filename, 'r') as file:
#         lines = file.readlines()
    
#     # Strip whitespace and split lines into lists of usernames
#     username_lists = [line.strip().split(',') for line in lines]
    
#     return username_lists

# # Example usage:
# filename = 'friendsList.txt'  # Replace with your actual file name
# usernames_list = read_usernames_from_file(filename)

# # Print the result
# for usernames in usernames_list:
#     usernames.pop()
#     print(usernames)

# with open("messages.txt", "r") as f:
#     data = f.readlines()
#     print(data)

# listOfWord=data[61].split(",")
# word1=listOfWord[1]
# word2=listOfWord[2]
# print(word1,word2)
# usernameNum=3
# for i in range(60,100):
#     data[i]= data[i].replace(word1,usernames_list[usernameNum][0])
#     data[i]= data[i].replace(word2,usernames_list[usernameNum][1])

# with open("messages.txt", "w") as f:
#     f.writelines(data)



# with open("messages.txt", "w") as f:
#     data=f.readlines

# with open("messages.txt", "r") as f:
#     data=f.readlines()
#     print(data)
#     for i in range(len(data)):
#         splitted = data[i].split(",")
#         splitted.pop(0)
#         data[i]= f'{str(i+1)},{",".join(splitted)}'
    
# with open("messages.txt", "w") as f:
#     f.writelines(data)
        


line='INSERT INTO messages( messageId,senderId, receiberId,message,time)\n VALUES '
with open("messagesDB\messages.txt", 'r') as file:
    data = file.readlines()
id = 0
for i in data:
    splitted = i.split(",")
    line += f"( {id}, "

    line += f"'{splitted[1]}', "
    line += f"'{splitted[2]}', "
    line += f"'{','.join(splitted[3:-1])}', "
    line +=f"'{splitted[-1][:-1]}' ), \n"
    id+=1

with open("messagesOut.txt", "w") as file:
    file.write(line)

