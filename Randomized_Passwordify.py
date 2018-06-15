#Randomized Passwordify (Please note that the password generated will be obtained by brute force if the others know your keyword)

import random
import re

Symbol_dict = {'a': '@', 'h': '#', 'i': '!', 'l': '|'}

def Main_Function (User_Keyword):

#Capitalizing the first character

	User_Keyword = User_Keyword.lower()
	Keyword_array = list(User_Keyword)
	iterator=0
	Capital_flag = True
	while Capital_flag:
		if(Keyword_array[iterator].isalpha()):
			Keyword_array[iterator] = Keyword_array[iterator].upper()
			Capital_flag = False
		else:
			iterator = iterator + 1

#----------------------Capitalization End--------------------------

#Special Character

	Keyword_array1 = []
	Symbol_flag = 0

	for i in range(len(Keyword_array)):
		if Keyword_array[i] == 'a' and Symbol_flag == 0:
			Keyword_array1.append(Symbol_dict['a'])
			Symbol_flag = 1
		elif Keyword_array[i] == 'h' and Symbol_flag == 0:
			Keyword_array1.append(Symbol_dict['h'])
			Symbol_flag = 1
		elif Keyword_array[i] == 'i' and Symbol_flag == 0:
			Keyword_array1.append(Symbol_dict['i'])
			Symbol_flag = 1
		elif Keyword_array[i] == 'l' and Symbol_flag == 0:
			Keyword_array1.append(Symbol_dict['l'])
			Symbol_flag = 1
		else:
			Keyword_array1.append(Keyword_array[i])

#----------------------Special Character End--------------------------

#Version Characters

	Temp_password = ''.join(Keyword_array1)
	Random_version_number = random.choice(['1','2','3','4','5','6','7','8','9','10','11','12'])
	Random_symbol = random.choice(['%','*','-','_','+','=',':','<','>','/','?','~'])
	Version_array = []
	if re.search(r"[@#$|!\-]", Temp_password):
		Version_array = ['V', Random_version_number] 
	else:
		Version_array = ['V', Random_symbol, Random_version_number ]

#----------------------Version Character End--------------------------

#Padding characters

	Password_length = random.randrange(10,13)
	Padding_length = Password_length - len(Keyword_array1) - 2
	if Padding_length > 0:
		for j in range(Padding_length):
			Keyword_array1 = Keyword_array1 + list(random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']))
	else:
		Keyword_array1 = Keyword_array1

#----------------------Padding Characters End--------------------------

#Passwordified Output

	Keyword_array1 = Keyword_array1 + Version_array
	Passwordified_Password = ''.join(Keyword_array1)
	return Passwordified_Password

#----------------------Main_Function End--------------------------