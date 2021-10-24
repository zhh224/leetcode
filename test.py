import itertools
all_lis = (x for x in list(itertools.permutations(range(1,10),9)))
#print(all_lis)
i = 0
new_rows = []
for rows in all_lis:
    if rows[0]+rows[4]+rows[8]==rows[2]+rows[4]+rows[6]==15:
        row1 = rows[:3]
        row2 = rows[3:6]
        row3 = rows[6:]
        i +=1
        for i in range(3):
            index = 0
            if sum(row1)==sum(row2)==sum(row3)==sum([row1[i],row2[i],row3[i]])==15:
                index = 1
        if index:
            if len(set(row1)&set(row2))==0:
                new_rows.append([row1,row2,row3])
    else:
        pass    
print(len(new_rows))  
for row in new_rows:  
    for i in row:
        print(i)
    print('\n')

