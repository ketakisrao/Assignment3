import csv
import pandas

v = open('classes.csv')
r = csv.reader(v)
df = pandas.read_csv('myClasses.csv', low_memory=False)

d = open('percentage_predict.csv', 'w')
w = csv.writer(d, lineterminator='\n')
w.writerow(['Group', 'Parent_Group', 'Percentage'])


all = []
for item in r:
    # count = 
    if(item[0] == 'Asthma' or item[0] == 'Issues Breathing' or item[0] == 'Respiratory Condition'):
        new_group = 'Issues Breathing'

    elif(item[0] == 'Birth Condition' or item[0] == 'Congenital Anomalies' or item[0] == 'Disturbance of Behavior or Senses'
         or item[0] == 'Mental or Behavioral' or item[0] == 'Seizures' or item[0] == 'Issues with Movement' or item[0] == 'Diseases of the nervous system'):
        new_group = 'Congenital Anomalies'

    elif(item[0] == 'Eye Condition' or item[0] == 'Muscle/Bone Condition' or item[0] == 'Skin Condition' or item[0] == 'Kidney Condition' or item[0] == 'Urinary Abdominal Issues'
         or item[0] == 'Liver Disease' or item[0] == 'Male Reproductive Condition' or item[0] == 'Female Reproductive Condition' or item[0] == 'Pregnancy Related'
         or item[0] == 'Stomach or Bowel Issues' or item[0] == 'Bladder Condition' or item[0] == 'Drug Use' or item[0] == 'Diabetes'):
        new_group = 'Organ Failure'

    elif(item[0] == 'Other' or item[0] == 'Unkown cause' or item[0] == 'Natural Disaster' or item[0] == 'Fire' or item[0] == 'HIV/AIDS' or item[0] == 'Fall' or item[0] == 'Heat Exposure'
         or item[0] == 'Medical Care Error' or item[0] == 'Military Situation' or item[0] == 'Infection' or item[0] == 'Motor Vehicle Accident' or item[0] == 'Accident'):
        new_group = 'Other'

    elif(item[0] == 'Heart Disease' or item[0] == 'Stroke'):
        new_group = 'Heart Disease'

    else:
        new_group = item[0]
    
    val = df[df['dis'] == new_group]
    den = int(val.get_value(0, 1,  takeable=True))
    num = int(item[1])
    percentage_true = round((num/den) * 100, 2)
    # print(item[0] + '  ' + str(percentage_true))
    new_row = [item[0], new_group, percentage_true]
    all.append(new_row)

w.writerows(all)
