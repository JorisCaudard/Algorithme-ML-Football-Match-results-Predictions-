from statsbombpy import sb

df = sb.events(match_id=3890561)

df = df.loc[df['period'] == 1]

EventCountByTeam = df.groupby(by=['team', 'type'])['type'].count().unstack(level=0)

print(EventCountByTeam['Hoffenheim'])

