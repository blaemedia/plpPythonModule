def divisible_by_ten(num):

    if num%10==0:
        return True
    else:
        return False


user=eval(input("Enter the base number: "))


print(divisible_by_ten(user))