import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


#Figure 1 data and plot
data = pd.read_excel(r'C:/Users/angela/Desktop/Example/taxintroduction.xlsx',
                     header=0)
print(data.head(n=10))

year = data['Year']
income = data['Income Tax']
vat = data['VAT']
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
plt.xlabel('Year')
plt.ylabel('Proportion of Countries')
plt.title('Proportion of 18 Countries with Income Tax and VAT Over Time')
plt.legend()
ax.set_xlim([1900, 2000])
ax.set_ylim([0, 1])
plt.plot(year, income, label="Income Tax", color='b')
plt.plot(year, vat, label="VAT", color='r')
plt.show()
fig.savefig(r'C:/Users/angela/Documents/Fall2021/CompEcon_Fall21/CompEcon_Fall21/ProblemSets/PS3/tax.png',
              transparent=False, dpi=80, bbox_inches="tight")



#Figure 2
mentalhealth = pd.read_excel(r'C:/Users/angela/Desktop/Example/map.xlsx',
                              sheet_name="Sheet3", header=0)

fig2 = px.line(mentalhealth, x="year",
              y=["Good Mental Health","Ok Mental Health","Bad Mental Health"],
              labels=dict(year="Year", value="Proportion of IL Population",
                           variable= "Severity of Mental Health Issues"))
fig2.show()
fig2.write_image(r"C:/Users/angela/Documents/Fall2021/CompEcon_Fall21/CompEcon_Fall21/ProblemSets/PS3/fig2.png")



#Figure 3 data and plot
data2 = pd.read_excel(r'C:/Users/angela/Desktop/Example/map.xlsx',
                      sheet_name="Sheet4", header=0)
data2.sort_values(by="ment14D_3pct", inplace=True)
fig3 = px.bar(data2, x='State', y='ment14D_3pct',
        labels={'ment14D_3pct':'Population with 14+ bad mental health days'})
fig3.show()
fig3.write_image(r"C:/Users/angela/Documents/Fall2021/CompEcon_Fall21/CompEcon_Fall21/ProblemSets/PS3/fig3.png")

