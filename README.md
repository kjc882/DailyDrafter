# DailyDrafter
Create Near Optimal NFL Daily Draft Lineup using Annealing and Knapsack concepts
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
