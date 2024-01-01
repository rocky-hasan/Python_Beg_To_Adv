import re
def is_valid(password):
    reg=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])"
    if re.match(reg,password):
        return password
    return False


password=input('Enter your password')
match_value=is_valid(password)
print(match_value)