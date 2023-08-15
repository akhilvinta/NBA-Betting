from PlayerGameData import PlayerGameData

class PlayerSeasonData:
    def __init__(self, playerName, teamName):
        self.dataFileName = "./Stats/" + teamName + "/" + playerName + ".csv"
        self.dataFile = open(self.dataFileName, "r")
        self.playerName = playerName
        self.teamName = teamName
        self.gameDataList = []
        self.fillSeasonData()
        self.numGamesPlayed = self.getNumGamesPlayed()
    
    def fillSeasonData(self):
        count = 0
        for line in self.dataFile:
            gameData = line.strip("\n").split(",")
            if gameData[0] != "Rk":
                currentGameData = PlayerGameData(gameData)
                self.gameDataList.append(currentGameData)
            count += 1

    def getNumGamesPlayed(self):
        count = 0
        for gameData in self.gameDataList:
            count = count + 1 if gameData.activeStatus == "Active" else count
        return count
        
