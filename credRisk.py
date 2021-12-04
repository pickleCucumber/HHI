import xml.etree.ElementTree as ET
import pandas as pd
import re
a=[]; n=[];a1=[]; n1=[]
tree = ET.parse('F0409118.xml')
root = tree.getroot()
regex= re.compile(r'^1.[0-9]{1,2}$')
for child in root[1][0]:
    regex = re.compile(r'^1.[0-9]{1,2}$')
    rv = regex.match(child.attrib['НомПоПорРазд1'])
    if rv:
        a.append(child.attrib['НомПоПорРазд1'])
        n.append(int(child.attrib['ВелКредРискИтого']))
summa=sum(n)
col = ['col1', 'col2', 'col3', 'col4']
df = pd.DataFrame(index=a, columns=col)
df = df.fillna(0)
df['col1']=n
df['col2']=df['col1']/summa
df['col3']=df['col2']*100
df['col4']=pow(df['col3'], 2)
summa1=sum(df['col4'])
print(df)
print('HHI=', summa1)
for child in root[1][1]:
    regex = re.compile(r'^2.[0-9]{1,2}$')
    rv = regex.match(child.attrib['НомПоПорРазд2'])
    if rv:
        a1.append(child.attrib['НомПоПорРазд2'])
        n1.append(int(child.attrib['ВелКредРискИтого']))
summa3=sum(n1)


col = ['col1', 'col2', 'col3', 'col4']
df1 = pd.DataFrame(index=a1, columns=col)
df1['col1']=n1
df1['col2']=df1['col1']/summa3
df1['col3']=df1['col2']*100
df1['col4']=pow(df1['col3'], 2)
summa2=sum(df1['col4'])
print(df1)

print('HHI=', summa2)
