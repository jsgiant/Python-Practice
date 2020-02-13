#Python
import re
n,m=list(map(int,input().split(' ')))
org = []
for _ in range(n):
    org.append(input())
final = ""
for i in range(m):
    for j in range(n):
        final+=(org[j][i])
#exp = re.compile(r'(?<=\w)([!@#$%^&\*/\s]+)(?=\w)')
#final = re.sub(r'(?<=\w)([!@#$%^&\*/\s]+)(?=\w)',' ',final)
final = re.sub(r'\b[\W]+\b',r' ',final)
print(final)

#Sample Input
'''Input:
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

Output:
This is Matrix#  %!
'''
