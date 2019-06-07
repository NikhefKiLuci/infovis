from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

init_notebook_mode(connected=True)

import pandas as pd

df_m = pd.read_csv('marriage.csv')
