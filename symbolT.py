import os, codecs, sys, re

class symbolTable():

    marathiSym = []
    sym = []
    value = []
    topIndex = 0

    def insertSymbol(self,currentSym):
        if(self.isNewsymbol(currentSym)):
            self.marathiSym.append(currentSym)
            self.topIndex = self.topIndex + 1
            self.sym.append("s"+"["+str(self.getIndex(currentSym))+"]")

            return self.sym[self.getIndex(currentSym)]
        else:
            return self.sym[self.getIndex(currentSym)]

    def getIndex(self,currentSym):
        for i in range(0,3*self.topIndex):
            if(self.marathiSym[i]==currentSym):
                return i

    def isNewsymbol(self,currentSym):
        for i in range(0,3*self.topIndex):
            if(self.marathiSym[i]==currentSym):
                return 0
        return 1


s = symbolTable()



