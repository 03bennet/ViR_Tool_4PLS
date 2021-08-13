import xml.etree.ElementTree as ET
import pandas as pd
import time

s_p_x, s_p_y, s_p_z, back_str, ahead_st, w_case, h_a_grd, radial_dist  = [], [], [], [], [], [], [], []


def grow_in_script():
	
	# user prompted for filepath input
	user_input = input("Enter filepath for grow in report: ")


	# removal of quotation marks if filepath contains them
	if '"' in user_input:
		user_input = user_input.replace('"','')

	# conditional test to see if xml contains data (If there is no data 'table' is not present )
	with open(user_input, "r") as xml:	

		mytree = ET.parse(xml)
		myroot = mytree.getroot()
			
		if myroot.find('table'):
			has_data = True

		else:
			has_data = False

	# if the previous conditional test comes back true, the fall in script is run

	if has_data is True:

		print("Processing....")

		xml = pd.read_xml(user_input, "/root/table/vegetation_analysis_report","", True, False ) 
		
		xml.to_excel("dataframe.xlsx", index = False)
		
		workbook = pd.read_excel("dataframe.xlsx")

		s_p_x = (workbook['survey_point_x'])
		s_p_y = (workbook['survey_point_y'])
		s_p_z = (workbook['survey_point_z_h'])
		back_str = (workbook['grow_in_closest_wire_back_str'])
		ahead_st = (workbook['grow_in_closest_wire_ahead_str'])
		w_case = (workbook['grow_in_closest_wire_weather_case'])
		h_a_grd = (workbook['survey_point_height_above_ground'])
		radial_dist = (workbook['grow_in_closest_wire_vert_or_radial_margin'])

		df = pd.DataFrame.from_dict({'survey_point_x': s_p_x,'survey_point_y': s_p_y, 
		"survey_point_z": s_p_z, "back_structure": back_str, "ahead_structure": ahead_st,
		"weather": w_case, "height_above_ground": h_a_grd, "radial_distance": radial_dist})

		df.to_excel('grow_in.xlsx', header=True, index=False)

	else:
		print("There is no data in this xml.")
		time.sleep(200)
