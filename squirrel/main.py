import pandas

data = pandas.read_csv("squirrel_data.csv")

total_gray = 0
total_cinnamon = 0
total_black = 0
for x in data.FurColor:
    if x == "Gray":
        total_gray += 1
    elif x == "Black":
        total_black += 1
    else:
        total_cinnamon += 1


squirrels = {"Fur Color": ["gray", "black", "cinnamon"], "Count": [total_black, total_gray, total_cinnamon]}
print(squirrels)
squirrels_data = pandas.DataFrame(squirrels)
squirrels_data.to_csv("color_amount.csv")


# grey_squirrels_count = len(data[data["FurColor"] == "Gray"])
# print(grey_squirrels_count)








#
# data = pandas.read_csv("weather_data.csv")
#
# temp_list = data["temp"].to_list()
#
# monday = data[data.day == "Monday"]
# monday_far = (monday.temp * 1.8) + 32
# print(monday_far)