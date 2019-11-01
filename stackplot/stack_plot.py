from matplotlib import pyplot as plt 

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player_one_score = [5, 1, 5, 5, 2, 1, 2, 1, 6]
player_two_score = [0, 1, 4, 8, 2, 2, 5, 3, 1]
player_three_score = [0, 1, 6, 1, 1, 3, 3, 1, 4]

labels = ['player_one', 'player_two', 'player_two']
colors = ['red', 'blue', 'green']



plt.title('Three player stack plot')
plt.stackplot(minutes, player_one_score, player_two_score, player_three_score, labels = labels, colors = colors)
plt.legend(loc = (0.7,0.78))
plt.tight_layout()
plt.show()

