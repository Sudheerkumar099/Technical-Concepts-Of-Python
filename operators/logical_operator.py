high_income = True
good_credit = False
student = False
if high_income and good_credit and not student:
    print("Eligible for loan")
elif high_income or good_credit:
    print("Maybe eligible for loan")
elif not high_income:
    print("Not eligible for loan")
else : 
    print("Unknown")
   