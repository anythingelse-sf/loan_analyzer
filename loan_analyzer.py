
import csv
from pathlib import Path

"""Part 1: Automate the Calculations."""

loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
how_many_loans = len(loan_costs)

# Print the number of loans from the list
print("The number of loans from this list:", how_many_loans)

# What is the total of all loans?
total_of_all_loans = sum(loan_costs)

# Print the total value of the loans.
print("The total value of the loans:", total_of_all_loans)

# What is the average loan amount from the list?
average_loan_amount = total_of_all_loans / how_many_loans

# Print the average loan amount
print(f'The average loan amount is: {average_loan_amount: .0f}')


""" Part 2: Analyze Loan Data."""
#     @NOTE: If Present Value represents the loan's fair value (given the required minimum return of 20%), 
#               does it make sense to buy the loan at its current cost?

# Given the following loan data, calculate the present value for the loan below.
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use get() on the dictionary of additional information 
# Extract the Future Value and Remaining Months on the loan.
# Print each variable.
future_value = loan.get("future_value")
print("The Future Value is:", future_value)

remaining_months = loan.get("remaining_months")
print("There are", remaining_months, "months remaining")


# Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate. Use the **monthly** version of the present value formula.
present_value = future_value / (1+.2/12) ** remaining_months
print(f"The Present Value is {present_value: .2f}")


# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
loan_price = loan.get("loan_price")

if present_value >= loan_price:
    print(f'This loan is worth at least the cost to but it. The expected profits is ${present_value-loan_price: .2f}')
else:
    print(f'This loan is too expensive and not worth the price. We could expect to lose ${present_value-loan_price: .2f}')


"""Part 3: Perform Financial Calculations."""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
#    The function should return the `present_value` for the loan.

def calculate_present_value(new_loan):
    future_value = new_loan.get('future_value')
    remaining_months = new_loan.get('remaining_months')
    annual_discount_rate = .2
    present_value = future_value / (1+annual_discount_rate/remaining_months) ** 12
    return present_value

pv_new_loan = calculate_present_value(new_loan)

## Use the function to return present value of the new loan.
print(f"The present value of the new loan is: {pv_new_loan: .2f}")


"""Part 4: Conditionally filter lists of loans."""
#Filter through the loans provided to find loan prices under $500
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#Create an empty list called `inexpensive_loans`
inexpensive_loans = []

#Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for each_loan in loans:
    if each_loan["loan_price"] <= 500:   
## Add to our list
        inexpensive_loans.append(each_loan)

#print the `inexpensive_loans` list
print(f' Here is a list of inexpensive loans: {inexpensive_loans}!')


"""Part 5: Save the results. Output this list of inexpensive loans to a csv file"""

"""Set at the top of the code"""
# import csv
# from pathlib import Path

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path to save the file to the "Saved_Loans"
output_path = Path("Saved_Loans/inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())