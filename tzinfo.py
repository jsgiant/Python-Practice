import datetime
for _ in range(int(input())):
    dt=input()
    if(len(dt.split())==5):
        #print("hey")
        dt+=' +0000'
    dt=datetime.datetime.strptime(dt,"%a %d %b %Y %H:%M:%S %z")
    timezone=input()
    if(timezone[0]!='+' and timezone[0]!='-'):
        timezone='+'+timezone
    timezone=datetime.datetime.strptime(timezone,"%z")
    dt2=dt.astimezone(timezone.tzinfo)
    dt2=datetime.datetime.strftime(dt2,"%a %d %b %Y %H:%M:%S %z")
    print(dt2)
'''import os
#os.system("cd var")
os.system("ls")'''
