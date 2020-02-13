import re
visa='^4(\d{12}|\d{15})$'
aexp='^3[47]\d{13}$'
mcard='^5[12345]\d{14}$'
disc='^6011\d{12}$'
for _ in range(int(input())):
    card=input()
    card = re.sub(r'[ -]',r'',card)
    if(re.match(visa,card)):
        print("Visa")
    elif(re.match(aexp,card)):
        print("American Express")
    elif(re.match(mcard,card)):
        print("MasterCard")
    elif(re.match(disc,card)):
        print("Discover")
    else:
        print("Unsupported Card")
