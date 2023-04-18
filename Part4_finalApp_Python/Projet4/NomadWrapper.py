import numpy as np
import subprocess
class NomadWrapper:

    DebitsMax = np.zeros(5)
    DebitDispo = 0
    HChute = 0
    pathParam = 'nomad.3.9.1_Personal/bin/param.txt'
    runNomad = 'nomad.3.9.1_Personal/bin'
    pathResult = 'nomad.3.9.1_Personal/bin/test.0.txt'

    def __init__(self, debitsmax, debitdispo, hchute):
        self.DebitsMax = debitsmax
        self.DebitDispo = debitdispo
        self.HChute = hchute
    def SetParam(self):
        with open(self.pathParam, 'r', encoding='utf-8') as file:
            data = file.readlines()

        print(data[18]+data[20]+data[21])
        data[18]='X0             ( 0 0 0 0 0 '+str(self.DebitDispo)[0:5]+' '+str(self.HChute)[0:5]+')  # starting point\n'
        data[20]='LOWER_BOUND    ( 0 0 0 0 0 '+str(self.DebitDispo)[0:5]+' '+str(self.HChute)[0:5]+' )           #\n'
        data[21]='UPPER_BOUND    ( '+str(self.DebitsMax[0])+' '+str(self.DebitsMax[1])+' '+str(self.DebitsMax[2])+' '+str(self.DebitsMax[3])+' '+str(self.DebitsMax[4])+' '+str(self.DebitDispo)[0:5]+' '+str(self.HChute)[0:5]+' )  # all are bounded\n '


        with open(self.pathParam, 'w', encoding='utf-8') as file:
             file.writelines(data)
        return 0

    def RunNomad(self):
        subprocess.run(["nomad.3.9.1_Personal/bin/nomad.exe","param.txt"],cwd="nomad.3.9.1_Personal/bin/")

    def ReadResult(self):
        with open(self.pathResult, 'r', encoding='utf-8') as file:
            data = file.readlines()
        lastline = data[len(data)-1].split()
        debits = np.zeros(5)
        for i in range(5):
            debits[i] = float(lastline[2+i])
        return debits,-float(lastline[len(lastline)-1])