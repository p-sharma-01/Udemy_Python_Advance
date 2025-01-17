student_dict={"student":["Raj","Ram","Krishna","Sushmita"],"marks":[55,69,63,89]}
import pandas
data_f=pandas.DataFrame(student_dict)
# for (i,j) in data_f.items():
#     print(j)
for (index,row) in data_f.iterrows():
    if row.student=="Raj":
        print(row.marks)