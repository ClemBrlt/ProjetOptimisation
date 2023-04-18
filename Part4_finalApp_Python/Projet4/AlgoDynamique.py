import numpy as np
from FonctionsProduction import FonctionsProduction


class ProgrammationDynamique:

    DebitsMax = np.zeros(5)
    Pas = 5
    EtatsMax = np.zeros(5, dtype='int')
    modeles = FonctionsProduction()

    def __init__(self, debitsmax, debitdispo, hchute):
        self.DebitsMax = debitsmax
        for i in range(5):
            self.EtatsMax[i] = int(self.DebitsMax[i] / self.Pas)
        self.DebitDispo = self.Pas * round(debitdispo/self.Pas)
        self.StepMaxDebit = int(self.DebitDispo / self.Pas)
        self.Resultats = np.zeros([5, self.StepMaxDebit + 1], dtype='int')
        self.Hchute = hchute

    def calcstep(self, resultatsprecpow, step, stepmindebit):
        newresultatspow = np.zeros(self.StepMaxDebit + 1)
        newresultatsdeb = np.zeros(self.StepMaxDebit + 1, dtype='int')
        for i in range(stepmindebit, self.StepMaxDebit + 1):
            pmw = resultatsprecpow[i]
            debitopti = 0
            for j in range(1, min(self.EtatsMax[step], i) + 1):
                ppot = self.modeles.productionturbinei(j*self.Pas,self.Hchute,step) + resultatsprecpow[i-j]
                if ppot > pmw:
                    pmw = ppot
                    debitopti = j
            newresultatsdeb[i] = debitopti
            newresultatspow[i] = pmw
        return newresultatspow, newresultatsdeb

    def fillresult(self):
        tabpow = np.zeros(self.StepMaxDebit+1)
        stepmin = self.StepMaxDebit
        for i in range(5):
            stepmin -= self.EtatsMax[i]
        for i in range(4, -1, -1):
            stepmin += self.EtatsMax[i]
            tabpow,tabdeb = self.calcstep(tabpow, i, max(stepmin, 0))
            self.Resultats[i, :] = tabdeb
        return 0

    def solve(self):
        self.fillresult()
        debitsturbines = np.zeros(5)
        pmw = np.zeros(5)
        stepdispo = self.StepMaxDebit
        for i in range(5):
            etat_optimal = self.Resultats[i, stepdispo]
            debitsturbines[i] = etat_optimal*5
            stepdispo -= etat_optimal
            pmw[i] = self.modeles.productionturbinei(etat_optimal*self.Pas, self.Hchute, i)
        return debitsturbines, pmw
