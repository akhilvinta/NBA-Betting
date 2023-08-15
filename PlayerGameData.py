class PlayerGameData:
    def __init__(self, gameDataString):
        self.gameDataString = gameDataString
        self.populateDataFields(self.gameDataString)
        self.bettingFieldsMap = self.populateBettingFieldsMap()

    def populateDataFields(self, gds):
        # if gds[-1] == "Inactive" or gds[-1] == "Did Not Play" or gds[-1] == "Did Not Dress":
        if gds[-1] in ["Inactive", "Did Not Play", "Did Not Dress", "Not With Team"]:
            self.activeStatus = "Inactive"
            self.gameNumber, self.date, self.opponent, self.outcome = gds[0], gds[2], gds[6], gds[7] 
            self.homeOrAway = "away" if gds[5] == "@" else "home"
        else:
            self.activeStatus = "Active"
            self.gameNumber, self.date, self.opponent, self.outcome = int(gds[0]), gds[2], gds[6], gds[7]
            self.MP, self.FG, self.FGA = gds[9], int(gds[10]), int(gds[11])
            self.threePM, self.threePA = int(gds[13]), int(gds[14])
            self.FT, self.FTA = int(gds[16]), int(gds[17])
            self.ORB, self.DRB, self.TRB = int(gds[19]), int(gds[20]), int(gds[21])
            self.AST, self.STL, self.BLK = int(gds[22]), int(gds[23]), int(gds[24])
            self.TOV, self.PF = int(gds[25]), int(gds[26])
            self.PTS = int(gds[27])
            if gds[29] != '':
                self.plusMinus = int(gds[29])
            else:
                self.plusMinus = 0
    
    def populateBettingFieldsMap(self):
        if self.activeStatus == "Inactive":
            return None
        self.bettingFieldsMap = {}
        self.bettingFieldsMap["points"] = self.PTS
        self.bettingFieldsMap["p+r+a"] = self.PTS + self.TRB + self.AST
        self.bettingFieldsMap["rebounds"] = self.TRB
        self.bettingFieldsMap["orb"] = self.ORB
        self.bettingFieldsMap["drb"] = self.DRB
        self.bettingFieldsMap["assists"] = self.AST
        self.bettingFieldsMap["3PM"] = self.threePM
        self.bettingFieldsMap["3PA"] = self.threePA
        self.bettingFieldsMap["p+r"] = self.PTS + self.TRB
        self.bettingFieldsMap["p+a"] = self.PTS + self.AST
        self.bettingFieldsMap["r+a"] = self.TRB + self.AST
        self.bettingFieldsMap["fgm"] = self.FG
        self.bettingFieldsMap["fga"] = self.FGA
        self.bettingFieldsMap["ftm"] = self.FT
        self.bettingFieldsMap["fta"] = self.FTA
        self.bettingFieldsMap["blocks"] = self.BLK
        self.bettingFieldsMap["steals"] = self.STL
        self.bettingFieldsMap["turnovers"] = self.TOV
        self.bettingFieldsMap["fantasyScore"] = self.PTS + (1.2 * self.TRB) + (1.5 * self.AST) + (3 * (self.STL + self.BLK)) - self.TOV
        return self.bettingFieldsMap
    
    def printGameData(self):
        for attribute, value in vars(self).items():
            print(str(attribute) + ": " + str(value))
