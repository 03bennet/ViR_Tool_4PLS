import time
import os
import ntpath
import xml.etree.ElementTree as ET
import pandas as pd


# list of table headers in which data from xml is pulled into

s_p_x, s_p_y, s_p_z, back_str, ahead_st, w_case, h_a_grd, radial_dist  = [], [], [], [], [], [], [], []


def xml_conversion_script():
	
	# user prompted for filepath input
	
	xml_path = input("\n")

	# removal of quotation marks if filepath contains them
	
	if '"' in xml_path:
		xml_path = xml_path.replace('"','')

	# determines whether xml has infringements
	with open(xml_path, "r") as xml:
	    mytree = ET.parse(xml) 
	    myroot = mytree.getroot()
	        
	    if myroot.find('table'):
	        has_data = True

	    else:
	        has_data = False

	# if the xml does have infringement data, the script is run
	# xml table is found and output as an xlsx for easy parsing
	if has_data == True:

		print("\nProcessing...")
		try:
			xml = pd.read_xml(xml_path, "/root/table/vegetation_analysis_report","", True, False ) 
			xml.to_excel("dataframe.xlsx", index = False)
			workbook = pd.read_excel("dataframe.xlsx")
		except:
			print("Error reading or writing files. Check your workspace permissions.")
			time.sleep(20)
			exit()

		# xlsx columns from workbook are assigned to the list of table headers
		# if statments are to determine whether report is grow in or fall in
		s_p_x = (workbook['survey_point_x'])
		s_p_y = (workbook['survey_point_y'])
		s_p_z = (workbook['survey_point_z_h'])
		if user_input == "1":
			back_str = (workbook['grow_in_closest_wire_back_str'])
		if user_input == "2":
			back_str = (workbook['falling_tree_closest_wire_back_str'])
		if user_input == "1":
			ahead_st = (workbook['grow_in_closest_wire_ahead_str'])
		if user_input == "2":
			ahead_st = (workbook['falling_tree_closest_wire_ahead_str'])
		if user_input == "1":
			w_case = (workbook['grow_in_closest_wire_weather_case'])
		if user_input == "2":
			w_case = (workbook['falling_tree_closest_wire_weather_case'])
		h_a_grd = (workbook['survey_point_height_above_ground'])
		if user_input == "1":
			radial_dist = (workbook['grow_in_closest_wire_vert_or_radial_margin'])
		if user_input == "2":
			radial_dist = (workbook['falling_tree_closest_wire_radial_margin'])


		# list is then assigned to dataframe headers
		df = pd.DataFrame.from_dict({'survey_point_x': s_p_x,'survey_point_y': s_p_y, 
		"survey_point_z": s_p_z, "back_structure": back_str, "ahead_structure": ahead_st,
		"weather": w_case, "height_above_ground": h_a_grd, "radial_distance": radial_dist})

		# df is output as an xlsx, basename of filepath is used for naming convention
		file_name = ntpath.basename(xml_path)
		if ".xml" in xml_path:
			file_name = file_name.replace(".xml","")
		df.to_excel(file_name + '.xlsx', header=True, index=False)


	#if there is no data in the xml, error message is printed.
	else:
		print("\nThere is no data in this xml. No infringements = Happy engineer :)")
		time.sleep(3)

# function determines whether report is grow in or fall in

def main():
	while True:
		if user_input == "1":
			try:
				False
				print("\nEnter file path for Grow In report:")
				xml_conversion_script()
				# checks to see if dataframe has been created. If it has, it's deleted.
				if os.path.isfile('dataframe.xlsx'):					
					os.remove("dataframe.xlsx")
					print("\nAll Done!")
					time.sleep(3)
					break
				else:
					break
			except:
				print("\nNot a filepath, or no xml file exists.")
		
		elif user_input == "2":
			try:
				False
				print("\nEnter file path for Fall In report:")
				xml_conversion_script()
				# checks to see if dataframe has been created. If it has, it's deleted.
				if os.path.isfile('dataframe.xlsx'):		
					os.remove("dataframe.xlsx")
					print("\nAll Done!")
					time.sleep(3)
					break
				else:
					break
			except:
				print("\nNot a filepath, or no xml file exists.")
		
		else:
			True
			print("\nPlease enter either 1 or 2...")
			break


# initial user input to determine whether report is grow in or fall in
if __name__ == '__main__':
	while True:
		user_input = input("\n1 - Grow In \nor \n2 - Fall In \n\nEnter number:")
		main()