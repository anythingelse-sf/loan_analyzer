## A basic valuation tool to analyze microloans

1) Automate calculations
    a) Use the len() function to calculate the total number of loans in your lists
    b) Use the sum() function to calculate the total value of all the loans in your lists
    c) Use the sum of the loans divided by the total number of loans to get the mean price
    d) Print each calculation with a descriptive message (f strings)
2) Analyze loan data
    a) Use the get() funtion on a dictionary to extract 'future value' and 'remaining months'
    b) Apply the present value forumula to calculate the fair value of the loan if the discount rate is 20%
        - Present Value = Future value / (1+Discount Rate)**Time
    c) Write an if-else statment, aka a conditional statement
        - If the PV is >= than the cost, print "This loan is worth at least the cost to but it"
        - Else, print "This loan is too expensive and not worth the price"
3) Perform financial calculations on a new loan
    a) Define a new function to calculate present value.
        - The function should include:
            > Paramaters for 'future_value', 'remaining_months', and 'annual_discount_rate'
            > Returen 'present_value'
    b) For this exercise use an annual_discount_rate of 20%
4) Conditionally filter through lists of loans
    a) Create a new empty list to store your "inexpensive_loans"
    b) Use a for loop to iterate through the list of loans, filtering for loan_price <500
    c) Append each loan under $500 to the list of "inexpensive_loans"
    d) Print this list with a descriptive message
5) Save your results to a CSV
	a) Save the results for yourself in the Saved_Loans folder