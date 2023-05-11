import re
import pandas as pd

unique_ids = pd.read_excel('ids.xlsx', header=0)

pattern = re.compile(r"(?P<a>\w{5})[:;.,|](?P<b>\w{5})[:;.,|](?P<c>\w{5})[:;.,|](?P<d>\w{5})")
trials = []
for unique_id in unique_ids.get('unique_id'):
    match_id = pattern.match(unique_id)
    a = match_id.group('a')
    b = match_id.group('b')
    c = match_id.group('c')
    d = match_id.group('d')
    trials.append([unique_id, a,b,c,d])

trials = pd.DataFrame(trials, columns=['unique_id', 'a', 'b', 'c', 'd'])

trials.to_excel('output.xlsx',index=None)

