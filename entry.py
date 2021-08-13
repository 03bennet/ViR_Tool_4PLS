from fall_in_function import fall_in_script 
from grow_in_function import grow_in_script
import time
import os


while True:

	user_input = input("Enter either 1 for grow in or 2 for fall in: ")

	if user_input == "1":
		False
		grow_in_script()
		os.remove("dataframe.xlsx")
		print("All Done!")
		time.sleep(200)

	
	if user_input == "2":
		False
		fall_in_script()
		os.remove("dataframe.xlsx")
		print("All Done!")
		time.sleep(200)
	
	if user_input != "1" or user_input != "2":
		True