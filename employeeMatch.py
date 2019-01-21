import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter


#IF NOT MATT SPARROW, change file path name to the location on your computer, make sure not to mix up the two
#Table length of 289k
list1 = pd.ExcelFile(r"C:\Users\Matthew Sparrow\Documents\datasets\university-of-california-2017.xlsx")
#Table length of 22.3k
list2 = pd.ExcelFile(r"C:\Users\Matthew Sparrow\Documents\datasets\useraaddqwdqfqegent.timelapse_table.xlsx")
#Table length of 20k
#list2 = pd.ExcelFile(r"C:\Users\Matthew Sparrow\Documents\datasets\matt1_table.xlsx")

#Parse excel data
df2 = pd.read_excel(list2, 0)
df1 = pd.read_excel(list1, 0)

normalList2 = list()
normalList1 = list()

print('Excel Files Read')

for j in range(1, len(df2)):
   # flagSmall = 0
    #for k in range(0, 6):
    #Extract only the first name columns from directories in order to match names



    #Confirm that first name entry from both lists will print out
    #print(nameList2)
    #print(nameList1)
    #if(flagSmall == 0):
   # flagSmall = 1
    nameList2 = df2.iloc[j, 0]
    #Set flags for name finding
    flag1 = 0
    flagLast = 0
    flagLast2 = 0
    fl2Space = -1

    idx = -1

    firstLetter = 0

    for i in range(0, len(nameList2)):
        if(nameList2[i] != ' ' and nameList2[i-1] == ' ' and flag1 == 0):
            flag1 = 1
            firstLetter = i

        if(nameList2[i-1] == ',' and flagLast == 0):
            idx = i
            flagLast = 1

        #if(flagLast == 1 and nameList2[i] == ' '):
        if(flagLast == 1 and flagLast2 == 0 and (ord(nameList2[i]) >= 65 and ord(nameList2[i]) <= 122)):
            flagLast2 = 1
            #fl2Space = i

        if(flagLast2==1 and nameList2[i] == ' '):
            fl2Space = i
            break


    lastName = nameList2[firstLetter:(idx-1)]

    if(flagLast2 == 1):
        firstName = nameList2[(idx+1):fl2Space]
    else:
        firstName = nameList2[(idx+1):len(nameList2)]

    #print('parsing of small file name')
    #print(firstName)
    #print('First name printed')
    #print('first name is'+firstName)
    normal = (firstName + lastName).lower()
    normalList2.append(normal)
    #print(normal + ' Small-File')
print("List 2 normalized, " + str(len(df2)) + " entries found")
for j in range(1, len(df1)):
    nameList1 = df1.iloc[j, 0]
    flag2 = 0

    idx2 = -1

    firstSpace = -1

    for i in range(0,len(nameList1)):
        if(nameList1[i] == ' ' and flag2 == 0):
            flag2 = 1
            idx2 = i
            firstSpace = i
        if(nameList1[i] == ' '):
            idx2 = i

    lastName2 = nameList1[(idx2+1):len(nameList1)]
    firstName2 = nameList1[0:firstSpace]

    #print('Parsing of large file name')
    #print(firstName2)
    normal2 = (firstName2+lastName2).lower()
    normalList1.append(normal2)
    #print(normal2 + ' Large-File')

print("List 1 normalized, " + str(len(df1)) + " entries found")
matchCount = 0
print('Sorting...')
normalList1.sort()
normalList2.sort()

print("Checking for matches...")
for j in range(0,len(normalList2)):
    found = 0
    first = j
    last = len(normalList1) - 1
    while first <= last and found == 0:
        midpoint = (first + last) // 2
        if(normalList2[j] == normalList1[midpoint]):
            matchCount = matchCount + 1
            #print(str(matchCount) + ' ' + normalList2[j])
            found = 1
        else:
            if normalList2[j] < normalList1[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

print(str(matchCount) + ' matches found')
