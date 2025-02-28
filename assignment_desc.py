#
# Test case 1 :- Successful Registration
# Steps:
# Open the registration page.
# Enter a valid username, email, and password.
# Click on the Register button.
# Verify the success message and redirection to the login page.
# Expected Result:
#
# User is registered successfully, and a confirmation message appears.
# Test Case 2 :- Register with Existing Email
# Steps:
#
# Enter an email that is already registered.
# Fill out other fields and click Register.
# Expected Result:
#
# Registration fails with an error: "Email already in use"
# Test case 3 :- Weak Password Validation
# Steps:
#
# Enter a weak password (e.g., 12345 or password).
# Click Register.
# Expected Result:
#
# Error message: "Password must contain at least 8 characters, including letters and numbers."
# Test Case 4 : Missing Required Fields
# Steps:
#
# Leave email, password, or username blank.
# Click Register.
# Expected Result:
#
# Form validation should display: "This field is required."
# Test Case 5 :- Invalid Email Format
# Steps:
#
# Enter an invalid email (e.g., user@com, test@.com).
# Click Register.
# Expected Result:
#
# Error message: "Please enter a valid email address."
# Test Case 6 :- Password Confirmation Mismatch
# Steps:
#
# Enter a password and a different confirmation password.
# Click Register.
# Expected Result:
#
# Error message: "Passwords do not match."
#
# Note :-
# 1. None of the fields should be hard coded
# 2. Each test case must be independent
# 3. Test cases should be written under try except blocks with proper error handling
# 4. Use log statements instead of prints