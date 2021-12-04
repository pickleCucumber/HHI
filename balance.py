import xml.etree.ElementTree as ET
import pandas as pd


n=[[], [], [], []]

tree = ET.parse('F0101.xml')
root = tree.getroot()


for child in root[1][0]:
    if (child.attrib['ПризнакАП']== 'Актив') and (child.attrib['Счет2Пор'][0:2] == '50') and (child.attrib['Валюта']=='Итого'):
        n[1].append(int(child.attrib['ИсхОст']))
        print(child.attrib['Счет2Пор'],
              child.attrib['Валюта'],
              child.attrib['ИсхОст'])


summa=sum(n[1])

col = ['col1', 'col2', 'col3', 'col4']
df = pd.DataFrame(index=n[1], columns=col)
df = df.fillna(0)
df['col1']=n[1]
df['col2']=df['col1']/summa
df['col3']=df['col2']*100
df['col4']=pow(df['col3'], 2)
summa1=sum(df['col4'])
print(df)

print('HHI=', summa1)
