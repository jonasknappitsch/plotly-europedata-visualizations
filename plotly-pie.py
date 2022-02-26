import pandas as pd
import numpy as np
import plotly.express as px

europe_data = px.data.gapminder().query("year==2007").query("continent=='Europe'")

fig = px.pie(
    europe_data,
    values="pop",
    names="country",
    title="Europe's Population Distribution (2007)")
fig.show()