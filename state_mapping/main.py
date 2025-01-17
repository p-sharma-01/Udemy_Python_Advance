# with open("./state_mapping/datafile/weather_data.csv") as data_file:
#     data=data_file.readlines()
#     print(data)
# import csv
# with open("./state_mapping/datafile/weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temp=[]
#     for i in data:
#         temp.append(i[1])
#     print(temp)

import pandas
data=pandas.read_csv("./state_mapping/datafile/weather_data.csv") # Two datatypes : 1. dataframe 2. series
# print(data)
data_dic=data.to_dict()
# print(data_dic)

#1 to find average 
temp_list=data["temp"].to_list()
average=sum(temp_list)/len(temp_list)
print(average)

#2 To find mean
print(data["temp"].mean())

#1 Max Temperature.
print(max(temp_list))

#2 Max temperature
print(data["temp"].max())


#1 to print particular row
print(data["condition"])

#2
print(data.condition)

#get data in row
print(data[data.Day=="Monday"])
print(data[data.temp==data["temp"].max()])


# create dataframes from scratches
data_dic={"students":['Pushpendra','Rachit','gopal'],"Marks":[90,90,89]}
data_f=pandas.DataFrame(data_dic)
data_f.to_csv("pushpendra.csv")