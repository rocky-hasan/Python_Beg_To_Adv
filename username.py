

def extract(username):
    newname=username.split('@')
    if len(newname)==2:
        return newname[0]


try:
    email=input("Email :")
    if email.endswith('@gmail.com'):
        result=extract(email)
        print(result)
    else:
        print("Enter Email again")
except ValueError:
    print("error")

