import pandas
data=pandas.pandas.read_csv("./state_mapping/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250114.csv")
Gray_sqirrels_data=len(data[data["Primary Fur Color"]=="Gray"])
red_sqirrels_data=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_sqirrels_data=len(data[data["Primary Fur Color"]=="Black"])
w={"Fur colors":["Gray","Red","Black"],"count":[Gray_sqirrels_data,red_sqirrels_data,black_sqirrels_data]}
data_f=pandas.DataFrame(w)
data_f.to_csv("birds_color_data.csv")

