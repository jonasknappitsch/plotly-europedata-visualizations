import pandas as pd
import numpy as np
import plotly.express as px

europe_data = px.data.gapminder().query("continent=='Europe'")

fig = px.line(
    europe_data,
    x="year",
    y="lifeExp",
    color="country",
    labels={
            "lifeExp": "Life Expectancy (in years)",
    })
fig.show()