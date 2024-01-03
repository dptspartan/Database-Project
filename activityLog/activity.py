from random import shuffle
with open("../posts/postsOut.txt", "r") as file:
    data = file.readlines()

activityStringsList=[]
count="#"
for i in data[2:]:
    splittedData=i.split(", ")
    username=splittedData[1]
    activitySummary= "'You made a post'"
    finalString = f"( {count}, {username}, {activitySummary}), \n"
    activityStringsList.append(finalString)

with open("../posts/commentsOut.txt", "r") as file:
    data = file.readlines()

activityLog= ""
for i in data[2:]:
    splittedData=i.split(", ")
    username=splittedData[1]
    activitySummary= "'You made a comment'"
    finalString = f"( {count}, {username}, {activitySummary}), \n"
    activityStringsList.append(finalString)




with open("../posts/likesOut.txt", "r") as file:
    data = file.readlines()

activityLog= ""
for i in data[2:]:
    splittedData=i.split(", ")
    username=splittedData[1]
    activitySummary= "'You liked a post'"
    finalString = f"( {count}, {username}, {activitySummary}), \n"
    activityStringsList.append(finalString)

shuffle(activityStringsList)
counter=0
activityLog= "INSERT INTO activityLog( activityId, userName, activitySummary )\n VALUES "
for i in range(len(activityStringsList)-1):

    activityStringsList[i]=activityStringsList[i].replace("#", str(counter))
    print(activityStringsList[i])
    activityLog+=activityStringsList[i]
    counter+=1

with open("activityLog.txt", "w") as file:
    file.write(activityLog)
