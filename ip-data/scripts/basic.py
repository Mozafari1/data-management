import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    '../fixed_data/countries/country_list.csv', index_col='country')

plt.style.use('ggplot')
data.T.plot(kind='bar')
plt.ylabel('Number of IP\'s')
plt.show()
