from readData import getTransformedData as getData
from readData import DataHeaders as dh
import plotly.graph_objects as go


data = getData()

min_install_count = 100000

# using "successful" games >= 100k installs
games = list(filter(lambda x: x[dh.CATEGORY] ==
             "GAME" and x[dh.INSTALLS] >= min_install_count, data["rows"]))

genres_dict = {}

for game in games:
    for genre in game[dh.GENRES]:
        if genre not in genres_dict:
            genres_dict[genre] = 1
        else:
            genres_dict[genre] += 1

sorted_genres_dict = dict(
    sorted(genres_dict.items(), key=lambda x: x[1], reverse=True))

size = 10

genres = list(sorted_genres_dict.keys())[:size]
game_count = list(sorted_genres_dict.values())[:size]

print(genres)
print(game_count)

fig = go.Figure(go.Pie(
    labels=genres,
    values=game_count,
))

fig.update_traces(
    textinfo="label+percent",
    textfont_size=20,
)

fig.update_layout(
    title=dict(
        text=f"Top {size} Genres of Games > 100k Installs",
        font_size=42,
        x=0.5,
        xanchor="center"
    )
)

fig.show()
