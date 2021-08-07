import pandas as pd

survey_point_x = [1, 3, 4, 5, 6]

survey_point_y = [1, 3, 4, 5, 6]

survey_point_z = [1, 3, 4, 5, 6]

back_structure = [1, 3, 4, 5, 6]

ahead_structure = [1, 3, 4, 5, 6]

weather_case = [1, 3, 4, 5, 6]

height_above_ground = [1, 3, 4, 5, 6]

radial_distance = [1, 3, 4, 5, 6]


df = pd.DataFrame.from_dict({'survey_point_x': survey_point_x,'survey_point_y': survey_point_y, 
"survey_point_z": survey_point_z, "back_structure": back_structure, "ahead_structure": ahead_structure,
"weather": weather_case, "height_above_ground": height_above_ground, "radial_distance": radial_distance})
#df.to_excel('test.xlsx', header=True, index=False)

print(df)