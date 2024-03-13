from statsbombpy import sb
import pandas as pd
import numpy as np

df = sb.events(match_id=3890561)

print(df.shape)

df = df.loc[df['period'] == 1]

print(df.shape)

EventCountByTeam = df.groupby(by=['team', 'type'])['type'].count().unstack(level=1)

EVENT_NAMES = ["Ball Receipt*", "Ball Recovery", "Dispossessed", "Duel", "Camera On", "Block", "Offside", "Clearance", "Interception", "Dribbe", "Shot", "Pressure", "Substitution", "Own Goal Against", "Foul Won", "Foul Committed", "Goal Keeper", "Bad Behaviour", "Player On", "Player Off", "Shield", "Pass", "50/50", "Tactical Shift", "Error", "Miscontrol", 'Dribble', "Dribbled Past", "Injury Stoppage", "Referee Ball-Drop", "Carry"]

TEAM_NAME = "Hoffenheim"

#print(EventCountByTeam.loc['Hoffenheim'].index)
print(EventCountByTeam.columns)

dfTest = pd.DataFrame(index = [TEAM_NAME])

try :
    for name in EVENT_NAMES:
        dfTest.loc[TEAM_NAME, TEAM_NAME + "-" + name] = int(EventCountByTeam.loc[TEAM_NAME, name]) if name in EventCountByTeam.loc[TEAM_NAME].index else np.nan
    print(dfTest)

except:
    print("Oopsie !")

print(dfTest['Hoffenheim-Dribbled Past'])