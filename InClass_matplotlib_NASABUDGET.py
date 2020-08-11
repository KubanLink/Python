"""
Title:   InClass_matplotlib.py
Purpose: Practice creating visualizations with Matplotlib. 
Author:  **** YOUR NAME HERE ****
Date:    **** TODAY'S DATE ****
"""

import matplotlib.pyplot as plt
import numpy as np

# Exercise 1
# Create a scatterplot that has 10 points, each with a 
# different marker style and color. Save the plot as
# a .PNG file.
#
# Hint: you'll want to visit these websites:
# https://matplotlib.org/3.2.1/api/markers_api.html
# https://matplotlib.org/2.0.2/api/colors_api.html

print('\nExercise 1------------------------------')
# Here are some points to plot in numpy arrays
'''xdata = np.arange(10)
ydata = xdata ** 2
xdata2= 3*ydata+1
ydata2= xdata2/0.5
ydata3= xdata2/ydata2
xdata3= xdata2/ydata3
xprime= np.arange(10)
yprime=xprime**3
xnatural=3**3
ynatural=xnatural**2

plt.scatter(xdata,ydata, s=1000, c='black', marker='^')
plt.scatter(xdata2,ydata2, s=78, c='red', marker='X')
plt.scatter(xdata,xdata2, s=90, c='lime')
plt.scatter(ydata,ydata2, s=50, c='magenta', marker='P')
plt.scatter(ydata2,ydata, s=92, c='goldenrod', marker='h')
plt.scatter(xdata2,xdata, s=292, c='yellowgreen', marker='p')
plt.scatter(xdata3,ydata3, s=88, c='aqua', marker='v')
plt.scatter(xprime,yprime, s=70, c='lavender', marker='>')
plt.scatter(yprime,xprime, s=12, c='orangered',marker='<')
plt.scatter(ynatural,xnatural, s=25, c='pink')

plt.savefig('scatterslop.png')

plt.show()
#f=open(a,"plotvisualization.png","x")



# Exercise 2    
# Plot the data from the "NASA_exoplanet.csv" file to show
# the brightness of a star that was monitored by a telescope
# in space over ~65 hours. You should use the plt.plot() 
# function. The figure should have an xlabel, a ylabel,
# a title, and a legend. Save the figure as a .PDF file.
print('\nExercise 2------------------------------')
# Here's the command to load the data
time, brightness = np.loadtxt('NASA_exoplanet.csv',delimiter=',',
                              usecols=[0,1],unpack=True)    
# time is in units of hours, and 
# brightness is in units of percent
plt.xlabel('time')
plt.ylabel('brighntess')
plt.plot(time,brightness,label='Light Curve')
plt.savefig('NASA_exoplanet.pdf')

plt.show()'''

    






# Exercise 3
# Make a bar graph showing the budget of NASA relative to 
# the total budget of the US Federal since NASA was founded
# back in 1958. The graph should have x and y labels.
# Also, plot a horizontal dashed line across the graph at 1% 
# Also, plot a vertical dotted line at 1969.
# Lastly, save the figure as a .PDF file.
#
# Hint: You may want to visit this wikipedia page:
# https://en.wikipedia.org/wiki/Budget_of_NASA
print('\nExercise 3------------------------------')
# Here's the command to load the data
year, budget = np.loadtxt('NASA_budget.csv',delimiter=',',
                              usecols=[0,1],unpack=True) 
# budget is in units of percent of the US Federal Budget
plt.bar(year,budget)
plt.xlabel('Calander Year')
plt.ylabel('% of Budget')
plt.axhline(y=1)
plt.plot([1958,2020],[1,1], c='k', ls='--')
plt.plot([1968][1,1],c='k',ls='--')

