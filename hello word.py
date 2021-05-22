def reversecheck(number):
    originalnum= number
    reversenum = 0


    while(number > 0):
        reminder = number % 10
        reverseNum = (reversenum * 10) + reminder


        if(originalnum == reversenum):
            return True
        else:
            return False


print("original and reverse number is")
print(reversecheck(121))

print("hello word ")


print("steel quantity estimation")
print("hello word")
