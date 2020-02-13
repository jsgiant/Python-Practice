def uncompress(s):
    i=0
    num,cstring="",""
    while(i<len(s)):
        num=""
        if(s[i].isdigit()):
            num+=s[i]
            j=i+1
            while(j<len(s)):
                if(s[j].isdigit()):
                    num+=s[j]
                else:
                    break
                j+=1
            i=j
            cstring+=s[i]*int(num)
        else:
            cstring+=s[i]
        i+=1
    return cstring
def compress(s):
    i=0
    string=""
    while(i<len(s)):
        count=1
        j=i+1
        if(j<len(s) and s[i]==s[j]):
            while(j<len(s)):
                if(s[j]==s[i]):
                    count+=1
                else:
                    break
                j+=1
            string+=str(count)+s[i]
            i=j
        else:
            string+=s[i]
            i+=1
    return string
if __name__=='__main__':
    #input
    for _ in range(int(input())):
        s=input()
        #print(compress(s))
        if(s.isalpha()):
            #print("hi")
            print(compress(s))
        else:
            print(uncompress(s))
