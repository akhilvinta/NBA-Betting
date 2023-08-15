from PlayerSeasonData import PlayerSeasonData
from PlayerSeasonData import PlayerSeasonData
from PlayerGameData import PlayerGameData
from PlayerCompare import PlayerCompare

class TeamDataBase:
    def __init__(self, outputFile, teamName, playerNames: list):
        self.outputFile = open(outputFile, "a")
        self.teamName = teamName
        self.playerNames = playerNames
        self.playerObjList = []
        self.playerCompareList = []
        self.createPlayerSeasonObjects()
        self.findTeamSplits()


    def createPlayerSeasonObjects(self):
        for player in self.playerNames:
            self.playerObjList.append(PlayerSeasonData(player, self.teamName))
        return None
    
    def findTeamSplits(self):
        for i in range(len(self.playerObjList)):
            for j in range(i+1, len(self.playerObjList)):
                self.findIndividualPairSplits(self.playerObjList[i], self.playerObjList[j])
    
    def findIndividualPairSplits(self, p1: PlayerSeasonData, p2: PlayerSeasonData):
        categories = ["points", "p+r+a", "rebounds", "assists", "3PM", "3PA", "p+r", "p+a", "r+a", "fgm", "fga", "ftm", "fta", "blocks", "steals", "turnovers", "fantasyScore"]
        commonCategories = ["points", "p+r+a", "rebounds", "orb", "drb", "assists", "3PM", "3PA", "p+r", "p+a", "r+a", "fgm", "fga", "ftm", "fta", "fantasyScore"]
        # commonCategories = ["points", "rebounds", "assists"]
        
        for i in range(len(commonCategories)):
            for j in range(len(commonCategories)):
                compareData = PlayerCompare(p1, commonCategories[i], p2, commonCategories[j])
                if compareData.uniformFlag: 
                    self.playerCompareList.append(compareData)
