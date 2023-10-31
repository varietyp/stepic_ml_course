import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(rc={'figure.figsize': (9, 6)})

events_data = pd.read_csv('event_data_train.csv')

actions_data = events_data.pivot_table(index='user_id',
                                       columns='action', values='step_id',
                                       aggfunc='count', fill_value=0).reset_index()
actions_data.discovered.hist()
plt.show()

