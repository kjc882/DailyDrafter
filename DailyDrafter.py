#DraftKings Daily Drafting Application
#Authored by Kieran Chang

"""
HIGH LEVEL

Pull in Raw player data from API
Process data to determine each player's projected scores
Create lineup of players with highest projected for necessary positions
    NOTE: Ignore Salary Cap
While Lineup total Salary > Salary Cap, Update Lineup with "next best" for a single position
    "Next Best"  determined by having smallest projection gap among ALL positions while still having lower salary
Output final lineup
"""
"""
MEDIUM LEVEL

playerHolder[] = playerData()
freeAgents = calcProj(playerHolder[])
lineup = createLineup(freeAgents)
for all players in lineup
    trimPool(lineup.player.position, lineup.player.salary)
if total lineup.salary > salary cap
    lineup1 = createLineup(freeAgents)
else
    print lineUp
    END
while total lineup.salary > salary cap
    holder[] findMinDif(lineup, lineup1)
    swap(holder[0], holder[1], lineup1, lineup2)
    updateLine(lineup1, holder[0].pos)
print lineup
END
"""
""" 
FUNCTIONS

sendRequest()
    pull down data from API

calcProj(playerHolder)
    Let X be games played where X = 0 is most recent, 0 <= X <= 50
    for all players
        for all player.yards[X]
            player.proj += ((1 + (count(player.yards) * .005) - (X * .01)) * player.yards[X] * (pt / yard))
        player.proj = player.proj / count(player.yards)
    return all players

createLineup(freeAgents)
    for all positions
        choice = findMax(players, position)
        lineup += choice
        players.remove(choice)

findmax(players, position)
    for all players with given position
        find max projected points
    return player index

trimPool(position, salary1)
    for all players with given position in freeAgents
        remove all freeAgents where player.salary >= salary1

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

updateLine(lineup, position)
    choice = findMax(freeAgents, position)
        lineup += choice
        freeAgents.remove(choice)
        trimPool(freeAgents, position, choice.salary)
"""
"""
OBJECT DEFINITION

CURRENTLY NOT IN USE

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

# class ProcessedPlayer(object):
#     name = ""
#     pos = ""
#     proj = 0
#     sal = 0
#
#     def __init__(self, name, pos, proj, sal):
#         self.name = name
#         self.pos = pos
#         self.proj = proj
#         self.sal = sal

POSLIST = ["QB", "WR", 'R', 'K', 'D', 'F', "TE"]

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

        with open('players.json', 'w', encoding = 'utf-8') as File:
            json.dump(format(response.content), File)

    except requests.exceptions.RequestException:
        print('HTTP Request failed')

"""
calculate player projected point
Create weighted average of yards per game and multiply by points per yard
    Points per yard are created as Constants
freeAgents: list of every player not in a lineUp
"""
def calcProjection(freeAgents):
    #TODO: Does not include defensive stats
    for player in freeAgents:
        for game in player.games:
            count += 1

        tmpCount = count
        for game in player.games:
            total = (1 + (tmpCount/200)) * (game.passingyards * PPPY + game.rushingyards * PPRY + game.receivingyards *
                                            PPRecY + game.kickingyards * PPKY + game.td * PPTD + game.receptions * PPR)
            tmpCount -= 2
        player.proj = (total/count)

"""
createLineup(freeAgents)
    for all positions
        choice = findMax(players, position)
        lineup += choice
        players.remove(choice)
"""
def createLineup(freeAgents):
    lineup = []
    for position in POSLIST:
        choice = findMax(freeAgents, position)
        lineup += choice
        freeAgents.delete(choice)
    return lineup

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

"""
Remove players from the freeAgent list with >= salary compared to current lineup selections
pos: position of current player in lineup
salary: salary of current player in lineup
"""
def trimPool(pos,salary):
    for player in freeAgents:
        if player.position == pos:
            if player.salary >= salary:
                freeAgents.remove(player)

"""
Find the player (in the same position) with minimum difference in projected points between the two lineups
lineup1: current lineup
lineup2: second highest point total lineup
"""
def findMinDif(lineup1, lineup2):
    holder = lineup1[0].projection
    for p in lineup1:
        for p2 in lineup2:
            if p.position == p2.position & (p.projection - p2.projection) < holder:
                print("hi")


def swap(p1, p2, lineup1, lineup2):
    print(1)

def updateLine(lineup, pos):
    print(2)

send_request()

print("Started Reading JSON file")
with open("players.json") as json_file:
    print("Converting JSON encoded data into Python dictionary")
    player = json.load(json_file)
    print("Type: ", type(player))

    print("Decoded JSON Data From File")
    for x in range(10):
        print(player[x])

    print("Done reading json file")

freeAgents = calcProjection()

lineup = createLineup(freeAgents)
for p in lineup:
    trimPool(p.position, p.salary)

totalSal = 0
for p in lineup:
    totalSal += p.salary

if totalSal > salCap:
    lineup1 = createLineup(freeAgents)
else:
    print (lineUp)
    quit()

while totalSal > salCap:
    holder = findMinDif(lineup, lineup1)
    swap(holder[0], holder[1], lineup, lineup1)
    updateLine(lineup1, holder[0].pos)

print(lineup)
quit()