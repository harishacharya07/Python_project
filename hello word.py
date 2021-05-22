def reverseCheck(number):
    originalNum= number
    reverseNum = 0


    while(number > 0):
        reminder = number % 10
        reverseNum = (reverseNum * 10) + reminder


        if(originalNum == reverseNum):
            return True
        else:
            return False


print("original and reverse number is")
print(reverseCheck(121))

print("hello word ")


print("steel quantity estimation")
print("hello word")
