import math

import numpy as np
import pandas as pd
from AlgoDynamique import ProgrammationDynamique


datas = pd.read_excel('DataProjet2023.xlsb', engine='pyxlsb', usecols='B,C,F,H,J,L,N,P', header=2, nrows=100)

diffpower = np.zeros(100)
totpower = np.zeros(100)

for i in range(100):
    hchute = datas['Niv Amont (m)'].loc[i] - datas['Elav (m)'].loc[i]
    Qtot = datas['Qtot (m3/s)'].loc[i]
    debitsmax = [160, 160, 160, 160, 160]
    solveur = ProgrammationDynamique(debitsmax,Qtot,hchute)
    debitsturbs,pmw = solveur.solve()
    pmwtot = pmw.sum()
    pmwreel = datas['P1 (MW)'].loc[i] + datas['P2 (MW)'].loc[i] + datas['P3 (MW)'].loc[i] + datas['P4 (MW)'].loc[i] + datas['P5 (MW)'].loc[i]
    diffpower[i] = pmwtot - pmwreel
    totpower[i] = pmwtot

SSE = (sum(diffpower**2))
SSR = (sum(totpower**2))
print(diffpower)
print("Erreur négative maximale "+min(diffpower))
print("Erreur positive maximale "+max(diffpower))
print("Somme des erreurs "+sum(diffpower))
print("Somme des erreurs carrées"+SSE)
print("R²="(1-SSE/SSR))

# hchute = datas['Niv Amont (m)'].loc[0] - datas['Elav (m)'].loc[0]
# Qtot = datas['Qtot (m3/s)'].loc[0]
#
# debitsmax = [160, 160, 160, 160, 160]
# solveur = ProgrammationDynamique(debitsmax,Qtot,hchute)
# debitsturbs,pmw = solveur.solve()
#
# print(debitsturbs)
# print(pmw)