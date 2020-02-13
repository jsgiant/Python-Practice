from collections import defaultdict
A=defaultdict(int)
B=defaultdict(int)
prod=defaultdict(int)
for _  in range(int(input())):
    p,c=map(int,input().split())
    A[p]=c
for _  in range(int(input())):
    p,c=map(int,input().split())
    B[p]=c
m=len(A)
n=len(B)
for i in range(m): 
    for j in range(n): 
        prod[i + j] += A[i] * B[j]; 
flg=False
for k,v in(sorted(prod.items(),key=lambda x:x[0],reverse=True)):
    if v!=0:
        if v>0:
            if flg:
                print(" + ",end="")
        else:
                print(" - ",end="")
        print(abs(v),end="")
        if(k!=0):
            print(f"x^{k}",end="")
        flg=True
