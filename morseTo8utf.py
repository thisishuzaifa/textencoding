import os
import re
import sys

file = open('testfilem.txt','r')
input_text = file.read()
print(input_text)


morse_alphabet = {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', '/':'-..-.' }

def morse_to_utf8(input_text):

    word = ''
    mcode_char = ''
    for letter in input_text:
        if(letter != ' '):

            i = 0
            mcode_char += letter

        else:
            i += 1
            if i ==2 :
                word += ' '

            else:
                word += list(morse_alphabet.keys())[list(morse_alphabet.values()).index(mcode_char)]
                mcode_char = ''
    return word 

    output_text = word
    output_file = open('morseTo8.txt','w+', encoding='utf-8') #change the name of text file 
    output_file.write(word)
    output_file.close()
                   

morse_to_utf8(input_text)



