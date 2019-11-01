from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter

# Specifying the style of plot.
plt.style.use("Solarize_Light2")

data = pd.read_csv('programming_data.csv')

langs = data['LanguagesWorkedWith']

# Initializing the counter
lang_counter = Counter()

for response in langs:
    lang_counter.update(response.split(';'))
print(lang_counter)

languages = []
popularity = []

for item in lang_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
    
print(languages)
print(popularity)

# Plotting using matplotlib
languages.reverse()
popularity.reverse()
plt.barh(languages,popularity)
plt.title('Most popular programming languages')
plt.xlabel('Number of people using the language')
plt.tight_layout()
plt.show()