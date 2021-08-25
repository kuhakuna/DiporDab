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
        self.puuids.append(puuid_grabber(teammate5))

    # 08/15 epoch: 1629056900
    # 08/23 epoch: 1629748221
    # my puuid: B9EYucaevIeQ4nteZYIuW5kx7fJ8IbQgVFgRJWViShiBF-ggsRkxI6XsAXQ1cq4lXkDfhqoesIv34g
    # my accountid: mR92AdskD6qLuKY3GwB5PApoh5vee7p8q68ouQS_zLhNHw

    def worthDodging(self, depth):
        if depth == "Shallow":
            league_watcher = LolWatcher(os.environ.get("RIOTAPIKEY"), default_match_v5=True)

            match_list0 = league_watcher.match_v5.matchlist_by_puuid(region='AMERICAS', puuid=self.puuids[0])
            match_list1 = league_watcher.match_v5.matchlist_by_puuid(region='AMERICAS', puuid=self.puuids[1])
            match_list2 = league_watcher.match_v5.matchlist_by_puuid(region='AMERICAS', puuid=self.puuids[2])
            match_list3 = league_watcher.match_v5.matchlist_by_puuid(region='AMERICAS', puuid=self.puuids[3])
            match_list4 = league_watcher.match_v5.matchlist_by_puuid(region='AMERICAS', puuid=self.puuids[4])

            # Debugging
            # print(match_list0)
            # print(match_list1)
            # print(match_list2)
            # print(match_list3)
            # print(match_list4)

            loaded_match1 = MatchData(match_list0[0], self.team[0])
            loaded_match2 = MatchData(match_list1[0], self.team[1])
            loaded_match3 = MatchData(match_list2[0], self.team[2])
            loaded_match4 = MatchData(match_list3[0], self.team[3])
            loaded_match5 = MatchData(match_list4[0], self.team[4])

            individual_wins = 0
            individual_wins += loaded_match1.won()
            individual_wins += loaded_match2.won()
            individual_wins += loaded_match3.won()
            individual_wins += loaded_match4.won()
            individual_wins += loaded_match5.won()

            print(loaded_match1.results())
            print(loaded_match2.results())
            print(loaded_match3.results())
            print(loaded_match4.results())
            print(loaded_match5.results())
            print(f"{individual_wins} wins from your 5 teammates")




