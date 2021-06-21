# imports
import random
import string

# if you want new password
stop = False
print('hello, Welcome to the password generator!')
while stop == False:

    # ask how long your password needs to be
    length = int(input('\nEnter the length of password: '))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    # put everything together
    all = lower + upper + num + symbols

    # make password with 'all' and the length of 'length'
    temp = random.sample(all, length)

    # making the password in text
    password = "".join(temp)

    # print the password
    print(password)
    ask_stop = input('Do you want a new password? Y/N')
    if ask_stop != 'Y':
        stop = True