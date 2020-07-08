
def findcountduplist(list):
    duplist = {}

    for i in list:
        if i in duplist:
            duplist[i]+=1
        else:
            duplist[i]=1
    
    keyvaluepair ={key:value for key,value in duplist.items() if value>1}
    return keyvaluepair

list = [2,3,4,4,5,2]

dupelem = findcountduplist(list)

for key,value in dupelem.items():
    print(key,':',value)