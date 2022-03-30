# Pandas indlæser moduler i Python
import pandas as pd
import numpy as np

# `plt` is an alias for the `matplotlib.pyplot` module
import matplotlib.pyplot as plt
plt.style.use('classic')

"""
for at køre koden skal man have en mappe ved siden af filen, der hedder images.
Billederne af graferne, der bliver lavet bliver lagt i denne mappe.
"""

# import seaborn library (wrapper of matplotlib)
#import seaborn as sns

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Excel fil indlæses i Python
df = pd.read_excel('Modul1.1CaseVirksomhedsberegning.xlsx', sheet_name='Beregning', usecols="A,B,F,G,H,I,J,K,L,M,O,P,Q,R,S,T,U,V")
#df = pd.read_excel('Modul1.1CaseVirksomhedsberegning.xlsx', sheet_name='Beregning', usecols="A,B,J")
#print(df)
#print(df.head(3))

# Denne kode ændrer på kolonne navnene
df = df.rename(columns={'Udledning faktor': 'Udledning_faktor',
                        'Total enheder for året': 'Total_enheder_for_året'})

#herunder opdeles det i grupper
print(df.groupby("Kategori").describe())
print(df.groupby(["Kategori"]).groups)

grouped = df.groupby(["Kategori"])
print(grouped)

for name, group in grouped:
    print(name)
    print(group)
    print("")

#print("Indkøb")
#print(grouped.get_group("Indkøb"))

df['Kategori'].value_counts()

# får dataframe til en liste
#print(df.values.tolist())


# følger side 285 i bogen
#tit, tot = [df['Titel'].values.tolist()],[df['Total_enheder_for_året'].values.tolist()]
#tot = df['Total_enheder_for_året'].values.tolist()

#print(df.loc[0])
#print(df.loc[0]["Titel"])

Ttit = df.loc[:, 'Titel'].values
Tot = df.loc[:, 'Total_enheder_for_året'].values
Udledning = df.loc[:, 'Udledning'].values
# hvis man vil tage værdierne undtagen den første linje skriver man som linjen nedenunder
#Tot = df.loc[1:, 'Total_enheder_for_året'].values

# tomme lister til matplotlib charts
#tit og Ttit er en forkortelse for titel og tot er en forkortelse for Total_enheder_for_året
Tit = []
#Tot = []
sampleList = [i for i in range(41)]
#print(sampleList)

# for loop for at fylde tomme lister op med data
for x in range(1):
    Tit.append(Ttit)
    print(Tit)

# You can also plot another line on the same graph
#plt.plot(tit, tot)
# plt.plot(month_number, principal_paid)

# bruges til at se om der er nogle nul (Non-Null Count) i Excel filen. Det vil sige steder hvor der eksempelvis ikke er noget data
# Man ser også hvilken datatype hver kolonne har, antallet at kolonner og navnene på kolonnerne
df.info()

# beskriver min, max, 25%, 50%, gennemsnit i alle kolonner i dataframe
#df.describe()

#print(tit)
print(Tot)
print(sampleList)
print(df)
# herunder ser vi på om længden af dataen i listerne for at tjekke at de er lige lange
print(len(Tot))
print(len(sampleList))
print(len(Udledning))
# Matplotlib bar og plot diagram
plt.bar(sampleList,Tot)   #dataframe.groupby("kategorier").mean()
# grafen får en titel
plt.title('Total enheder for året')
# Add labels    
ax.set_xlabel('Titel')
ax.set_ylabel('Total enheder for året')
#gemmer grafen som en png fil i undermappen images
plt.savefig('images/totalplot.png', dpi =300)
plt.close()

f1, ax = plt.subplots(1)
ax.plot(sampleList,Tot)
ax.set_ylim(ymin=0, ymax=5500)
plt.title("Total enheder for året")
# Add labels    
ax.set_xlabel('Titel')
ax.set_ylabel('Total enheder for året')
plt.savefig('images/TotalEnheder for året2.png')
plt.close()

#cirkel diagram Totale enheder
fig2, ax = plt.subplots(figsize=(30, 23), subplot_kw=dict(aspect="equal"))

data1 = [Tot]
ingredients1 = [Tit]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:.1f}%)".format(pct, absolute)

wedges, texts, autotexts = ax.pie(Tot, autopct=lambda pct: func(pct, Tot),
                                  textprops=dict(color="w"))
# Det viser en sinatur forklaring
ax.legend(wedges, Ttit,
          title="Titel",
          loc="center left",
          bbox_to_anchor=(0.9, 0, 0.1, 1))

plt.setp(autotexts, size=16, weight="bold")

ax.set_title("Total enheder for året")

plt.savefig('images/cirkelDiagramTotaleEnheder.png')
plt.close()

#cirkel diagram Udledning
fig3, ax = plt.subplots(figsize=(30, 23), subplot_kw=dict(aspect="equal"))

data2 = [Udledning]
ingredients2 = [Tit]

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return "{:.1f}%)".format(pct, absolute)

wedges, texts, autotexts = ax.pie(Tot, autopct=lambda pct: func(pct, Udledning),
                                  textprops=dict(color="w"))

# titel på grafen
ax.legend(wedges, Ttit,
          title="Titel",
          loc="center left",
          bbox_to_anchor=(0.9, 0, 0.1, 1))

plt.setp(autotexts, size=16, weight="bold")

ax.set_title("Udledning")

plt.savefig('images/cirkelDiagramUdledning.png')
plt.close()

#df.pivot(index='Kategori',columns='Titel',values='Total enheder for året')

# Not the prettiest plot
plt.plot(sampleList,Tot)

df.head()
df['Total_enheder_for_året'].head()
# Using the default settings is not a good idea
# Keep in mind that visualizations are an interative process.
df['Total_enheder_for_året'].hist()

# One solution is to rotate your xticklabels
df['Total_enheder_for_året'].hist()
plt.xticks(rotation = 90)

#Totale enheder for hele året summeret op
df['Total_enheder_for_året'].sum()
# dette kan eksempelvis bruges til at lave et cirkel diagram hvor vi kigger 
# på det totale i forhold til hver enkelt.
