import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(rc={'figure.figsize': (9, 6)})

events_data = pd.read_csv('event_data_train.csv')
# events_data[events_data.action == 'passed'].groupby('user_id', as_index=False)\
#    .aggregate({'step_id': 'count'})\
#    .rename(columns={'step_id': 'passed_steps'}).head()
# events_data[events_data.action == 'passed'].groupby('user_id', as_index=False)\
#    .aggregate({'step_id': 'count'})\
#    .rename(columns={'step_id': 'passed_steps'}).passed_steps.hist()

# events_data[events_data.action == 'passed'].groupby('user_id', as_index=False)\
#    .aggregate({'step_id': 'count'})\
#    .rename(columns={'step_id': 'passed_steps'}).passed_steps.min()

actions_data = events_data.pivot_table(index='user_id',
                                       columns='action', values='step_id',
                                       aggfunc='count', fill_value=0).reset_index()
actions_data.discovered.hist()
plt.show()

