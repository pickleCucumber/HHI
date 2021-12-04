import pandas as pd

df = pd.read_csv('f634_1021.csv', sep=';', encoding='PT154', header=0, usecols=[17,18])
df.to_numpy()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

n=len(df)
df.drop(df.tail(n-37).index, inplace=True)
df=df[df['Длинные']!='x']
print(df)
df = df.replace(r'\s+','',regex=True)
df['Длинные']=pd.to_numeric(df['Длинные'], errors='coerce')
df['Короткие']=pd.to_numeric(df['Короткие'], errors='coerce')
for i in df:
    df=df[df < 0] = df.abs()


DF1=pd.DataFrame(list(df['Длинные'].append(df['Короткие'])), columns=['col1'])
summa=DF1['col1'].sum()
DF1['col2']=DF1['col1']/summa
DF1['col3']=DF1['col2']*100
DF1['col4']=pow(DF1['col3'], 2)
summa1=DF1['col4'].sum()
print(summa)
print(DF1)
