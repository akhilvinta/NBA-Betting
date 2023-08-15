import numpy as np
from PlayerSeasonData import PlayerSeasonData
from PlayerGameData import PlayerGameData
from Odds import Odds
import math

class PlayerCompare:
    def __init__(self, p1: PlayerSeasonData, p1Cat, p2: PlayerSeasonData, p2Cat):
        self.p1 = p1
        self.p2 = p2
        self.p1Cat = p1Cat
        self.p2Cat = p2Cat
        self.p1CatData, self.p2CatData = self.getPlayerDataFields()
        self.p1CatDataFiltered, self.p2CatDataFiltered, self.sampleSize = self.removeInactives()
        self.r, self.p1Mean, self.p2Mean = self.findMeanAndCorrelation()
        self.rAbs = abs(self.r)
        self.split = self.findSplits()
        self.uniformThreshold = 0.43
        self.minSampleSize = 40
        self.uniformFlag, self.distribution = self.findDistributionOverUnders()
        self.calculateEV3LegFlexNeutral()

    def __lt__(self, other):
        ## Ranking based on 3-leg flex EV
        # return self.EV < other.EV
        return self.r < other.r
        # return self.rAbs < other.rAbs

    def getPlayerDataFields(self):
        p1Data, p2Data = [], []
        for gameDataObj in self.p1.gameDataList:
            extractedDataField = self.extractDataFieldFromDataObject(gameDataObj, self.p1Cat)
            p1Data.append(extractedDataField)
        for gameDataObj in self.p2.gameDataList:
            extractedDataField = self.extractDataFieldFromDataObject(gameDataObj, self.p2Cat)
            p2Data.append(extractedDataField)
        return p1Data, p2Data

    def removeInactives(self):
        p1CatDataFiltered, p2CatDataFiltered = [], []
        for i in range(82):
            if self.p1CatData[i] != "Inactive" and self.p2CatData[i] != "Inactive":
                p1CatDataFiltered.append(self.p1CatData[i])
                p2CatDataFiltered.append(self.p2CatData[i])
        sampleSize = len(p1CatDataFiltered)
        return p1CatDataFiltered, p2CatDataFiltered, sampleSize
    
    def findMeanAndCorrelation(self):
        p1CatDataNumpy = np.array(self.p1CatDataFiltered)
        p2CatDataNumpy = np.array(self.p2CatDataFiltered)
        p1CatMean = np.mean(p1CatDataNumpy)
        p2CatMean = np.mean(p2CatDataNumpy)
        r = np.corrcoef(p1CatDataNumpy, p2CatDataNumpy)
        return r[0][1], p1CatMean, p2CatMean

    def findSplits(self):
        U_U, U_O, O_U, O_O = 0, 0, 0, 0
        for i in range(self.sampleSize):
            if self.p1CatDataFiltered[i] < self.p1Mean and self.p2CatDataFiltered[i] < self.p2Mean:
                U_U += 1
            elif self.p1CatDataFiltered[i] < self.p1Mean and self.p2CatDataFiltered[i] > self.p2Mean:
                U_O += 1
            elif self.p1CatDataFiltered[i] > self.p1Mean and self.p2CatDataFiltered[i] < self.p2Mean:
                O_U += 1
            elif self.p1CatDataFiltered[i] > self.p1Mean and self.p2CatDataFiltered[i] > self.p2Mean:
                O_O += 1
        # print("U_U: " + str(U_U) + ", U_O: " + str(U_O) + ", O_U: " + str(O_U) + ", O_O: " + str(O_O))
        self.splitTotals = [U_U, U_O, O_U, O_O]
        return [U_U/self.sampleSize, U_O/self.sampleSize, O_U/self.sampleSize, O_O/self.sampleSize]

    def extractDataFieldFromDataObject(self, gameData: PlayerGameData, category):
        if gameData.activeStatus == "Inactive":
            return "Inactive"
        try:
            return gameData.bettingFieldsMap[category]
        except KeyError:
            print("Invalid Category Key for PlayerCompare Object: (" \
                + str(self.p1.playerName) + " [" + self.p1Cat + "]" + ", " + str(self.p2.playerName) + " [" + self.p2Cat + "])")
            exit(1)
        
    def findDistributionOverUnders(self):
        p1Overs = [1 if val >= self.p1Mean else 0 for val in self.p1CatDataFiltered]
        p1Unders = [1 if val < self.p1Mean else 0 for val in self.p1CatDataFiltered]
        p2Overs = [1 if val >= self.p2Mean else 0 for val in self.p2CatDataFiltered]
        p2Unders = [1 if val < self.p2Mean else 0 for val in self.p2CatDataFiltered]

        assert sum(p1Overs) + sum(p1Unders) == self.sampleSize
        assert sum(p2Overs) + sum(p2Unders) == self.sampleSize

        overPercentage1 = sum(p1Overs)/self.sampleSize
        overPercentage2 = sum(p2Overs)/self.sampleSize
        uniformFlag = self.sampleSize >= self.minSampleSize and (overPercentage1 > self.uniformThreshold and overPercentage1 < (1-self.uniformThreshold)) and (overPercentage2 > self.uniformThreshold and overPercentage2 < (1-self.uniformThreshold))
        return uniformFlag, [overPercentage1, overPercentage2]
        # exit(1)

    def calculateEV3LegFlexNeutral(self):
        EVCalculator = Odds()
        self.EV, self.optimalBet = EVCalculator.threeLegFlexCalculation(self.split, .55)
        

    def printData(self):
        print("PlayerCompare Object: " + str(self.p1.playerName) + " [" + self.p1Cat + "]" + ", " + str(self.p2.playerName) + " [" + self.p2Cat + "])")
        print("p1 mean: " + str(self.p1Mean))
        print("p2 mean: " + str(self.p2Mean))
        print("sample size: " + str(self.sampleSize))
        print("distribution: " + str(self.distribution))
        print("r: " + str(self.r))
        print("split: " + str(self.split))
        print("EV: " + str(self.EV))

    def printDataConcise(self):
        print("PlayerCompare Object: " + str(self.p1.playerName) + " [" + self.p1Cat + "]" + ", " + str(self.p2.playerName) + " [" + self.p2Cat + "])")
        print("distribution: " + str(self.distribution))
        print("split: " + str(self.split))
        print("EV: " + str(self.EV))
        print("Bet: " + str(self.optimalBet))
        print("sampleSize: " + str(self.sampleSize))
        print("split: " + str(self.splitTotals))
    
    def printDataR(self):
        print("PlayerCompare Object: " + str(self.p1.playerName) + " [" + self.p1Cat + "]" + ", " + str(self.p2.playerName) + " [" + self.p2Cat + "])")
        print("split: " + str(self.split))
        print("EV: " + str(self.EV))
        print("r: " + str(self.r))
        # print("sampleSize: " + str(self.sampleSize))
        # print("optimal bet: " + str(self.optimalBet))
    


####   .4 OO  
####   .4 OO

# .16 * 

# .84 -- *0 
# .16 -- *10


# .84*0 + .16*10