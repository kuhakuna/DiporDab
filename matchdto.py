import pprint

from riotwatcher import LolWatcher, ApiError

import os
# "deadplayeri" puuid: B9EYucaevIeQ4nteZYIuW5kx7fJ8IbQgVFgRJWViShiBF-ggsRkxI6XsAXQ1cq4lXkDfhqoesIv34g
lol_watcher = LolWatcher(os.environ.get('RIOTAPIKEY'), default_match_v5=True)



class MatchData:
    def __init__(self, match_id, player_ign):
        self.match_id = lol_watcher.match.by_id('AMERICAS', match_id)
        self.map_side = self.match_id['info']['mapId']
        self.selected_champ = self.match_id['info']['participants'][0]
        x = range(10)
        for n in x:
            if self.match_id['info']['participants'][n]['summonerName'].strip() == player_ign:
                self.selected_champ = self.match_id['info']['participants'][n].copy()

        self.summonerName = self.selected_champ['summonerName']

        # self.champ1 = match_id['info']['participants'][1]
        # self.champ3 = match_id['info']['participants'][3]
        # self.champ4 = match_id['info']['participants'][4]
        # self.champ5 = match_id['info']['participants'][5]
        # self.champ6 = match_id['info']['participants'][6]
        # self.champ7 = match_id['info']['participants'][7]
        # self.champ8 = match_id['info']['participants'][8]
        # self.champ9 = match_id['info']['participants'][9]
        # hehe

        self.selected_champion = self.selected_champ['championName']

        self.selected_side = ""
        if self.selected_champ['teamId'] == 100:
            self.selected_side = "Blue"
        elif self.selected_champ['teamId'] == 200:
            self.selected_side = "Red"

    def side_played(self):
        return self.selected_side

    def champ_played(self):
        return self.selected_champ['championName']

    def summoner_name(self):
        return self.summonerName

    def won(self):
        if self.selected_champ['win']:
            return 1
        else:
            return 0

    def map(self):
        if self.map_side == 11:
            return "Summoner's Rift"
        if self.map_side == 12:
            return "ARAM"
        return

    def results(self):
        if self.selected_champ['win']:
            win_symbol = "WIN"
        else:
            win_symbol = "LOSS"
        return "{} on {} on {} by {} on {}".format(win_symbol, self.side_played(), self.champ_played(),
                                                   self.summoner_name(), self.map())

    def results_clean(self):
        if self.selected_champ['win']:
            win_symbol = "WIN"
        else:
            win_symbol = "LOSS"
        return "{} by {}".format(win_symbol, self.summoner_name())