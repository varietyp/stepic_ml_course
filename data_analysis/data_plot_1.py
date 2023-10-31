import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(rc={'figure.figsize': (9, 6)})

events_data = pd.read_csv('event_data_train.csv')
events_data['date'] = pd.to_datetime(events_data.timestamp, unit='s')
events_data['day'] = events_data.date.dt.date
events_data.groupby('day').user_id.nunique().plot()
plt.show()