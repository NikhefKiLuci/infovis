from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

init_notebook_mode(connected=True)

import pandas as pd

df = pd.read_csv('huizenmarkt.csv')
