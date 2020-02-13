import json
l1=[]
data={}
li=[]
for _ in range(int(input())):
    l1=input().split(';')
    if l1[0]not in data:
        data[l1[0]]=[0]*5
    data[l1[0]][0]+=1
    if l1[1] not in data:
        data[l1[1]]=[0]*5
    data[l1[1]][0]+=1
    if l1[2]=='win':
        data[l1[0]][1]+=3
        data[l1[0]][2]+=1
        data[l1[1]][4]+=1
    elif l1[2]=='loss':
        data[l1[1]][1]+=3
        data[l1[1]][2]+=1
        data[l1[0]][4]+=1
    elif l1[2]=='draw':
        data[l1[0]][1]+=1
        data[l1[1]][1]+=1
        data[l1[0]][3]+=1
        data[l1[1]][3]+=1
#print(data)
data=dict(sorted(data.items()))
#data=dict(data)
#print(data)
data=dict(sorted(data.items(),key=lambda x:x[1][1],reverse=True))
#data=dict(data)
l2=[]
for k,v in data.items():
    dic={}
    dic["Team"]=k
    dic["Matches Played"]=v[0]
    dic["Total Points"]=v[1]
    dic["Won"]=v[2]
    dic["Tied"]=v[3]
    dic["Lost"]=v[4]
    l2.append(dic)
#l2=sorted(dict(l2).items(),key=lambda  x:x[0]['Team'])
#print(l2)
final =json.dumps(l2,indent=4)
print(final)
