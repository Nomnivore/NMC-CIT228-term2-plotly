from readData import getTransformedData as getData
from readData import DataHeaders as dh
import plotly.graph_objects as go


data = getData()

apps = data["rows"]

min_install_count = 100000


labels = ["Free", "Paid"]
num_apps = [0, 0]

for app in apps:
    if app[dh.INSTALLS] < min_install_count:
        continue

    if app[dh.TYPE] == "Paid":
        num_apps[1] += 1
    else:
        num_apps[0] += 1


print(num_apps)

fig = go.Figure(go.Pie(
    labels=labels,
    values=num_apps,
    hole=.3
))

fig.update_traces(
    textinfo="label+percent",
    textfont_size=20,
)

fig.update_layout(
    title=dict(
        text="Payment Model of Apps > 100k Installs",
        font_size=42,
        x=0.5,
        xanchor="center"
    )
)

fig.show()
