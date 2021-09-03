import codecs
file = open('testfile(1).txt', 'r') 
     
input_text = file.read()
input_text.upper()
print(input_text)
     

def utf8_utf32():
     input_text.encode()

print(utf8_utf32())
output_text = utf8_utf32
output_file = open('utf_to_utf32.txt','w+') 
output_file.write(output_text)
output_file.close()


