import random
databasename="HiveMind"
tablename="users"
feilds=""
data=""
# -----------------------------USERS---------------------------------
USERNAME = []

with open("Raw_Data/users.txt", 'r') as file:
    line = file.readline()[:-1]
    feilds = line
    line = file.readline()[:-1]
    while line != "":
        line = line.split(',')
        data += "( "
        for i in line:
            data+= "\"" + i + "\","
        data += " ),\n"
        USERNAME.append(line[0])
        line = file.readline()[:-1]
    file.close


format = "INSERT INTO " + tablename + " ( " + feilds + " ) \n" + "Values " + data

with open("usersout.txt", 'w') as file:
    file.write(format)
    file.close()

print(format)
print(USERNAME)
# ------------------------------FRIENDS-------------------------------------------------------------
friends = []
for i in range(20):
    while True:
        x = random.randint(0, len(USERNAME)-1)
        y = random.randint(0, len(USERNAME)-1)
        if x == y:
            continue
        fnrd = {USERNAME[x],USERNAME[y]}
        if fnrd not in friends:
            friends.append(fnrd)
            break
print("Friends list:",friends)

with open("friendsList.txt", "w") as f:
    for i in friends:
        for j in i:
            f.write(j)
            f.write(",")
        f.write("\n")


with open("frndsout.txt", 'w') as file:
    id = 0
    data = "INSERT INTO friends\nVALUES "
    for i in friends:
        i = tuple(i)
        data += "(" + str(id)+","+ "\"" + str(i[0]) + "\"" +","+ "\"" + str(i[1])+ "\"" +"),\n"
        id+=1
    file.write(data)
    file.close()



# -------------------------------------FRIEND REQUESTS----------------------------------------

friendsReq = []
for i in range(20):
    while True:
        x = random.randint(0, len(USERNAME)-1)
        y = random.randint(0, len(USERNAME)-1)
        if x == y:
            continue
        fnrd = {USERNAME[x],USERNAME[y]}
        if fnrd not in friends and fnrd not in friendsReq:
            friendsReq.append(fnrd)
            break
print("FriendReq list:",friends)

with open("frndsReqout.txt", 'w') as file:
    id = 0
    data = "INSERT INTO friendsReq\nVALUES "
    for i in friendsReq:
        i = tuple(i)
        data += "(" + str(id)+","+ "\"" + str(i[0]) + "\"" +","+ "\"" + str(i[1])+ "\"" +"),\n"
        id+=1
    file.write(data)
    file.close()



# ----------------------------------MESSAGES---------------------------------------
    
# with open("messages.txt", "r") as f:
#     # data = f.readlines()
#     with open("./friendsList.txt", "r") as j:
