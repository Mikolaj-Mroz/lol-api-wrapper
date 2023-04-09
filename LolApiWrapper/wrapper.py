import requests


class Summoner():
    # TODO: Add rate limiting

    def __init__(self, 
                 region: str, 
                 api_key: str, 
                 puuid: str = None, 
                 accountId: str = None, 
                 summonerId: str = None, 
                 name: str = None):
        
        if region not in ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'tr1', 'ru', 'pbe1']:
            raise ValueError('Invalid region')

        if name:
            request_string = '/lol/summoner/v4/summoners/by-name/' + name
        elif puuid:
            request_string = '/lol/summoner/v4/summoners/by-puuid/' + puuid
        elif accountId:
            request_string = '/lol/summoner/v4/summoners/by-account/' + accountId
        elif summonerId:
            request_string = '/lol/summoner/v4/summoners/' + summonerId
        
        response = requests.get(
            'https://' +
            region +
            '.api.riotgames.com' +
            request_string +
            '?api_key=' +
            api_key
            )
        
        if response.status_code == 404:
            raise ValueError('Summoner not found')
        elif response.status_code == 429:
            raise ValueError('Rate limit exceeded')
        elif response.status_code == 403:
            raise ValueError('Invalid API key')
        elif response.status_code == 500:
            raise ValueError('Internal server error')
        else:
            response = response.json()
    
        self.id = response['id']
        self.accountId = response['accountId']
        self.puuid = response['puuid']
        self.name = response['name']
        self.profileIconId = response['profileIconId']
        self.revisionDate = response['revisionDate']
        self.summonerLevel = response['summonerLevel']


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