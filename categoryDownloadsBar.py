from readData import getTransformedData as getData
from readData import DataHeaders as dh
import plotly.graph_objects as go
import plotly.colors as plcolor

data = getData()

categories_set = set([x[dh.CATEGORY] for x in data["rows"]])
categories = sorted(list(categories_set))
install_counts = [0] * len(categories)

for app in data["rows"]:
    install_counts[categories.index(app[dh.CATEGORY])] += app[dh.INSTALLS]


for i in range(len(categories)):
    categories[i] = categories[i].title().replace("_", " ").replace("And", "&")

fig = go.Figure(go.Bar(
    y=categories,
    x=install_counts,
    orientation='h',
))

fig.update_layout(
    title={
        'text': "Total Installs by Category",
        'x': 0.5,
        'xanchor': 'center',
        'font_size': 42
    },
    yaxis={'categoryorder': 'total ascending', 'title': 'Category'},
    xaxis={'title': 'Total Installs (all apps)'},
    font={'size': 20},
    xaxis_title_font={'size': 32},
    yaxis_title_font={'size': 32},
)

# set the color of the bars
fig.update_traces(
    marker=dict(
        color=plcolor.qualitative.Plotly * 5,
    )
)

fig.show()
