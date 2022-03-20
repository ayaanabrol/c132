from turtle import distance
import pandas as pd 
import csv 
import matplotlib.pyplot as plt 
df=pd.read_csv("data.csv")
df.head()

mass=df['Mass'].to_list()
radius=df['Radius'].to_list()
distance=df['Distance'].to_list()
gravity=df['Gravity'].to_list()

mass.sort()
radius.sort()
gravity.sort()
distance.sort()
plt.plot(radius,mass)

plt.title("Radius and mass of star")
plt.xlabel("radius")
plt.ylabel("Mass")
plt.show()

plt.plot(mass,gravity)

plt.title('Mass vs Gravity')
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()

plt.scatter(radius,mass)
plt.xlabel("radius")
plt.ylabel("mass")
plt.show()