import random
import string

def randomStringwithDigitsAndSymbols(stringLength=10):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))



	

print('WELCOME TO RANDOM PASSWORD GENERATOR')
n=int(input('How long do you want your password(minimum 8 characters)?'))


print("Generating Random String password with letters, digits and special characters ")
print ("First Random String ", randomStringwithDigitsAndSymbols() )
print ("Second Random String", randomStringwithDigitsAndSymbols(n) )
print ("Third Random String", randomStringwithDigitsAndSymbols(n) )
print ("Fourth Random String", randomStringwithDigitsAndSymbols(n) )
print ("Fifth Random String", randomStringwithDigitsAndSymbols(n) )
print ("Sixth Random String", randomStringwithDigitsAndSymbols(n) )

