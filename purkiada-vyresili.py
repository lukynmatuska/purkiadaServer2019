#file = open("C:\\Users\\buchmaier.jan\\Desktop\\finished_Users.txt")
file = open("finishedUsers\\finished_Users.txt")
read = file.readlines()
udelali = []
skoroudelali = []
for i in read:
    if "Done" in i and i.split(" ")[0] not in udelali:
        i = i.split(" ")
        udelali.append(i[0])

    else:
        i = i.split(" ")
        skoroudelali.append(i[0])
file.close()
print("-------------------------------------------")
print("           Udelali: {}".format(len(udelali)))
for i in udelali:
    print(i)
print("-------------------------------------------")
print("           Ziskali heslo admina:            ")
for i in skoroudelali:
    if i not in udelali:
        print(i)
if len(skoroudelali) == len(udelali):
    print("ALL USERS HAS DONE IT")



input(".: EXIT :.")