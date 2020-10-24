import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    '../fixed_data/continents/continent_list.csv', index_col='continent')

plt.style.use('ggplot')
data.T.plot(kind='bar')
plt.ylabel('Number of IP\'s')
plt.xlabel('Continents')
