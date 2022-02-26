import pandas as pd
import numpy as np
import plotly.express as px

europe_data = px.data.gapminder().query("country=='Austria'")

fig = px.bar(
    europe_data,
    x="year",
    y="pop",
    color="lifeExp",
    color_continuous_scale="bluered_r",
    labels={
            "pop": "Population",
    })
fig.show()