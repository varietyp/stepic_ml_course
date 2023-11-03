import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(rc={'figure.figsize': (9, 6)})

submissions_data = pd.read_csv('submissions_data_train.csv')
submissions_data['date'] = pd.to_datetime(submissions_data.timestamp, unit='s')
submissions_data['day'] = submissions_data.date.dt.date

users_scores = submissions_data.pivot_table(index='user_id',
                                            columns='submission_status',
                                            values='step_id',
                                            aggfunc='count',
                                            fill_value=0).reset_index()

events_data = pd.read_csv('event_data_train.csv')
events_data['date'] = pd.to_datetime(events_data.timestamp, unit='s')
events_data['day'] = events_data.date.dt.date
gap_data = events_data[['user_id', 'day', 'timestamp']]\
      .drop_duplicates(subset=['user_id', 'day'])\
      .groupby('user_id')['timestamp'].apply(list)\
      .apply(np.diff).values

gap_data = pd.Series(np.concatenate(gap_data, axis=0))

gap_data.quantile(0.90) / (24 * 60 * 60)

users_events_data = events_data.pivot_table(index='user_id',
                                            columns='action',
                                            values='step_id',
                                            aggfunc='count',
                                            fill_value=0).reset_index()

users_data = events_data.groupby('user_id', as_index=False)\
      .agg({'timestamp': 'max'}).rename(columns={'timestamp': 'last_timestamp'})
now = 1526772811
drop_out_threshold = 30 * 24 * 60 * 60
users_data['is_gone_user'] = (now - users_data.last_timestamp) > drop_out_threshold

users_data = users_data.merge(users_scores,on='user_id', how='outer')
users_data = users_data.fillna(0)

users_data = users_data.merge(users_events_data, how='outer')

users_days = events_data.groupby('user_id').day.nunique().to_frame().reset_index()

users_data = users_data.merge(users_days, how='outer')
users_data['passed_course'] = users_data.passed > 170




