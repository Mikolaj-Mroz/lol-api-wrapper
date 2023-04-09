from summoner import Summoner
from lolstatus import LolStatus


class Wrapper():
    """Wrapper for the League of Legends API"""

    def __init__(self, api_key: str):
        """Initializes the Wrapper class"""
        self._api_key = api_key
    
    def get_summoner_by_name(self, name: str, region: str) -> Summoner:
        """Get a summoner object by summoner name."""
        return Summoner(region, self._api_key, name=name)
    
    def get_summoner_by_puuid(self, puuid: str, region:str) -> Summoner:
        """Get a summoner object by puuid."""
        return Summoner(region, self._api_key, puuid=puuid)
    
    def get_summoner_by_accountId(self, accountId: str, region: str) -> Summoner:
        """Get a summoner object by accountId."""
        return Summoner(region, self._api_key, accountId=accountId)
    
    def get_summoner_by_summonerId(self, summonerId: str, region: str) -> Summoner:
        """Get a summoner object by summonerId."""
        return Summoner(region, self._api_key, summonerId=summonerId)
    
    def lol_status(self, region: str) -> LolStatus:
        """Get the status of the League of Legends servers."""
        return LolStatus(self._api_key, region)