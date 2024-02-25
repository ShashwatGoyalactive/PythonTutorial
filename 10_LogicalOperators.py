has_high_income = True
has_good_credit = True
# and or not
if has_high_income and has_good_credit :
    print("Eligible for loan")
elif has_high_income or has_good_credit:
    print("Loan may be granted")
else:
    print("Loan will not be granted")