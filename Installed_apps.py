import winapps
#check all apps that u have installed in your pc or laptop



#winapps.searching_installed google chrome
index = 0 
thisdict = {}

for item in winapps.list_installed():
    thisdict[item.name] = item.version


for i in thisdict:
    index += 1
    print(index, i)
