class Odds:
    def __init__(self):
        return
    
    def twoLegPP(self, x,y):
        return 3 * x * y

    def threeLegPP(self, x,y,z):
        return 5 * x * y * z

    def fourLegPP(self, w,x,y,z):
        return 10 * w * x * y * z

    def threeLegFlex(self, x,y,z):
        return 2.25*x*y*z + (1.25 * (x*y*(1-z) + x*(1-y)*z + (1-x)*y*z)) 

    def threeLegFlexCalculation(self, split: list, x):
        [UU, UO, OU, OO] = split
        max((UU * 2.25 + UO * 1.25 + OU * 1.25), (UO * 2.25 + UU * 1.25 + OO * 1.25), (OU * 2.25 + UU * 1.25 + OO * 1.25), (OO * 2.25 + UO * 1.25 + OU * 1.25))
        bet = UU
        betUU = (UU * x * 2.25) + (1.25 * ((UO * x) + (OU * x) + (UU * (1-x))))
        betUO = (UO * x * 2.25) + (1.25 * ((OO * x) + (UU * x) + (UO * (1-x))))
        betOU = (OU * x * 2.25) + (1.25 * ((OO * x) + (UU * x) + (OU * (1-x))))
        betOO = (OO * x * 2.25) + (1.25 * ((OU * x) + (UO * x) + (OO * (1-x))))
        EV = [betUU, betUO, betOU, betOO]
        labels = ["UU", "UO", "OU", "OO"]
        maxIndex = EV.index(max(EV))
        return EV[maxIndex], labels[maxIndex]


    def fourLegFlex(self, w,x,y,z):
        return 5*w*x*y*z + 1.5 * (w*x*y*(1-z) + w*x*(1-y)*z + w*(1-x)*y*z + (1-w)*x*y*z)

    def fiveLegFlex(self, v,w,x,y,z):
        return 10*v*w*x*y*z + \
            2*(v*w*x*y*(1-z) + v*w*x*(1-y)*z + v*w*(1-x)*y*z + v*(1-w)*x*y*z + (1-v)*w*x*y*z) + \
            0.4 * (v*w*(1-x)*(1-y)*(1-z) + v*(1-w)*x*(1-y)*(1-z) + v*(1-w)*(1-x)*y*(1-z) + v*(1-w)*(1-x)*(1-y)*z + (1-v)*w*x*(1-y)*(1-z) + (1-v)*w*(1-x)*y*(1-z) + (1-v)*w*(1-x)*(1-y)*z + (1-v)*(1-w)*x*y*(1-z) + (1-v)*(1-w)*x*(1-y)*z + (1-v)*(1-w)*(1-x)*y*z)

    def sixLegFlex(self,u,v,w,x,y,z):
        return 25*u*v*w*x*y*z +\
            2*(u*v*w*x*y*(1-z)+ u*v*w*x*(1-y)*z + u*v*w*(1-x)*y*z + u*v*(1-w)*x*y*z + u*(1-v)*w*x*y*z + (1-u)*v*w*x*y*z) +\
            0.4*(u*v*w*x*(1-y)*(1-z) + u*v*w*(1-x)*y*(1-z) + u*v*(1-w)*x*y*(1-z) + u*(1-v)*w*x*y*(1-z) + (1-u)*v*w*x*y*(1-z) +\
                u*v*w*(1-x)*(1-y)*z + u*v*(1-w)*x*(1-y)*z + u*(1-v)*w*x*(1-y)*z + (1-u)*v*w*x*(1-y)*z +\
                u*v*(1-w)*(1-x)*y*z + u*(1-v)*w*(1-x)*y*z + (1-u)*v*w*(1-x)*y*z +\
                u*(1-v)*(1-w)*x*y*z + (1-u)*v*(1-w)*x*y*z +\
                (1-u)*(1-v)*w*x*y*z)

    def helpfulInfo(self):
        print("options for this function are as follows:")
        print("\t-- twoLegPP\n\t-- threeLegPP\n\t-- fourLegPP\n\t-- threeLegFlex\n\t-- fourLegFlex\n\t-- fiveLegFlex\n\t-- sixLegFlex\n\t-- all")
        exit(0)

    def getOdds(self, parlayType=None):
        if not parlayType:
            self.helpfulInfo()
        flag = (parlayType == "all")
        if "two" in parlayType or flag:
            print("odds for " + str(parlayType) + ": " + str(self.twoLegPP(.5,.5)))
            return self.twoLegPP(.5,.5)
        if ("three" in parlayType and "PP" in parlayType) or flag:
            print("odds for " + str(parlayType) + ": " + str(self.threeLegPP(.5,.5)))
            return self.threeLegPP(.5,.5,.5)
        if ("three" in parlayType and "flex" in parlayType) or flag:
            print("odds for " + str(parlayType) + ": " + str(self.threeLegFlex(.5,.5,.5)))
            return self.threeLegFlex(.5,.5,.5)
        if ("four" in parlayType and "PP" in parlayType) or flag:
            print("odds for " + str(parlayType) + ": " + str(self.fourLegPP(.5,.5,.5,.5)))
            return self.fourLegPP(.5,.5,.5,.5)
        if ("four" in parlayType and "flex" in parlayType) or flag:
            print("odds for " + str(parlayType) + ": " + str(self.fourLegFlex(.5,.5,.5,.5)))
            return self.fourLegFlex(.5,.5,.5,.5)
        if "five" in parlayType or flag:
            print("odds for " + str(parlayType) + ": " + str(self.fiveLegFlex(.5,.5,.5,.5,.5)))
            return self.fiveLegFlex(.5,.5,.5,.5,.5)
        if "six" in parlayType or flag:
            print("odds for " + str(parlayType) + ": " + str(self.sixLegFlex(.5,.5,.5,.5,.5,.5)))
            return self.sixLegFlex(.5,.5,.5,.5,.5,.5)


odds = Odds()
print(odds.twoLegPP(.58,.58))
