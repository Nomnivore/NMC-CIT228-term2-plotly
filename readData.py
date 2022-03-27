import csv
import re
from typing import Union
filename = "data/googleplaystore.csv"


class DataHeaders:
    APP = 0
    CATEGORY = 1
    RATING = 2
    REVIEWS = 3
    SIZE = 4
    INSTALLS = 5
    TYPE = 6
    PRICE = 7
    CONTENT_RATING = 8
    GENRES = 9
    LAST_UPDATED = 10
    CURRENT_VER = 11
    ANDROID_VER = 12


def getData():

    rows = []

    with open(filename) as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for row in csvreader:
            if not row:
                continue

            rows.append(row)

    return {"header": header, "rows": rows}


def _colToNum(col, parser=int) -> Union[int, float]:
    num = "".join(re.findall(r"[\d|.]+", col))
    if num == "":
        return 0
    return parser(num)


def getTransformedData():
    data = getData()

    for row in data["rows"]:
        row[DataHeaders.INSTALLS] = _colToNum(row[DataHeaders.INSTALLS])
        row[DataHeaders.PRICE] = _colToNum(row[DataHeaders.PRICE], float)
        row[DataHeaders.RATING] = _colToNum(row[DataHeaders.RATING], float)
        row[DataHeaders.GENRES] = row[DataHeaders.GENRES].split(";")

    return data
