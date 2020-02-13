import textwrap
n=int(input())
lines=[]
for word in textwrap.wrap(input(),n):
    lines.append(word.split())
#print(lines)
for i in range(len(lines)-1):
    space=n-sum(len(words) for words in lines[i])
    while(space>0):
        for j in range(len(lines[i])-1):
            lines[i][j]+=" "
            space-=1
            if(space<=0):
                break
for i in range(len(lines)-1):
    for words in lines[i]:
        print(words,end="")
    print()
print(" ".join(lines[-1]).ljust(n))
#print('\n'.join(string))
