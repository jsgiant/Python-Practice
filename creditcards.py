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

      

    #Second method
    import re
nums = []
for _ in range(int(input())):
    string = input()
    copy = re.sub(r'([\s,-]+)',r'',string)
    if not(re.search(r'^[4-6]',string)):
        print("Invalid")
    elif(re.match(r'^[4-6]([0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$',string)):
        if(re.search(r'(\d)\1{3}',copy)):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")
    '''elif(re.match(r'^[4-6]([0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})',string)):
        print("Valid")'''
