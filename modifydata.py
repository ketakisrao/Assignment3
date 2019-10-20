import csv

v = open('death_causes1.csv')
d = open('output.csv', 'w')
r = csv.reader(v)
w = csv.writer(d, lineterminator='\n')
row0 = next(r)
row0.append('New_group')
w.writerow(row0)
# print(row0)
all = []

for item in r:
    new_group = ''
    if(item[-1] == 'Asthma' or item[-1] == 'Issues Breathing' or item[-1] == 'Respiratory Condition'):
        new_group = 'Issues Breathing'
    # elif(item[-1] == 'Motor Vehicle Accident' or item[-1] == 'Accident'):
    #     new_group = 'Accident'
    elif(item[-1] == 'Birth Condition' or item[-1] == 'Congenital Anomalies' or item[-1] == 'Disturbance of Behavior or Senses'
         or item[-1] == 'Mental or Behavioral' or item[-1] == 'Seizures' or item[-1] == 'Issues with Movement' or item[-1] == 'Diseases of the nervous system'):
        new_group = 'Congenital Anomalies'
    elif(item[-1] == 'Eye Condition' or item[-1] == 'Muscle/Bone Condition' or item[-1] == 'Skin Condition' or item[-1] == 'Kidney Condition' or item[-1] == 'Urinary Abdominal Issues'
         or item[-1] == 'Liver Disease' or item[-1] == 'Male Reproductive Condition' or item[-1] == 'Female Reproductive Condition' or item[-1] == 'Pregnancy Related'
         or item[-1] == 'Stomach or Bowel Issues' or item[-1] == 'Bladder Condition' or item[-1] == 'Drug Use' or item[-1] == 'Diabetes'):
        new_group = 'Organ Failure'
    elif(item[-1] == 'Other' or item[-1] == 'Unkown cause' or item[-1] == 'Natural Disaster' or item[-1] == 'Fire' or item[-1] == 'HIV/AIDS' or item[-1] == 'Fall' or item[-1] == 'Heat Exposure'
         or item[-1] == 'Medical Care Error' or item[-1] == 'Military Situation' or item[-1] == 'Infection' or item[-1] == 'Motor Vehicle Accident' or item[-1] == 'Accident'):
        new_group = 'Other'
    elif(item[-1] == 'Heart Disease' or item[-1] == 'Stroke'):
        new_group = 'Heart Disease'
    else:
        new_group = item[-1]
    item.append(new_group)
    all.append(item)

w.writerows(all)
