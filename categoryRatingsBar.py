from readData import getTransformedData as getData
from readData import DataHeaders as dh
import plotly.graph_objects as go
import plotly.colors as plcolor


def avg(lst):
    return sum(lst) / len(lst)


data = getData()

categories_set = set([x[dh.CATEGORY] for x in data["rows"]])
categories = sorted(list(categories_set))
min_install_count = 100000

all_ratings: list[list] = [[] for _ in range(len(categories))]

for app in data["rows"]:
    if app[dh.INSTALLS] >= min_install_count:
        all_ratings[categories.index(app[dh.CATEGORY])].append(app[dh.RATING])

ratings = []

for cat in all_ratings:
    ratings.append(avg(cat))

for i in range(len(categories)):
    categories[i] = categories[i].title().replace("_", " ").replace("And", "&")

fig = go.Figure(go.Bar(
    x=categories,
    y=ratings,
))

fig.update_layout(
    title=dict(
        text="Average Ratings by Category",
        x=0.5,
        xanchor='center',
        font_size=42,
    ),
    xaxis=dict(title='Category'),
    yaxis=dict(title='Average Rating'),
    font=dict(size=20),
    xaxis_title_font=dict(size=32),
    yaxis_title_font=dict(size=32),
)

# set the color of the bars
fig.update_traces(
    marker=dict(
        color=plcolor.qualitative.Plotly * 5,
    )
)

fig.show()
