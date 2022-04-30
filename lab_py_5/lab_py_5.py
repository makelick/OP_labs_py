from BankAccount import *

n = int(input("Enter the number of bank accounts: "))
currents = []
deposits = []
init_arrays(n, currents, deposits)
check_deposits(n, currents, deposits)
print_accounts(n, currents, deposits)
