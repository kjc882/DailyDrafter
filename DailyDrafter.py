"""
pull in raw player data
    pull down data from API
    load data into player objects(would like to manipulate data before loading into player array if possible)


calculate player projected points
    Let X be games played where X = 0 is most recent, 0 <= X <= 50
    for all players
        for all player.yards[X]
            (((1.25 - (X * .01)) * player.yards[X] * (pt / yard)) * defense.yardsAllowed

createLineup(players)
    for all positions
        choice = findMax(players, position)
        lineup += choice
        players.remove(choice)
        trimPool(players, position, choice.salary)

findmax(players, position)
    for all players with given position
        find max projected points
    return player index

trimPool(players, position, salary1)
    for all players with given position
        remove all players.salary >= salary1

lower lineup to fit in salary cap
    while (lineup.totalSal > maxSal)
        createSecondLineup(players)
        compare secondlineup players with first lineup player
            replace player in first lineup with min(player0.proj - player1.proj)

PLAYER OBJECT DEFINITION(assuming all data must be stored in Player Objects rather than raw database)
    Name: Player's name
    Projected Points: number of points projected for the coming week
    Salary: Amount of money required for player
    Position: QB, WR, R, K, D, F, TE
    RYards: Array of RUSHING yards over past X number of games
    RecYards: Array of RECEIVING yards over past X number of games
    PYards: Array of PASSING yards over past X number of games(only for QB, 0 for others)
"""
import base64
import requests
import csv

class ProcessedPlayer(object):
    name = ""
    pos = ""
    proj = 0
    sal = 0

    def __init__(self, name, pos, proj, sal):
        self.name = name
        self.pos = pos
        self.proj = proj
        self.sal = sal

def send_request():
    # Request

    try:
        response = requests.get(
            url= 'https://api.mysportsfeeds.com/v2.1/pull/nfl/2019-regular/date/20191118/player_gamelogs.csv' ,
            params={
                "fordate": "20161121"
            },
            headers={
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format('cc0ccd01-3831-448a-a562-fd6585','MYSPORTSFEEDS').encode('utf-8')).decode('ascii')
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        File = open('test.txt', 'w')
        with File:
            writer = csv.writer(File)
            writer.writerow(response.content)
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

send_request()

"""
find the player with the max projected points
playerList: List of ProcessedPlayer Objects
pos: Required Position of the Player to return.
returns ProcessedPlayer Object
"""
def findMax(playerList, pos):
    #load tmp with first player with given position
    if x.pos != pos:
        tmp = x

    for x in playerList:
        #find next player with given position
        if x.pos != pos:
            print('3')
            continue

        #if current player projection is greater than tmp projection, override tmp
        if x.proj > tmp.proj:
            tmp = x
            print('1')

    return tmp

print('4')