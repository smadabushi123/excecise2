#Author:Sri Harsha Madabushi
#Date : 21/05/2019
"""Write a program that accepts a sentence and calculate the number of letters and digits.
		Suppose the following input is supplied to the program:
		hello world! 123
		Then, the output should be:
		LETTERS 10
		DIGITS 3"""
# Asking user to input a string		
string1 = input("enter a string")
#intializing values of letters and digits to 0
Letters = 0
Digits = 0
#taking value of whole string in to variable i
for i in string1:
#to check for alphabets using function isalpha()
    if i.isalpha():
        Letters = Letters+1
    elif i.isdigit():
	#to check for alphabets using function isalpha()
        Digits = Digits+1
    else:
        pass
print("Letters :", Letters)
print("Digits :", Digits)