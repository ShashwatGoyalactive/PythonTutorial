# if , elif , else

is_hot = False
is_cold = False

if is_hot:
    print("It is a hot Day!!")
    print("Drink plenty of water")
elif is_cold:
    print("It is a cold Day!!")
    print("Wear warm clothes")
else:
    print("Its a lovely Day")
# print("What are your ideas on Day?")


# If the credit score of a buyer of house($1M) is good then they put down 10% else they put down 40%

price_of_house = 1000000
has_good_creditScore = True

if has_good_creditScore:
    down_payment = 0.1 *price_of_house
else:
    down_payment = 0.4*price_of_house
print(f'down_payment : {down_payment}')