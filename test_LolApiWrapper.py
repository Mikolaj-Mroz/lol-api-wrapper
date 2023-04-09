from LolApiWrapper import wrapper


def test_Summoner_methods():
    # Test the methods to get Summoner objects

    name = 'fake-name' # fill in with a valid name
    accountId = 'fake-accountId' # fill in with a valid accountId
    summonerId = 'fake-summonerId' # fill in with a valid summonerId
    puuid = 'fake-puuid' # fill in with a valid puuid
    region = 'fake-region' # fill in with a valid region
    api_key = 'fake-api-key' # fill in with a valid api key

    wrapper_instance = wrapper.Wrapper(api_key)
    responses = [
        wrapper_instance.get_summoner_by_name(name,region),
        wrapper_instance.get_summoner_by_puuid(puuid,region),
        wrapper_instance.get_summoner_by_summonerId(summonerId,region),
        wrapper_instance.get_summoner_by_accountId(accountId,region)
    ]
    
    for response in responses:
        assert isinstance(response, wrapper.Summoner), """Response should be a Summoner object"""
        assert type(response.name) == str, """The name should be a string"""