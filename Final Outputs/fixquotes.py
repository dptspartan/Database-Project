import os
path = 'Final Outputs//'
for i in os.listdir(path):
    with open(path+i, 'r') as file:
        data = file.read()
        data = data.replace('\'', '\'')
        file.close()
    with open(path+i, 'w') as file:
        file.write(data)