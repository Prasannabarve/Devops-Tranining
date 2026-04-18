# ATM Withdrawal Script

## Overview

This is a simple Python script that simulates an ATM withdrawal system. It validates user input based on basic banking rules and displays appropriate messages for successful or failed transactions.

## Features

* Ensures the withdrawal amount is greater than 0
* Allows only multiples of 500
* Checks for sufficient account balance
* Displays remaining balance after a successful withdrawal
* Handles invalid inputs with clear error messages

## Code Structure

### Function: `atm_withdrawal(withdrawal_amount)`

This function processes the withdrawal request.

#### Parameters:

* `withdrawal_amount` (int): The amount the user wants to withdraw

#### Logic:

1. Sets a fixed account balance of 5000
2. Validates:

   * Amount must be greater than 0
   * Amount must be a multiple of 500
   * Amount must not exceed available balance
3. If all checks pass:

   * Deducts amount
   * Displays success message and remaining balance
4. Returns:

   * `True` if withdrawal is successful
   * `False` if any validation fails

## How to Run

1. Make sure Python is installed on your system
2. Save the script to a file, for example: `atm.py`
3. Run the script:

```bash
python atm.py
```

4. Enter the withdrawal amount when prompted

## Example

```
Enter withdrawal amount: 1500
Withdrawal successful. Amount: 1500
Remaining balance: 3500
```

## Error Cases

| Condition            | Message                                          |
| -------------------- | ------------------------------------------------ |
| Amount ≤ 0           | Error: Withdrawal amount must be greater than 0  |
| Not multiple of 500  | Error: Withdrawal amount must be multiple of 500 |
| Insufficient balance | Error: Insufficient balance. Available: 5000     |

## Notes

* The balance is hardcoded (5000) for demonstration purposes
* No persistent storage or real banking integration is included

## Future Improvements

* Add user authentication
* Connect to a database for dynamic balance tracking
* Support deposit and balance inquiry features
* Add a graphical user interface (GUI)

## License

This project is free to use for learning and educational purposes.
