import random
databasename="HiveMind"
tablename="users"
feilds=""
data=""

USERNAME = []

with open("users.txt", 'r') as file:
    line = file.readline()
    feilds = line
    line = file.readline()
    while line != "":
        data += "( " + line + " ),\n"
        line = line.split(',')
        USERNAME.append(line[0])
        line = file.readline()
    file.close


format = "INSERT INTO " + tablename + " ( " + feilds + " ) \n" + "Values " + data

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