import os
import random
import sys

namein = ['What is your name?','What is your name','Whats your name?','your name?']
greetin = ['hi','hello','hey','hi there','hello there']
birth=['what is your birthdate','your dob','what is your date of birth']
owner=['who is your owner','you work for?','who is your master']

nameout = ['assitant']
B= "\n\n\n\n"

print(B)
while True:h
    H = input('=>')
    if H == '':
        print('=> Nice to meet you')
        break
    elif H in namein:
        print ('=>' + (random.choice(nameout)))
