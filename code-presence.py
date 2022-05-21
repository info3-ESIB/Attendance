import pandas as pd
import datetime as dt
import random

date=dt.date.today().strftime('%d-%B-%Y')

df=pd.read_excel('presence.xlsx')

l=['Present','Abscent']
i=0
Status=[]
while i<len(df['Matricule']):
    Status.append(l[random.randint(0,1)])
    i+=1

df[date]=Status

df.to_excel('presence.xlsx',index=False)
