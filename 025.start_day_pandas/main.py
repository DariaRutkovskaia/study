import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
# data_dict = data.to_dict()
# data_list = data["temp"].tolist()
# print(data["temp"].mean())
# print(data.temp.max())
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# c_temp = monday.temp
# f_temp = 1.8 * c_temp + 32
# print(f_temp)
# data_dict = {
#     "students": ["Howard", "Radj", "Penny"],
#     "scores": [30, 45, 20]
# }
# data_scores = pandas.DataFrame(data_dict)
# print(data_scores)
# data_scores.to_csv("new_data.csv")

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_colors = data["Primary Fur Color"]
all_list = fur_colors.to_list()
colors = fur_colors.unique()
colors = colors[1:]
print(colors)

color_dict = {"Color": [],
              "Count": []}
for item in colors:
    color_dict["Color"].append(item)
    color_dict["Count"].append(all_list.count(item))

print(color_dict)

squirrel_count = pandas.DataFrame(color_dict)
print(squirrel_count)

squirrel_count.to_csv("squirrel_count.csv")
