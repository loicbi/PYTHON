# from email_validator import validate_email, EmailNotValidError
#
# testEmail = "examples@gmail.com"
#
# try:
#     # Validating the `testEmail`
#     emailObject = validate_email(testEmail)
#
#     # If the `testEmail` is valid
#     # it is updated with its normalized form
#     testEmail = emailObject.email
#     print(testEmail)
# except EmailNotValidError as errorMsg:
#     # If `testEmail` is not valid
#     # we print a human readable error message
#     print(str(errorMsg))

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

import re
# Define a function for
# for validating an Email
def check(email):
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")


# Driver Code
if __name__ == '__main__':
    # Enter the email
    email = "énkitrai326@gmail.com"

    # calling run function
    check(email)

    email = "my.ownsite@our-earth.org"
    check(email)

    email = "ankitrai326.com"
    check(email)
