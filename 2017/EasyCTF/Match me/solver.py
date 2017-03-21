#https://www.youtube.com/watch?v=Qcv1IqHWAzg

import hashlib
def main(maleFile,femaleFile,reverse):
    #These -10000's and such are to pad the array,
    #so nth id represents nth index
    males = [[-10000]]
    maleIDNameMap = {}
    females = [[-10000]]
    femaleIDNameMap = {}
    loadData(males,maleIDNameMap,maleFile)
    loadData(females,femaleIDNameMap,femaleFile)
    #Format is that the man's index is there id, and inside is [x,y] where y is id of person they're paired with,
    # and x is his rank for that person, rank being 0-based
    manCurrentAssignments = [[1000000,-1000]]*len(males)
    unassignedWomenIDs = list(range(1,len(females)))
    while(len(unassignedWomenIDs) != 0):
        #use i, so I don't ahve to worry about modifying list while looping through it.
        i = len(unassignedWomenIDs) - 1
        while(i >= 0):
            womanID = unassignedWomenIDs[i]
            i-=1
            #pop so that I don't check same combo again later.
            nextPrefferedManID = females[womanID].pop(0)

            thisWomanPrefferenceRank = males[nextPrefferedManID].index(womanID)

            if(manCurrentAssignments[nextPrefferedManID][0] > thisWomanPrefferenceRank):
                # assign this woman to this man
                del unassignedWomenIDs[i+1]
                oldAssigneeID = manCurrentAssignments[nextPrefferedManID][1]
                if(oldAssigneeID==-1000):
                    #ezpz
                    manCurrentAssignments[nextPrefferedManID] = [thisWomanPrefferenceRank,womanID]
                else:
                    #gotta kick off old woman, and try everything in range 1... cur
                    #except I'm doing something clever and only keeping men she hasn't tried on listRef
                    #so program may just iterate a few more times. No recursive dealing with kicking off more
                    #and more women.
                    unassignedWomenIDs.append(oldAssigneeID)
                    manCurrentAssignments[nextPrefferedManID] = [thisWomanPrefferenceRank,womanID]

    output = []
    if(reverse):
        for i in range(1,len(males)):
            output.append([femaleIDNameMap[manCurrentAssignments[i][1]],maleIDNameMap[i]])
    else:
        for i in range(1,len(males)):
            output.append([maleIDNameMap[i],femaleIDNameMap[manCurrentAssignments[i][1]]])
    return output


def loadData(listRef,idRef,fname):
    lines = []
    with open(fname) as f:
        lines = f.readlines()

    i = 1
    for line in lines:
        elements = line.split(' ')
        idRef[i] = elements[0]
        tmp = []
        for k in range(1,len(elements)):
            tmp.append(int(elements[k][:-1]))
        listRef.append(tmp)
        i += 1


maleFirst   = main('male','female',False)
femaleFirst = main('female','male',True )

toMD5 = []
for i in maleFirst:
    for j in femaleFirst:
        if(i[0] == j[0]):
            if(i[1]==j[1]):
                toMD5.append(i)

# For MD5
md5String = ""
for i in toMD5:
    md5String += "(%s,%s)" %(i[0], i[1])
print(md5String)
md5 = hashlib.md5(md5String.encode()).hexdigest()
print(md5)
