import string
from readData import getTransformedData as getData
from readData import DataHeaders as dh
import plotly.graph_objects as go
import plotly.colors as plcolor


def remove_punctuation(text):
    return text.translate(text.maketrans("", "", string.punctuation))


data = getData()

min_install_count = 100000


# using "successful" games >= 100k installs
games = list(filter(lambda x: x[dh.CATEGORY] ==
             "GAME" and x[dh.INSTALLS] >= min_install_count, data["rows"]))

words_dict = {}


for game in games:
    name = game[dh.APP]

    name = remove_punctuation(name)

    for word in name.split():
        word = word.lower()
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1


sorted_words_dict = dict(
    sorted(words_dict.items(), key=lambda x: x[1], reverse=True))


top_words = list(sorted_words_dict.keys())[:20]
word_count = list(sorted_words_dict.values())[:20]

fig = go.Figure(go.Treemap(
    labels=top_words,
    parents=[""] * len(top_words),
    values=word_count
))

fig.update_layout(
    title=dict(
        text="Frequency of Words in Game Titles > 100k Installs",
        x=0.5,
        xanchor="center",
        font_size=42
    )
)

fig.update_traces(
    marker=dict(
        colors=plcolor.qualitative.Plotly * 5,
    ),
    textinfo="label+value",
    textfont_size=20,
)

fig.show()
