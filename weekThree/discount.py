def calculate_discount(price, discount_percent):

    if discount_percent == 20 or discount_percent > 20:
        discount=price * discount_percent/100
        payPrice=price-discount
        return payPrice

    else:
        return price
    

OriginalPrice=eval(input("Enter the Price: "))
discountPer=eval(input("Enter the Percentage:   "))
    
print(calculate_discount(OriginalPrice,discountPer))