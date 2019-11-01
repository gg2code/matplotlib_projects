from matplotlib import pyplot as plt 

plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.2 ,0]
colors = ['red', 'blue','green','cyan','yellow']

plt.title('Top 5 programming languages')
plt.pie(slices,explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True,)
plt.tight_layout()
plt.show()