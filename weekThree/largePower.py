
def large_power(base,power):
    result = pow(base,power)

    if result > 5000:
        return True
    else:
        return False


nBase=eval(input("Enter the base number: "))
npower=eval(input("Enter the power number:   "))



print(large_power(nBase,npower))