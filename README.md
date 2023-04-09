
# Lol Api Wrapper

A little project to test myself and create a test-driven development API wrapper for League of Legends. Work in progress, but it works if you want to use it.


## Features

### implemented

- Summoner-V4

### Will be implemented in the future

- Spectator-V4
- League-V5
- Clash-V1
- Match-V5
- Champion-V3
- Champion-Mastery-V4
- Lol-Challenges-V1
- Lol-Status-V4
- Tournament-V4






## Usage/Examples

To use this project install requirements (I recommend creating virtual environment before tho)

```bash
  pip install -r requirements.txt
```

Then all you need to do is import Wrapper class from LolApiWrapper.

Example usage looks like this:

```
    from LolApiWrapper import Wrapper

    lolwrapper = Wrapper('api key from riot games, can be found at https://developer.riotgames.com/')

    player = lolwrapper.get_summoner_by_name('nickname in game', 'server (ie. euw1, na1, etc.))')

    print(player.name)

```
## Running Tests

To run tests, install requirements, fill in fake data with real ones in the test_LolApiWrapper.py file and run the following command

```bash
  py.test
```


## Authors

- [@Mikołaj Mróz](https://www.github.com/Mikolaj-Mroz)

