#User_Input File to get the Data from the User to Passwordify the User Key word depending on the user's choice of Easy to remember or Hard to remember type of Password

import Randomized_Passwordify as RP
import Passwordify as P
import Password_Strength as PS
import string
import re

#User Keyword Validation (Minimum Word Length is 5)

def User_Keyword_validation(Keyword):
  flag=0
  if len(Keyword) < 5:
    flag=1
  return flag

User_Keyword = input("Enter any WORD to passwordify  ")

Flag=User_Keyword_validation(User_Keyword.strip())
while(Flag):
  User_Keyword = input("Please enter the keyword with minimum length of 5 ")
  Flag=User_Keyword_validation(User_Keyword.strip())

#-------------------------Keyword validation End----------------------------

#Final Password Validation

def Validate_Password (Passkey):
  lowercase = re.search(r"[a-z]", Passkey)
  uppercase = re.search(r"[A-Z]", Passkey)
  number = re.search(r"[0-9]", Passkey)
  symbol = re.search(r"[@#$|!%*_+=;<>/?~\-]",Passkey)
  return all((lowercase, uppercase, number, symbol))

#-------------------------Password validation End----------------------------

#Menu to choose the type of Password to be generated

User_Input = input("Please enter '1' for EASY TO REMEMBER type of Password and '2' for STRONG YET TOUGH TO REMEMBER type of Password ")

def Menu_Validation (Input):
	flag = 1
	if int(Input) == 1 or int(Input) == 2 :
		flag = 0
	else: 
		flag = 1
	return flag

Menu_Flag = Menu_Validation(User_Input)
while(Menu_Flag):
	User_Input = input("Please enter '1' for EASY TO REMEMBER type of Password and '2' for STRONG YET TOUGH TO REMEMBER type of Password")
	Menu_Flag = Menu_Validation(User_Input)

#-------------------------Menu validation End----------------------------
	
#Main Function Calls for Passwordifying the User Input

User_Keyword = User_Keyword.strip()
Output_Flag = True
while(Output_Flag):
	if User_Input == '1':
		Easy_Pass = P.Main_Function(User_Keyword)	
		Password_flag = Validate_Password(Easy_Pass)
		Strength = PS.passwordstrength(Easy_Pass,verbose=False)
		Strength_Check = Strength.get_readable_score()
		if Password_flag:
			if Strength_Check == "OK" or Strength_Check == "Strong" or Strength_Check == "Very strong":
				print('')
				print('')
				print("The EASY Passwordified version of your keyword ", Easy_Pass)
				Output_Flag = False
			else:
				Output_Flag = True

		else:
			Output_Flag = True
	elif User_Input == '2':
		Tough_Pass = RP.Main_Function(User_Keyword)	
		Password_flag = Validate_Password(Tough_Pass)
		Strength = PS.passwordstrength(Tough_Pass,verbose=False)
		Strength_Check = Strength.get_readable_score()
		if Password_flag:
			if Strength_Check == "OK" or Strength_Check == "Strong" or Strength_Check == "Very strong":
				print('')
				print('')
				print("The STRONG Passwordified version of your keyword ", Tough_Pass)
				Output_Flag = False
			else:
				Output_Flag = True
		else:
			Output_Flag = True


#-------------------------The End----------------------------
