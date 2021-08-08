from functions import grow_in_script, fall_in_script 

user_input = input("grow in or fall in?: ")

if user_input == "grow in" or user_input == "growin" or user_input == "grow":
	grow_in_script()
if user_input == "fall in" or user_input == "fallin" or user_input == "fall":
	fall_in_script()
else:
	exit("Error: Please enter either 'grow in' or 'fall in'")