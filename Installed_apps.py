import winapps
#kjo librari kqyre vetem appet qe i keni te instaluar ne krejt userat



#winapps.searching_installed google chrome
index = 0 
thisdict = {}

for item in winapps.list_installed():
    thisdict[item.name] = item.version


for i in thisdict:
    index += 1
    print(index, i)
