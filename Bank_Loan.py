# Imports python libraries i need for this analysis
import pandas as pd
import matplotlib.pyplot as plt

# Displays the data in the bank loan file
bank_loan = pd.read_excel('Bank_loan.xls')
pd.set_option('display.max_columns', 114)
pd.set_option('display.max_rows', 114)
print(bank_loan)

# Displays the top (5) data and the bottom (5) data in the bank loan file
print(bank_loan.head(5))
print(bank_loan.tail(5))

# Displays all the column names in the bank loan file
print(bank_loan.columns)

# Displays the number of rows and columns we have in the bank loan file
print(f'Number of rows:', bank_loan.shape[0])
print(f'Number of columns:', bank_loan.shape[1])

# Displays the data type of our bank loan file
print(bank_loan.dtypes)

# Displays summary of the bank loan file
print(bank_loan.describe())

#Displays the total number of loan application in the bank loan file
total_loan_app = bank_loan['id'].count()
print(f'The total number of loan applications: ', total_loan_app)

# Displays the last time a loan was issued
latest_issue_date = bank_loan['issue_date'].max
#latest_year = latest_issue_date.year()
#latest_month = latest_issue_date.month()
#date_data = bank_loan[(bank_loan['issue_date'].dt.year() == latest_year) & (bank_loan['issue_date'].dt.month() == latest_month)]
#loan_application = date_data['id'].count()
print(f"The last date a loan was issued(for (latest_issue_date.strftime('%0 &Y))):loan_application)")

# Displays the total amount funded
total_funded = bank_loan['loan_amount'].sum()
total_funded_millions = total_funded / 1000000
print(f"Total Amount Funded: ${total_funded_millions:.2f}M")

#Displays the total amount received
total_received = bank_loan['total_payment'].sum()
total_received_millions = total_received / 1000000
print(f"Total Amount Funded: ${total_received_millions:.2f}M")

# Displays the average interest
Avg_interest = bank_loan['int_rate'].mean()
print(f"The Average Rate: {Avg_interest:.2f}%")

#Displays the Debt to income ratio
Avg_DTI = bank_loan['dti'].mean()
print(f"The Average Debt To Income Ratio: {Avg_DTI:.2f}%")

#Displays the Good loans
good_loans = bank_loan[bank_loan['loan_status'].isin(['Fully Paid', 'Current'])]
good_loans_app = good_loans['id'].count()
good_loan_funded = good_loans['loan_amount'].sum()
good_loan_received = good_loans['total_payment'].sum()

good_loan_million = good_loan_funded / 1000000
good_loan_received_millions = good_loan_received / 1000000
good_loan_percent = (good_loans_app / total_loan_app) * 100

print(f"Good Loan Applications: ", good_loans_app)
print(f"Good Loan Funded Amount: ${good_loan_funded}M")
print(f"Total Good Loan Received: ${good_loan_received_millions}M")
print(f"Good Loan Percentage: {good_loan_percent:.2f}%")

# Displays the bad loans
bad_loans = bank_loan[bank_loan['loan_status'].isin(['Charged Off'])]
bad_loans_app = bad_loans['id'].count()
bad_loan_funded = bad_loans['loan_amount'].sum()
bad_loan_received = bad_loans['total_payment'].sum()

bad_loan_million = bad_loan_funded / 1000000
bad_loan_received_millions = bad_loan_received / 1000000
bad_loan_percent = (bad_loans_app / total_loan_app) * 100

print(f"Bad Loan Applications: ", bad_loans_app)
print(f"Bad Loan Funded Amount: ${bad_loan_funded}M")
print(f"Total Bad Loan Received: ${bad_loan_received_millions:.2f}M")
print(f"Bad Loan Percentage: {bad_loan_percent:.2f}%")

# Displays the visual Analysis based on States
states = bank_loan.groupby('address_state')['loan_amount'].sum().sort_values(ascending=True)
state_funding = states / 1000

plt.figure(figsize=(8,6))
bars = plt.barh(state_funding.index,state_funding.values, color= 'Blue')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 9, bar.get_height() / 2,
             f'{width:,.0f}K', va = 'center', fontsize = 6)

plt.title('Total Amount Funded By State')
plt.xlabel('Funded Amount')
plt.ylabel('State')
plt.tight_layout()
plt.show()

# Displays the visual Analysis on Loan Term
term_funding = bank_loan.groupby('term')['loan_amount'].sum() / 1000000

plt.figure(figsize=(5,5))
plt.pie(
    term_funding,
    labels = term_funding.index,
    autopct = lambda d: f"{d:.1f}%\n${d*sum(term_funding) / 100:.1f}M",
    startangle = 90,
    wedgeprops = {'width': 0.4}
)
plt.gca().add_artist(plt.Circle((0, 0), 0.80, color='white'))
plt.title('Total Amount Funded By Term')
plt.show()

# Displays the visual Analysis on Loan Term
employee_funding = bank_loan.groupby('emp_length')['loan_amount'].sum().sort_values() / 1000000

plt.figure(figsize=(10,7))
bars = plt.barh(employee_funding.index,employee_funding, color= 'Green')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 5, bar.get_height() / 2,
             f'{width:,.0f}K', va = 'center', fontsize = 8)

plt.title('Amount Funded')
plt.xlabel('Total Funded Amount By Employee Lenght')
plt.grid(axis='x', linestyle = '--', alpha = 0.5 )
plt.tight_layout()
plt.show()

# Displays the visual Analysis on Loan Term
funding_purpose = bank_loan.groupby('purpose')['loan_amount'].sum().sort_values() / 1000000
plt.figure(figsize=(10,7))
bars = plt.barh(funding_purpose.index,funding_purpose, color= 'Red')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.1, bar.get_height() / 2,
             f'{width:,.2f}M', va = 'center', fontsize = 9)

plt.title('Total Amount Funded Due to Loan Purpose', fontsize = 14)
plt.xlabel('Amount Funded')
plt.ylabel('Loan Purpose')
plt.grid(axis='x', linestyle = '--', alpha = 0.5)
plt.tight_layout()
plt.show()