#Loan Calculator by Michael Keleti



princ = float(input("How much money did you borrow?\n"))
year = float(input("How many years are required to pay back the loan?\n"))
frate = float(input("What is the annual interest rate on your loan?\n"))
mont = year*12
rate = frate/12
payment = ((1+rate)**mont * princ * rate)/((1+rate)**mont-1)
print(payment)

##Outputs different value than intended

