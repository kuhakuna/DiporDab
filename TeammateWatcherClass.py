import pprint

from riotwatcher import LolWatcher, ApiError
from matchdto import MatchData
import os


class TeammateWatcher:
    def __init__(self, teammate1, teammate2, teammate3, teammate4, teammate5):
        lw = LolWatcher(os.environ.get('RIOTAPIKEY'), default_match_v5=True)

        def puuid_grabber(summoner_name):
            puuid = lw.summoner.by_name('NA1', summoner_name)
            return puuid['puuid']

        self.lw = LolWatcher(os.environ.get('RIOTAPIKEY'), default_match_v5=True)
        self.team = []
        self.team.append(teammate1)
        self.team.append(teammate2)
        self.team.append(teammate3)
        self.team.append(teammate4)
        self.team.append(teammate5)
        self.puuids = []
        self.puuids.append(puuid_grabber(teammate1))
        self.puuids.append(puuid_grabber(teammate2))
        self.puuids.append(puuid_grabber(teammate3))
        self.puuids.append(puuid_grabber(teammate4))
        self.puuids.append(puuid_grabber(teammate1))

    # 08/15 epoch: 1629056900
    # 08/23 epoch: 1629748221
    # my puuid: B9EYucaevIeQ4nteZYIuW5kx7fJ8IbQgVFgRJWViShiBF-ggsRkxI6XsAXQ1cq4lXkDfhqoesIv34g
    # my accountid: mR92AdskD6qLuKY3GwB5PApoh5vee7p8q68ouQS_zLhNHw

    def worthDodging(self, depth, number_of_games=None, match_list=None):
        overall_wins = 0
        total_matches = 0
        if depth == "Shallow":
            for i in range(5):
                individual_wins = 0
                individual_victories = []
                matches = []
                league_watcher = LolWatcher(os.environ.get("RIOTAPIKEY"), default_match_v5=True)

                match_list = league_watcher.match_v5.matchlist_by_puuid(region='AMERICAS', puuid=self.puuids[i], queue=420, type="MATCHED_GAME", start=1629056900, end=1629748221)
                pprint.pp(f"match_list:{match_list}")
