import pandas

# data frames to place relevant data and output xlsx.

def dataframe_fall():
	df = pd.DataFrame.from_dict({'survey_point_x': survey_point_x,'survey_point_y': survey_point_y, 
	"survey_point_z": survey_point_z, "back_structure": back_structure, "ahead_structure": ahead_structure,
	"weather": weather_case, "height_above_ground": height_above_ground, "radial_distance": radial_distance})
	df.to_excel('fall_in.xlsx', header=True, index=False)

def dataframe_grow():
	df = pd.DataFrame.from_dict({'survey_point_x': survey_point_x,'survey_point_y': survey_point_y, 
	"survey_point_z": survey_point_z, "back_structure": back_structure, "ahead_structure": ahead_structure,
	"weather": weather_case, "height_above_ground": height_above_ground, "radial_distance": radial_distance})
	df.to_excel('grow_in.xlsx', header=True, index=False)