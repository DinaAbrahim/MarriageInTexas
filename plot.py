#plot.py
#this program makes a bar graph

import matplotlib.pyplot as plt

#create this to later save the plot to a PDF
f = plt.figure()

fig, ax = plt.subplots()

#the labels on the x-axis
races = ['White', 'Black', 'Asian', 'Indian', 'Multi', 'Hispanic']
#the values of the labels on the x-axis
counts = [28, 30, 28, 24, 24, 27]
#the colors of each bar
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:pink']

ax.bar(races, counts, color=bar_colors)

#the label of the y-axis
ax.set_ylabel('Average Age at Marriage')
#the label of the x-axis 
ax.set_xlabel('Races')
#the title 
ax.set_title('Average Age of Women at Marriage Based on Race in Texas')

plt.show()

#Save the plot into a PDF file 
f.savefig("plot.pdf")
