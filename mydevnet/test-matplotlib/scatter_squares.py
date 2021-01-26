import matplotlib.pyplot as plt

x_valure=list(range(1,1001))
y_valure=[x**2 for x in x_valure]

plt.scatter(x_valure,y_valure,c=y_valure,cmap=plt.cm.Blues,edgecolors='none',s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Values",fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100,0,1100000])
plt.show()