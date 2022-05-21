import pandas as pd
import datetime as dt
import random as rd

df=pd.read_excel('presence.xlsx')
students_ids=df['Matricule']

attended_list=[]
for i in range(1,50):
    attended_list.append(students_ids[rd.randint(1,100)])

Status=[]
for student in students_ids:
    if student in attended_list:
        Status.append('Present')
    else:
        Status.append('Abscent')

date=dt.date.today().strftime('%d-%B-%Y')
df['121314']=Status

df.to_excel('presence.xlsx',index=False)


