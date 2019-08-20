#Cifra de César move um caractere três espaços à frente
#Texto normal:    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#Texto cifrado:   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

#Usaremos o método string.find() para achar a posição de um caractere 
import sys


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar(str_in):
	strfinal = (str_in.upper()).replace(" ","")

	size = len(strfinal)
	str_out = ""

	for i in range(size):
		c = strfinal[i] 
		local = alphabet.find(c)  
		newlocale = local + 3
		str_out += alphabet[newlocale]

	return str_out

def variable_caesar(str_in):
	shift = int(input("Shift value: "))
	strfinal = (str_in.upper()).replace(" ","")
	size = len(strfinal)
	str_out = ""

	for i in range(size):
		c = strfinal[i] 
		local = alphabet.find(c)  
		newlocale = (local + shift)%26
		str_out += alphabet[newlocale]

	return str_out

def rot13(str_in):
	strfinal = (str_in.upper()).replace(" ","")
	size = len(strfinal)
	str_out = ""

	for i in range(size):
		c = strfinal[i] 
		local = alphabet.find(c)  
		newlocale = (local + 13)%26
		str_out += alphabet[newlocale]

	return str_out
while 1:
	selector = input("Select the operation: 1 - Caesar, 2 - Variable Caesar, 3 - ROT13\n")

	if(selector == '1'):
		print(caesar(input("Enter a message: ")))
	elif(selector == '2'):
		print(variable_caesar(input("Enter a message: ")))
	elif(selector == '3'):
		print(rot13(input("Enter a message: ")))
		print(rot13(input("Now enter the previously encrypted message: ")))

	choice = input("Do you want to end?\n")
	if(choice!='n'):
		sys.exit(1)
