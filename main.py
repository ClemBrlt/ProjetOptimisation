import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from AlgoDynamique import ProgrammationDynamique

start = time.time()

datas = pd.read_excel('DataProjet2023.xlsb', engine='pyxlsb', usecols='B,C,F,H,J,L,N,P', header=2, nrows=100)

diffpower = np.zeros(100)
totpower = np.zeros(100)
debitstotaux = np.zeros([100,5])
sumDifnbTurb = 0;

for i in range(100):
    hchute = datas['Niv Amont (m)'].loc[i] - datas['Elav (m)'].loc[i]
    Qtot = datas['Qtot (m3/s)'].loc[i]
    debitsmax = [160, 160, 160, 160, 160]
    solveur = ProgrammationDynamique(debitsmax,Qtot,hchute)
    debitsturbs,pmw = solveur.solve()
    pmwtot = pmw.sum()
    pmwreel = datas['P1 (MW)'].loc[i] + datas['P2 (MW)'].loc[i] + datas['P3 (MW)'].loc[i] + datas['P4 (MW)'].loc[i] + datas['P5 (MW)'].loc[i]
    nbTurbreel = int(datas['P1 (MW)'].loc[i] > 0) + int(datas['P2 (MW)'].loc[i] > 0) + int(datas['P3 (MW)'].loc[i] > 0) + int(datas['P4 (MW)'].loc[i] > 0) + int(datas['P5 (MW)'].loc[i] > 0)
    nbTurbSim = int(pmw[0] > 0) + int(pmw[1] > 0) + int(pmw[2] > 0) + int(pmw[3] > 0) + int(pmw[4] > 0)
    sumDifnbTurb += abs(nbTurbSim - nbTurbreel)
    diffpower[i] = pmwtot - pmwreel
    totpower[i] = pmwtot
    debitstotaux[i]=debitsturbs

end = time.time()

SSE = (sum(diffpower**2))
SSR = (sum(totpower**2))

for i in range(100):
    print("Débits: "+str(debitstotaux[i])+" Puissance totale: "+str(totpower[i]))
print("Somme des erreurs sur le nombre de turbines: " + str(sumDifnbTurb))
print("Erreur négative maximale: "+str(min(diffpower))+" MW")
print("Erreur positive maximale: "+str(max(diffpower))+" MW")
print("Somme des erreurs: "+str(sum(diffpower))+" MW")
print("Somme des erreurs carrées: "+str(SSE)+" MW²")
print("R²: "+str((1-SSE/SSR)))
print("Temps d'éxécution: "+str(end-start)+" s")


legend = np.arange(1,101)
plt.figure(figsize=(1, 2))
plt.subplot(121)
plt.bar(legend,totpower)
plt.xlabel('Ligne du fichier')
plt.ylabel('Puissance (MW)')
plt.subplot(122)
plt.bar(legend,diffpower)
plt.xlabel('Ligne du fichier')
plt.ylabel('Différence de puissance (MW)')
plt.show()