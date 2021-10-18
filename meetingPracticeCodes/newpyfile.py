# Variables Needed

# Deposit Amount -- DELETE
# Withdrawal Amount -- DELETE
# Intreast
# Starting fees
# Balance ***
# ID Number 

idNumber = 1394
idnumber = 4832 #not camel case
x = 4829 #bad

balance = 339.29
annualInterestRate = 1.18
#bank account was made in 2000
#pay me.

# balance * (1.08 * 21)

newBalance = balance * (annualInterestRate * 21)

#function: makes yo code simple cuz you dont gotta repeat it a bunch
def balance(bal):
    roundedBalance = round(bal, 2)
    return roundedBalance

balance = balance(newBalance)

print("you got $", newBalance)
print("you got $", balance)
#round, int, str, max/min, etc.


