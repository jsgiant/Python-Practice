n = int(input())
nums =[1000 , 900, 500 , 400,
      100,90,50,40,
      10,9,5,4,
      1
     ]
roman =['M' , 'CM' , 'D' , 'CD',
        'C' , 'XC' , 'L' , 'XL',
        'X' ,'IX' ,'V' , 'IV',
        'I'
    ]
i = 0
roman_number =""
while(n>0):
    while(n >= nums[i]):
        roman_number+=roman[i]
        #print(n,nums[i],roman[i])
        n-=nums[i]
    i+=1
print(roman_number)

#sample I/O
Input:
1990

Output:
MCMXC
