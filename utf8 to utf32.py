import os
import re
import sys


file = open('testfile.txt','r')
input_text = file.read()
print(input_text)


output_file = open('8to32.txt','w+', encoding='utf-32') #outputs file with new encoding
output_file.write(input_text)
output_file.close()
