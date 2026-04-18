print('hellow world')
def atm_withdrawal(withdrawal_amount):
    current_balance = 5000

    if withdrawal_amount <= 0:
        print("Error: Withdrawal amount must be greater than 0")
        return False

    if withdrawal_amount % 500 != 0:
        print("Error: Withdrawal amount must be multiple of 500")
        return False

    if withdrawal_amount > current_balance:
        print(f"Error: Insufficient balance. Available: {current_balance}")
        return False

    remaining_balance = current_balance - withdrawal_amount
    print(f"Withdrawal successful. Amount: {withdrawal_amount}")
    print(f"Remaining balance: {remaining_balance}")
    return True

withdrawal_amount = int(input("Enter withdrawal amount: "))
atm_withdrawal(withdrawal_amount)
