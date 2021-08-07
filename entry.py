from first_draft import grow_in_script, fall_in_script

user_input = input("grow in or fall in?: ")

if user_input == "grow in":
	grow_in_script()
if user_input == "fall in":
	fall_in_script()
if user_input != "fall in" or user_input != "grow in":
	exit("Error: Please enter either 'grow in' or 'fall in'")


