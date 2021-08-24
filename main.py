# Below is some of the data that you can get from Riot Games API:
# Service status.
# Summoner details: name, level, profile icon, account ids.
# Match History and Match details and timelines by Summoner name.
# Someone’s current game info, if someone is in the game.
# Other information, check out the API documentation (https://developer.riotgames.com/apis)
# Imports
import re
import cassiopeia as cass
from cassiopeia import Summoner
import os
from TeammateWatcherClass import TeammateWatcher

from riotwatcher import LolWatcher, ApiError

from matchdto import MatchData

from BlankWinObject import BlankMatch

# Global Variables
lw = LolWatcher(os.environ.get('RIOTAPIKEY'), default_match_v5=True)
bg = BlankMatch
teammates = []


teammates_dump = """dead player I joined the lobby
dead player I joined the lobby
season 6 dun joined the lobby
Krovos joined the lobby
sha ß joined the lobby"""

lobby_dump = open("C:\\logs\\lobbydump.txt")
regex_pattern = r"(.*)(\sjoined the lobby)"
x = re.findall(regex_pattern, teammates_dump, flags=re.MULTILINE)
print(f"{x[0][0]},\n{x[1][0]},\n{x[2][0]},\n{x[3][0]},\n{x[4][0]}")
tw = TeammateWatcher(x[0][0], x[1][0], x[2][0], x[3][0], x[4][0])

# my_puuid = puuid("dead player I")
# print(my_puuid)
tw.worthDodging("Shallow")
