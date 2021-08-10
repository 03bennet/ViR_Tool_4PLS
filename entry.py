from functions import grow_in_script, fall_in_script 
import time

user_input = input("grow in or fall in?: ")

if user_input == "grow in" or user_input == "grow":
	grow_in_script()
	time.sleep(6)
if user_input == "fall in" or user_input == "fall":
	fall_in_script()
	time.sleep(6)
if user_input != "fall in" or user_input != "fall":
	print("Error: Please enter either 'grow in' or 'fall in'")
	time.sleep(6)
	exit()
if user_input != "grow in" or user_input != "grow":
	print("Error: Please enter either 'grow in' or 'fall in'")
	time.sleep(6)
	exit()

