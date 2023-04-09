import requests

class LolStatus():
    def __init__(self, api_key: str, region: str) -> None:
        """Initializes the LolStatus class"""

        # Check if the region is valid
        if region not in ['br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'tr1', 'ru', 'pbe1']:
            raise ValueError('Invalid region')
        
        response = requests.get('https://' + region + '.api.riotgames.com/lol/status/v4/platform-data?api_key=' + api_key)
        
        # Check if the request was successful
        if response.status_code == 429:
            raise ValueError('Rate limit exceeded')
        elif response.status_code == 403:
            raise ValueError('Invalid API key')
        elif response.status_code == 500:
            raise ValueError('Internal server error')
        else:
            response = response.json()

        self.id = response['id']
        self.name = response['name']
        self.locales = response['locales']
        self.maintenances = response['maintenances']
        self.incidents = response['incidents']