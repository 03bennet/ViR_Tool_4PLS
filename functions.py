#imports

import xml.etree.ElementTree as ET
#import os
#import sys
import pandas as pd
import time


#fall in/ grow in lists

s_p_x, s_p_y, s_p_z, back_str, ahead_st, w_case, h_a_grd, radial_dist  = [], [], [], [], [], [], [], []


#function to pull relevant attributes from fall in XML and assign them to above lists

def fall_in_script():

	with open(input("Enter Filepath (no quotation marks): "), "r") as xml:
		
		mytree = ET.parse(xml)
		myroot = mytree.getroot()	

		if myroot.find('table'):

			print("Processing. Please Wait...")

			for x in myroot.find('table'):
				item = x.find('survey_point_x')
				s_p_x.append(item.text)
				
				item = x.find('survey_point_y')
				s_p_y.append(item.text)
				
				item = x.find('survey_point_z_h')
				s_p_z.append(item.text)

				item = x.find('falling_tree_closest_wire_back_str')
				back_str.append(item.text)
				
				item = x.find('falling_tree_closest_wire_ahead_str')
				ahead_st.append(item.text)
				
				item = x.find('falling_tree_closest_wire_weather_case')
				w_case.append(item.text)
				
				item = x.find('survey_point_height_above_ground')
				h_a_grd.append(item.text)
				
				item = x.find('falling_tree_closest_wire_radial_margin')
				radial_dist.append(item.text)

				#values from lists are then assigned to a heading from the dataframe dictionary and output as xlsx
				
				df = pd.DataFrame.from_dict({'survey_point_x': s_p_x,'survey_point_y': s_p_y, 
				"survey_point_z": s_p_z, "back_structure": back_str, "ahead_structure": ahead_st,
				"weather": w_case, "height_above_ground": h_a_grd, "radial_distance": radial_dist})
				df.to_excel('fall_in.xlsx', header=True, index=False)

			print("Done!")
			
		else:
			exit("There is no data in this xml.")
			time.sleep(6)


#function to pull relevant attributes from grow in XML and assign them to above lists

def grow_in_script():

	with open(input("Enter Filepath (no quotation marks): "), "r") as xml:

		mytree = ET.parse(xml)
		myroot = mytree.getroot()
			
		if myroot.find('table'):

			print("Processing. Please wait....")

			for x in myroot.find('table'):

				item = x.find('survey_point_x')
				s_p_x.append(item.text)
				
				item = x.find('survey_point_y')
				s_p_y.append(item.text)
				
				item = x.find('survey_point_z_h')
				s_p_z.append(item.text)

				item = x.find('grow_in_closest_wire_back_str')
				back_str.append(item.text)
			
				item = x.find('grow_in_closest_wire_ahead_str')
				ahead_st.append(item.text)
				
				item = x.find('grow_in_closest_wire_weather_case')
				w_case.append(item.text)
			
				item = x.find('survey_point_height_above_ground')
				h_a_grd.append(item.text)
			
				item = x.find('grow_in_closest_wire_vert_or_radial_margin')
				radial_dist.append(item.text)


				#values from lists are then assigned to a heading from the dataframe dictionary and output as xlsx
				df = pd.DataFrame.from_dict({'survey_point_x': s_p_x,'survey_point_y': s_p_y, 
				"survey_point_z": s_p_z, "back_structure": back_str, "ahead_structure": ahead_st,
				"weather": w_case, "height_above_ground": h_a_grd, "radial_distance": radial_dist})
				df.to_excel('grow_in.xlsx', header=True, index=False)
			
			print("Done!")

		else:
			exit("There is no data in this xml.")	
			time.sleep(6)