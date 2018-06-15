Passwordify

Hi ever got frustrated because of the Password requirements? I have. many times when I had to change my Laptop's password 
every 15 days..! That is when I came up with an idea of automating the password generation. However, I respect your (the user's) choices. So, I have developed a code using python-3 which accepts the user's keywords with a minimum length of 5 as input and transforms them into the Universally accepted passwords. You can use these passwords anywhere needed.

Here's the way it works. 
* You have to execute the code "User_Input" using the python3 compiler which asks for the User Keyword. 
* You have to input the keyword satisfying the minimum length requirement of 5 (five) else you will be asked again until you input a five lettered word.
* You have to choose the level of randomization for the password by typing '1' or '2'. There are two levels Easy and Tough, both have the different ranges of password security.
* After selecting the level the code internally does the work by randomly modifying the keyword by capitalizing, symbolizing (Special characters) and appending random characters and making the outcome meeting the universal password requirements.
* Once a Random password is generated, this password is passed as an argument to the password strength checker which checks the strength of the password. If the strength is more than the given threshold this password is the Passwordified output else the code generates another random string and does the same as discussed earlier as long as the strength is more than the threshold.
   

    Password strength is one module which I have cloned from the following repository. I have made significant and required changes for that code to make it useful in my scenario.
Reference: https://github.com/gkbrk/passwordstrength


**** There are no special requirements to use this code. Just have Python3 Installed on your PC. Clone or download the code and run it ****