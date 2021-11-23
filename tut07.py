import os
from numpy.core.numeric import False_
import pandas as pd
import re
import csv
import openpyxl
from collections import Counter
df = pd.read_csv("course_master_dont_open_in_excel.csv")
ltp = df["ltp"].tolist()
modified_ltp = []
for text in ltp:
    i = 0
    spiled_text = re.split("\-", text)
    for credit in spiled_text:
        if credit != '0':
            i += 1
    spiled_text.append(i)
    modified_ltp.append(spiled_text)
df.drop("ltp", inplace=True, axis=1)
ltp_example = pd.DataFrame(modified_ltp, columns=[
                           'L', 'T', 'P', 'non zero bits'])
new_df = pd.concat([df, ltp_example], axis=1)
new_df.to_csv("modified.csv")
student_info = pd.read_csv("studentinfo.csv")
student_data = {}
subject_data = {}
student_rollno = student_info["Roll No"]
with open("studentinfo.csv", "r")as f:
    reader = csv.DictReader(f)
    for row in reader:
        dct = dict(row)
        student_data[dct["Roll No"]] = [dct["Roll No"], "", "", "",
                                        dct["Name"], dct["email"], dct["aemail"], dct["contact"]]
# print(student_data)
with open("course_registered_by_all_students.csv", "r")as f:
    reader = csv.DictReader(f)
    for row in reader:
        dct = dict(row)
        subject_data[dct["subno"]] = [dct["register_sem"], dct["schedule_sem"]]
# print(subject_data)
alloted_subject = {}
feedback_given_subject = {}
for i in student_rollno:
    alloted_subject[i] = []
    feedback_given_subject[i] = []

with open("course_registered_by_all_students.csv", "r")as f:
    reader = csv.DictReader(f)
    for row in reader:
        dct = dict(row)
        if dct["rollno"] not in alloted_subject:
            alloted_subject[dct["rollno"]] = []
        alloted_subject[dct["rollno"]].append(dct["subno"])

with open("course_feedback_submitted_by_students.csv", "r")as f:
    reader = csv.DictReader(f)
    for row in reader:
        dct = dict(row)
        temp=[]
        if dct["stud_roll"] not in feedback_given_subject:
            feedback_given_subject[dct["stud_roll"]] = []
        temp.append(dct["course_code"])
        temp.append(dct["feedback_type"])
        feedback_given_subject[dct["stud_roll"]].append(temp)

#  print(alloted_subject)
subject_count = {}
with open("modified.csv", "r")as f:
    reader = csv.DictReader(f)
    for row in reader:
        dct = dict(row)
        subject_count[dct["subno"]] = dct["non zero bits"]
# print(subject_count)
data_xls = pd.read_excel(
    'course_feedback_remaining.xlsx', 'Sheet1')
# d = Counter(feedback_given_subject)
xx = []
for i in alloted_subject:
    for subject in alloted_subject[i]:
        if i in feedback_given_subject:
            for j in feedback_given_subject[i]:
              if subject != j[0] and i in student_data and subject in subject_count:

                if subject_count[subject] == "1":
                  data_xls.loc[len(data_xls.index)] = [i, subject_data[subject][0], subject_data[subject][1], subject,
                                  student_data[i][4], student_data[i][5], student_data[i][6], student_data[i][7]]
                if subject_count[subject] == "2":
                  data_xls.loc[len(data_xls.index)] = [i, subject_data[subject][0], subject_data[subject][1], subject,
                                  student_data[i][4], student_data[i][5], student_data[i][6], student_data[i][7]]
                  data_xls.loc[len(data_xls.index)] = [i, subject_data[subject][0], subject_data[subject][1], subject,student_data[i][4], student_data[i][5], student_data[i][6], student_data[i][7]]
                if subject_count[subject] == "3":
                  data_xls.loc[len(data_xls.index)] = [i, subject_data[subject][0], subject_data[subject][1], subject,
                                  student_data[i][4], student_data[i][5], student_data[i][6], student_data[i][7]]
                  data_xls.loc[len(data_xls.index)] = [i, subject_data[subject][0], subject_data[subject][1], subject,
                                  student_data[i][4], student_data[i][5], student_data[i][6], student_data[i][7]]
                  data_xls.loc[len(data_xls.index)] = [i, subject_data[subject][0], subject_data[subject][1], subject,
                                  student_data[i][4], student_data[i][5], student_data[i][6], student_data[i][7]]

              
              elif i not in student_data:
                t="NA_IN_STUDENTINFO"
                data_xls.loc[len(data_xls.index)]=[i,t,t,t,t,t,t,t]

              # else:
              #     d = Counter(feedback_given_subject[i])
              #     print(type(d))
              #     print(d)
              #     if d not in xx:
              #         xx.append(d)
              #         print(int(subject_count[subject]), int(d[subject]))
              #         if(subject in subject_count and d[subject] != subject_count[subject] and i in student_data):
              #             t = abs(int(subject_count[subject]) - int(d[subject]))
              #             # print(t)
              #             while(t > 0):
              #                 t -= 1
              #                 data_xls.loc[len(data_xls.index)] = [i, subject_data[subject][0], subject_data[subject][1], subject,
              #                                                     student_data[i][4], student_data[i][5], student_data[i][6], student_data[i][7]]


# print(data_xls)
# file_name = 'MarksData.xlsx'

# # saving the excel
# data_xls.to_excel(file_name)

