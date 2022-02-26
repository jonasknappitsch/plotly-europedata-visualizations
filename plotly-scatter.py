import pandas as pd
import numpy as np
import plotly.express as px

europe_data2007 = px.data.gapminder().query("year==2007").query("continent=='Europe'")

print(europe_data2007)

# color_continuous_scale: appending _r reverses the colorscale
fig = px.scatter(
                europe_data2007,
                x="lifeExp",
                y="gdpPercap",
                size="pop",
                size_max=40,
                color="lifeExp",
                text="country",
                trendline="ols",
                color_continuous_scale=px.colors.sequential.Inferno_r,
                labels={
                     "lifeExp": "Life Expectancy (in years)",
                     "gdpPercap": "GDP Per Capita (in USD)",
                 }
                )

fig.update_traces(textposition='bottom center')
fig.update_layout(
    width=1080,
    height=720,
    title_text='GDP and Life Expectancy (Europe, 2007)'
)

# mark minimum lifeExp
fig.add_annotation(
            x=europe_data2007["lifeExp"].min(),
            y=float(europe_data2007["gdpPercap"][europe_data2007["lifeExp"] == europe_data2007["lifeExp"].min()]),
            text="minimum Life Expectancy",
            showarrow=True,
            arrowhead=1,
            standoff=1,
            arrowcolor="gray",
            bgcolor="white",
            opacity=0.8)

# mark maximum lifeExp
fig.add_annotation(
            x=europe_data2007["lifeExp"].max(),
            y=float(europe_data2007["gdpPercap"][europe_data2007["lifeExp"] == europe_data2007["lifeExp"].max()]),
            text="maximum Life Expectancy",
            showarrow=True,
            arrowhead=1,
            standoff=1,
            arrowcolor="gray",
            bgcolor="white",
            opacity=0.8)

# mark minimum gdpPercap
fig.add_annotation(
            x=float(europe_data2007["lifeExp"][europe_data2007["gdpPercap"] == europe_data2007["gdpPercap"].min()]),
            y=europe_data2007["gdpPercap"].min(),
            text="minimum GDP Per Capita",
            showarrow=True,
            arrowhead=1,
            standoff=1,
            arrowcolor="gray",
            bgcolor="white",
            opacity=0.8)

# mark maximum gdpPercap
fig.add_annotation(
            x=float(europe_data2007["lifeExp"][europe_data2007["gdpPercap"] == europe_data2007["gdpPercap"].max()]),
            y=europe_data2007["gdpPercap"].max(),
            text="maximum GDP Per Capita",
            showarrow=True,
            arrowhead=1,
            standoff=1,
            arrowcolor="gray",
            bgcolor="white",
            opacity=0.8)

fig.show()