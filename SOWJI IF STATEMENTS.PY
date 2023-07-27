#if statements:

price=100000
has_good_credit=True

if has_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(down_payment)
print(f"down_payment: {down_payment}")

#logicaloperators:

#IF APPLICANT HAS HIGH INCOME AND GOOD CREDIT ELIGIBLE FOR LOAN.
#HERE WE USED AND  OPERATOR.
has_high_income=True
has_good_credit=True

#we use two variables

if has_high_income and has_good_credit:

#here we use and operator that means both conditions are true

    print("eligible for loan")


#now we use or operator.for this operator atleast one condition is true.
has_high_income=True
has_good_credit=False


if has_high_income or has_good_credit:
    
    print("eligible for loan")

has_high_income=False
has_good_credit=False

if has_high_income or has_good_credit:
    print("eligible for loan")
#here no output because of the two conditions are false.

#AND=BOTH CONDITIONDS SHOULD BE TRUE
#OR=AT LEAST ONE CONDITION SHOULD BE TRUE
#NOT=IT REVERSE THE CONDITION

has_high_income=True
has_criminal_record=False

if has_high_income and not has_criminal_record:
#here we used not operator so it changes the false condition to true
    print("eligible for loan")

#COMPARISON OPERATORS:
#<,>,<=,>=,==,!=
name="j"
if len(name)< 3:
    print("name must be at least 3 characters")
elif len(name)> 5:
    print("name must be a maximum of 50 characters")
else:
    print("name looks good")

#WEIGHT CHANGES

weight=int(input('weight: '))
unit=input('(l)bs or (k)g: ')
if unit =="l":
    converted=weight * 0.45
    print(f"you are{converted} kilos")
else:
    converted=weight/0.45
    print(f"you are{converted} lbs")


#WHILE CONDITION:
i=1
while i<=5:
    print(i)
    i=i+1
print('done')

i=1
while i<=5:
    print('*'*i)
    i=i+1
print('done')



