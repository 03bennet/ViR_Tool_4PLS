#imports

import xml.etree.ElementTree as ET
import os
import sys
import pandas as pd

#fall in/ grow in lists

survey_point_x = []

survey_point_y = []

survey_point_z = []

back_structure = []

ahead_structure = []

weather_case = []

height_above_ground = []

radial_distance = []


#function to pull relevant attributes from fall in XML and assign them to above lists

def fall_in_script():

	with open(input("Enter Filepath: "), "r") as xml:
		
		mytree = ET.parse(xml)
		myroot = mytree.getroot()	

		if myroot.find('table'):

			print("Processing....")

			for x in myroot.find('table'):
				item = x.find('survey_point_x')
				survey_point_x.append(item.text)
				
				item = x.find('survey_point_y')
				survey_point_y.append(item.text)
				
				item = x.find('survey_point_z_h')
				survey_point_z.append(item.text)

				item = x.find('falling_tree_closest_wire_back_str')
				back_structure.append(item.text)
				
				item = x.find('falling_tree_closest_wire_ahead_str')
				ahead_structure.append(item.text)
				
				item = x.find('falling_tree_closest_wire_weather_case')
				weather_case.append(item.text)
				
				item = x.find('survey_point_height_above_ground')
				height_above_ground.append(item.text)
				
				item = x.find('falling_tree_closest_wire_min_dist_to_wire')
				radial_distance.append(item.text)

				df = pd.DataFrame.from_dict({'survey_point_x': survey_point_x,'survey_point_y': survey_point_y, 
				"survey_point_z": survey_point_z, "back_structure": back_structure, "ahead_structure": ahead_structure,
				"weather": weather_case, "height_above_ground": height_above_ground, "radial_distance": radial_distance})
				df.to_excel('fall_in.xlsx', header=True, index=False)
			
		else:
			exit("There is no data in this xml.")


#function to pull relevant attributes from grow in XML and assign them to above lists

def grow_in_script():

	with open(input("Enter Filepath: "), "r") as xml:

		mytree = ET.parse(xml)
		myroot = mytree.getroot()
			
		if myroot.find('table'):

			print("Processing...")

			for x in myroot.find('table'):
				item = x.find('survey_point_x')
				survey_point_x.append(item.text)
				
				item = x.find('survey_point_y')
				survey_point_y.append(item.text)
			
				item = x.find('survey_point_z_h')
				survey_point_z.append(item.text)

				item = x.find('grow_in_closest_wire_back_str')
				back_structure.append(item.text)
			
				item = x.find('grow_in_closest_wire_ahead_str')
				ahead_structure.append(item.text)
			
				item = x.find('grow_in_closest_wire_weather_case')
				weather_case.append(item.text)
			
				item = x.find('survey_point_height_above_ground')
				height_above_ground.append(item.text)
			
				item = x.find('grow_in_closest_wire_min_dist_to_wire')
				radial_distance.append(item.text)

				df = pd.DataFrame.from_dict({'survey_point_x': survey_point_x,'survey_point_y': survey_point_y, 
				"survey_point_z": survey_point_z, "back_structure": back_structure, "ahead_structure": ahead_structure,
				"weather": weather_case, "height_above_ground": height_above_ground, "radial_distance": radial_distance})
				df.to_excel(input('grow_in.xlsx'), header=True, index=False)

		else:
			exit("There is no data in this xml.")	