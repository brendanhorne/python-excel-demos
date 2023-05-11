#https://typesense.org/learn/fuzzy-string-matching-python/
from difflib import SequenceMatcher as SM
import pandas as pd

cities_list = pd.read_excel('cities.xlsx', header=0)
unique_list = [
    "Sydney",
    "Melbourne",
    "Brisbane",
    "Perth",
    "Adelaide",
    "Cairns",
    "Canberra",
    "Darwin",
    "Hobart"
]
trials = []
for enum_value in cities_list.get('Location'):
    probabilities = []
    for unique_value in unique_list:
        probabilities.append(SM(None, enum_value, unique_value).ratio())
    probability = max(probabilities)
    index = probabilities.index(probability)
    probable_value = unique_list[index]
    trials.append([enum_value, probable_value, probability])

trials = pd.DataFrame(trials, columns=['value', 'value guess', 'probability'])

trials.to_excel('output.xlsx',index=None)