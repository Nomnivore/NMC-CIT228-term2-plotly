from readData import getTransformedData as getData
from readData import DataHeaders as dh
import plotly.graph_objects as go
import plotly.colors as plcolor

data = getData()

min_install_count = 100000

prices = []

for app in data["rows"]:
    if app[dh.TYPE] == "Free" or app[dh.INSTALLS] < min_install_count:
        continue
    prices.append(app[dh.PRICE])

print(len(prices))


fig = go.Figure(go.Histogram(
    x=prices,
    xbins=dict(
        start=0,
        end=10,
        size=2.0
    )
))

fig.update_layout(
    title=dict(
        text="Price of Paid Apps (>100k installs)",
        x=0.5,
        xanchor="center",
        font_size=42
    ),
    yaxis=dict(title="Number of Apps"),
    xaxis=dict(title="Price (in dollars)"),
    font=dict(size=20),
    yaxis_title_font=dict(size=32),
    xaxis_title_font=dict(size=32),
)

# I couldn't figure out how to set the color of the bars
# based on their value.
fig.update_traces(
    marker=dict(
        color=plcolor.qualitative.Plotly,
    )
)

fig.show()
