from PlayerSeasonData import PlayerSeasonData
from PlayerCompare import PlayerCompare
from TeamDatabase import TeamDataBase
from NBARosterList import NBARosterList

# runbook = TeamDataBase("output.txt", "Warriors", ["StephenCurry", "DraymondGreen", "KlayThompson", "AndrewWiggins", "KevonLooney", "JordanPoole"])
# runbook = TeamDataBase("output.txt", "Warriors", ["StephenCurry", "DraymondGreen", "KlayThompson", "AndrewWiggins", "JordanPoole"])

# print(len(runbook.playerCompareList))


# maxVal = -1
# maxObj = None

# sortedPlayerComps = sorted(runbook.playerCompareList)
# for obj in sortedPlayerComps:
#     obj.printDataR()

# print(len(sortedPlayerComps))

# teamRunbook = []
rosterList = NBARosterList()
# nuggetsTeam = TeamDataBase("output.txt", "Nuggets", rosterList.teamsMap["Nuggets"])
# for player in nuggetsTeam.playerObjList:
#     print(player.playerName + ", " + str(player.numGamesPlayed))

# sortedPlayerComps = sorted(nuggetsTeam.playerCompareList)
# for playerComp in sortedPlayerComps:
#     print(playerComp.printDataR())

hawksTeam = TeamDataBase("output.txt", "Nuggets", rosterList.teamsMap["Nuggets"])
for player in hawksTeam.playerObjList:
    print(player.playerName + ", " + str(player.numGamesPlayed))

sortedPlayerComps = sorted(hawksTeam.playerCompareList)
for playerComp in sortedPlayerComps:
    print(playerComp.printDataR())

# warriorsTeam = TeamDataBase("output.txt", "Warriors", rosterList.teamsMap["Warriors"])
# for player in warriorsTeam.playerObjList:
#     print(player.playerName + ", " + str(player.numGamesPlayed))

# sortedPlayerComps = sorted(warriorsTeam.playerCompareList)
# for playerComp in sortedPlayerComps:
#     print(playerComp.printDataR())
# print(len(nuggetsTeam.playerCompareList))
