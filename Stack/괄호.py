T = int(input())
res=[]
Data=[]

for _ in range(T):
    Question = input()
    Data.append(Question)


for i in Data:
    count = 0
    res_count = True
    for j in i:
        if count == 0:
            if j == ')':
                res.append('NO')         
                res_count = False   
                break
        if j == '(':
            count += 1
       
        if j == ')':
            count -= 1
    if res_count  != False:
        if count == 0:
            res.append('YES')
        else:
            res.append('NO')


print(res)