import os 
import pandas as pd
import re
import csv
df=pd.read_csv("course_master_dont_open_in_excel.csv")
ltp=df["ltp"].tolist()
modified_ltp =[]
for text in ltp:
  i=0
  spiled_text=re.split("\-",text)
  for credit in spiled_text:
    if credit!='0':
      i+=1
  spiled_text.append(i)
  modified_ltp.append(spiled_text)
df.drop("ltp",inplace=True,axis=1)
ltp_example=pd.DataFrame(modified_ltp,columns=['L','T','P','non zero bits'])
new_df=pd.concat([df,ltp_example],axis=1)
new_df.to_csv("modified.csv")
student_info=pd.read_csv("studentinfo.csv")
student_rollno=student_info["Roll No"]
list={}
list1={}
for i in student_rollno:
  list[i]=[]
  list1[i]=[]

with open("course_registered_by_all_students.csv","r")as f:
   reader=csv.DictReader(f)
   for row in reader:
     dct=dict(row)
     if dct["rollno"] not in list:
       list[dct["rollno"]]=[]
     list[dct["rollno"]].append(dct["subno"])
    
with open("course_feedback_submitted_by_students.csv","r")as f:
  reader=csv.DictReader(f)
  for row in reader:
    dct=dict(row)
    if dct["stud_roll"] not in list1:
      list1[dct["stud_roll"]]=[]
    list1[dct["stud_roll"]].append(dct["course_code"])

