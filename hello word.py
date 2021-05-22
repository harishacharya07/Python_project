def reverse(number):
    original_number = number
    reverse_number = 0

    while number > 0:
        reminder = number % 10
        reverse_number = (reverse_number * 10) + reminder

        if original_number == reverse:
            return True
        else:
            return False


print("original and reverse number is")
print(reverse(121))
print("hello word ")
print("steel quantity estimation")
print("hello word")
