import pandas as pd 


infos=pd.read_excel('names.xlsx')

names=infos['Prénom']
fam_nam=infos['Nom']
father=infos['Père']
id=infos['Matricule']

d={}

for (n,fam,fath,i) in zip(names,fam_nam,father,id):
    full_name=n+' '+fath+' '+fam
    d[full_name]=i 

IDS=[]
FullName=[]

for n,i in d.items():

    # ids=pd.Series(i)
    # full__name=pd.Series(n)
    IDS.append(i)
    FullName.append(n)
    
dic={}
dic['Matricule']=IDS
dic['Nom']=FullName
df2=pd.DataFrame(dic)
df2.to_excel('presence.xlsx',index=False)

