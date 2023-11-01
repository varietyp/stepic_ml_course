import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(rc={'figure.figsize': (9, 6)})
events_data = pd.read_csv('event_data_train.csv')
events_data['date'] = pd.to_datetime(events_data.timestamp, unit='s')
events_data['day'] = events_data.date.dt.date
gap_data = events_data[['user_id', 'day', 'timestamp']]\
      .drop_duplicates(subset=['user_id', 'day'])\
      .groupby('user_id')['timestamp'].apply(list)\
      .apply(np.diff).values

gap_data = pd.Series(np.concatenate(gap_data, axis=0))
gap_data = gap_data / (24 * 60 * 60)
gap_data.hist()

print(gap_data.quantile(0.95))
