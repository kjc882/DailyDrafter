#TODO: ADJUST TRIMMING, MULTIPLE OF THE SAME POSITION IN LINEUP
#TODO: CHANGE PROCESS OF LOWERING LINEUP TO FIT IN SALARY CAP
#TODO: LOOK AT USING UPDATELINE FUNCTION IN CREATELINEUP

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
    lineup2 = createLineup(players)
    while (lineup1.totalSal > maxSal)
        holder[] findMinDif(lineup1, lineup2)
        swap(holder[0], holder[1], lineup1, lineup2)
        updateLine(lineup2, holder[0].pos)

findMinDif(lineup1, lineup2)
    for player1 in Lineup1
	    for player2 in Lineup2
		    if player1.pos = player2.pos && (player1.proj - player2.proj) < holder.proj
		        holder1 = player1
			    holder2 = player2

swap(player1, player2, lineup1, lineup2)
    lineup1.remove(player1)
    lineup1 += player2
    lineup2.remove(player2)

updateLine(lineup2, position)
    choice = findMax(players, position)
        lineup += choice
        players.remove(choice)
        trimPool(players, position, choice.salary)

PLAYER OBJECT DEFINITION(assuming all data must be stored in Player Objects rather than raw database)
    Name: Player's name
    Projected Points: number of points projected for the coming week
    Salary: Amount of money required for player
    Position: QB, WR, R, K, D, F, TE
    RYards: Array of RUSHING yards over past X number of games
    RecYards: Array of RECEIVING yards over past X number of games
    PYards: Array of PASSING yards over past X number of games(only for QB, 0 for others)

PROCESSEDPLAYER OBJECT DEFINITION
    Name: Player's Name
    Pos: Player Position
    Proj: Projected Points
    Sal: Player's Salary
"""
import base64
import requests
import json

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
            url = ' https://api.mysportsfeeds.com/v2.1/pull/nfl/2019-regular/week/1/player_gamelogs.json' ,
            params = {
                "fordate": "20161121"
            },
            headers = {
                "Authorization": "Basic " + base64.b64encode('{}:{}'.format('cc0ccd01-3831-448a-a562-fd6585','MYSPORTSFEEDS').encode('utf-8')).decode('ascii')
            }
        )

        with open('test.txt', 'w', encoding = 'utf-8') as File:
            json.dump(format(response.content), File)

    except requests.exceptions.RequestException:
        print('HTTP Request failed')

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

        #if current player projection is greater than tmp projection, overwrite tmp
        if x.proj > tmp.proj:
            tmp = x
            print('1')

    return tmp

send_request()

print(4)