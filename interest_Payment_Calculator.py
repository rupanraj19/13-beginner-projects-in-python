# collect the necessary inputs: principal, apr, years
# calculate the monthly payment
# show the user

def main():
    print("This is monthly payment calculator")
    print("")

    principal = float(input("Input the loan amount:"))
    apr = float(input("Input the annual interest rate:"))
    years = int(input("Input the number of years:"))

    monthly_interest = apr/1200
    months = years * 12
    monthly_payment = principal * monthly_interest / (1 - (1 + monthly_interest) ** (-months)) # formula for monthly payment

    print("Monthly payment for this loan: %.2f"  % (monthly_payment))


main()