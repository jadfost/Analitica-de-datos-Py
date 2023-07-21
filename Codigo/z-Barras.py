import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Codigo/menu.csv')

a = len(df[df['Category']=='Breakfast'])
b = len(df[df['Category']=='Beef & Pork'])
c = len(df[df['Category']=='Chicken & Fish'])
d = len(df[df['Category']=='Salads'])
e = len(df[df['Category']=='Snacks & Sides'])
f = len(df[df['Category']=='Desserts'])
g = len(df[df['Category']=='Beverages'])
h = len(df[df['Category']=='Coffee & Tea'])
i = len(df[df['Category']=='Smoothies & Shakes'])

# fix, (ax1, ax2, ax3) = plt.subplots(1,2,3)

plt.bar(['br','be','ch','sal','sn','des','bev','cof&tea ',' sm&sh'],[a,b,c,d,e,f,g,h,i])
plt.show()

