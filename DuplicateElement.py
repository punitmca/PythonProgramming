def getDuplicatesWithCount(listOfElems):
    dictOfElems = {}

    for i in listOfElems:
        if i in dictOfElems:
            dictOfElems[i]+=1
        else:
            dictOfElems[i]=1

     di ={key:value for key, value in dictOfElems.items() if value>1}
    return di

list = [1,1,2,3,2]

d= getDuplicatesWithCount(list)

for key, value in d.items():
    print(key, ':' ,value)