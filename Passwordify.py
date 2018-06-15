#Easy Passwordify (Please note that the password generated will be easily obtained if the others know your keyword)
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
	Version_array = []
	if re.search(r"[@#$|!\-]", Temp_password):
		Version_array = ['V','1'] 
	else:
		Version_array = ['V', '-', '1']

#----------------------Version Character End--------------------------

#Padding characters

	Padding_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	Padding_2 = ['ab', 'bc', 'cd', 'de', 'ef', 'fg', 'gh', 'hi', 'ij', 'jk', 'kl', 'lm', 'mn', 'no', 'op', 'pq', 'qr', 'rs', 'st', 'tu', 'uv', 'vw', 'wx', 'xy', 'yz']
	Padding_3 = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']
	Padding_4 = ['abcd', 'bcde', 'cdef', 'defg', 'efgh', 'fghi', 'ghij', 'hijk', 'ijkl', 'jklm', 'klmn', 'lmno', 'mnop', 'nopq', 'opqr', 'pqrs', 'qrst', 'rstu', 'stuv', 'tuvw', 'uvwx', 'vwxy', 'wxyz']
	Padding_5 = ['abcde', 'bcdef', 'cdefg', 'defgh', 'efghi', 'fghij', 'ghijk', 'hijkl', 'ijklm', 'jklmn', 'klmno', 'lmnop', 'mnopq', 'nopqr', 'opqrs', 'pqrst', 'qrstu', 'rstuv', 'stuvw', 'tuvwx', 'uvwxy', 'vwxyz']
	Padding_6 = ['abcdef', 'bcdefg', 'cdefgh', 'defghi', 'efghij', 'fghijk', 'ghijkl', 'hijklm', 'ijklmn', 'jklmno', 'klmnop', 'lmnopq', 'mnopqr', 'nopqrs', 'opqrst', 'pqrstu', 'qrstuv', 'rstuvw', 'stuvwx', 'tuvwxy', 'uvwxyz']

	Password_length = random.randrange(9,13)
	Padding_length = Password_length - len(Keyword_array1) - 2
	if Padding_length > 0 and Padding_length == 1:
		Keyword_array1 = Keyword_array1 + list(random.choice(Padding_1))
		#print("The Passwordified list is ", Keyword_array1)
	elif Padding_length > 0 and Padding_length == 2:
		Keyword_array1 = Keyword_array1 + list(random.choice(Padding_2))
		#print("The Passwordified list is ", Keyword_array1)
	elif Padding_length > 0 and Padding_length == 3:
		Keyword_array1 = Keyword_array1 + list(random.choice(Padding_3))
		#print("The Passwordified list is ", Keyword_array1)
	elif Padding_length > 0 and Padding_length == 4:
		Keyword_array1 = Keyword_array1 + list(random.choice(Padding_4))
		#print("The Passwordified list is ", Keyword_array1)
	elif Padding_length > 0 and Padding_length == 5:
		Keyword_array1 = Keyword_array1 + list(random.choice(Padding_5))
		#print("The Passwordified list is ", Keyword_array1)
	elif Padding_length > 0 and Padding_length == 6:
		Keyword_array1 = Keyword_array1 + list(random.choice(Padding_6))
		#print("The Passwordified list is ", Keyword_array1) 
	else:
		Keyword_array1 = Keyword_array1

  
#----------------------Padding Characters End--------------------------

#Passwordified Output

	Keyword_array1 = Keyword_array1 + Version_array
	Passwordified_Password = ''.join(Keyword_array1)
	return Passwordified_Password

#----------------------Main_Function End--------------------------