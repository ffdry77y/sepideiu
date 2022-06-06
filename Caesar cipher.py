# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 15:32:47 2022

@author: sepideiu
"""

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ending=False

def encrypt(text, shift):
    code=[]
    for letter in text:
        if letter in alphabet:
            for i in range(0,len(alphabet)):
                if alphabet[i]== letter:
                    new_position= i+shift
                    if new_position>25:
                        new_position=new_position-26 
            code+=alphabet[new_position]
        else:
            code+=letter
    print(f"{''.join(code)}")


def decrypt(text, shift):
    code=[]
    for letter in text:
        if letter in alphabet:
            for i in range(0,len(alphabet)):
                if alphabet[i]== letter:
                    new_position= i-shift
                    if new_position<0:
                        new_position=new_position+26
        
            code+=alphabet[new_position]
        else:
            code+=letter
    print(f"{''.join(code)}")

while ending==False:
    direction = input("type encode to 'encrypt' type decode to 'decrypt':\n")
    text = input("type your message:\n")
    shift = int(input("type the shift number:\n"))

    if direction== "encode":
        encrypt(text,shift)
    elif direction=="decode":
        decrypt(text,shift)
    else:
        print("invalid input")
    continuee=input("do you want to cantinue? yes or no\n")
    if continuee== "no":
        ending=True