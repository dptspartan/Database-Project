import random
databasename="HiveMind"
tablename="users"
feilds=""
data=""

USERNAME = []

with open("C:\\Shoaib\\Database-Project\\Raw Data\\users.txt", 'r') as file:
    line = file.readline()[:-1]
    feilds = line
    line = file.readline()[:-1]
    while line != "":
        line = line.split(',')
        data += "( " + line[0] + ","
        for i in line[1:]:
            data+= "\"" + i + "\","
        data += " ),\n"
        USERNAME.append(line[0])
        line = file.readline()[:-1]
    file.close


format = "INSERT INTO " + tablename + " ( " + feilds + " ) \n" + "Values " + data

with open("C:\\Shoaib\\Database-Project\\Raw Data\\usersout.txt", 'w') as file:
    file.write(format)
    file.close()

print(format)
print(USERNAME)

friends = []
for i in range(20):
    while True:
        x = random.randint(1, len(USERNAME))
        y = random.randint(1, len(USERNAME))
        if x == y:
            continue
        fnrd = {x,y}
        if fnrd not in friends:
            friends.append(fnrd)
            break
    
print("Friends list:",friends)

with open("C:\\Shoaib\\Database-Project\\Raw Data\\frndsout.txt", 'w') as file:
    id = 0
    data = "INSERT INTO friends\nVALUES "
    for i in friends:
        i = tuple(i)
        data += "(" + str(id)+","+ str(i[0])+","+ str(i[1])+"),\n"
    file.write(data)
    file.close()