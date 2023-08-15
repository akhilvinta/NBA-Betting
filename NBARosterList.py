class NBARosterList:
    def __init__(self):
        self.TeamDatabaseList = []
        self.teamsMap = {}
        self.addTeams()

    def addTeams(self):
        self.teamsMap["Warriors"] = ["StephenCurry", "KlayThompson", "AndrewWiggins", "DraymondGreen", "KevonLooney", "JordanPoole"]
        self.teamsMap["Hawks"] = ["TraeYoung", "DejounteMurray", "BogdanBogdanovic", "JohnCollins", "ClintCapela"]
        self.teamsMap["Nuggets"] = ["JamalMurray", "KCP", "MichaelPorter", "AaronGordon", "NikolaJokic"]
