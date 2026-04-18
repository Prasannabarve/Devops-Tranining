


# Login Authentication System
A Python program that validates user login credentials based on security rules.

# How to Run
python3 login_auth.py

# Logic
Takes username and password as input
Validates credentials in order
Stops at first failure

# Validations (in order)
Username must be at least 5 characters
Password must be at least 8 characters
Password must contain at least one digit (0-9)

Example
Success Case:

Enter username: john_doe
Enter password: Pass1234
Login successful


Failure Cases:

Enter username: john
Enter password: Pass1234
Error: Username must be at least 5 characters

Enter username: john_doe
Enter password: Pass
Error: Password must be at least 8 characters

Enter username: john_doe
Enter password: Password
Error: Password must contain at least one digit
Returns

# Result	Return      Value
All validations pass	True

Any validation fails	False