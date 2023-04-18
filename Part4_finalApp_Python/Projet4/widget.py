# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from AlgoDynamique import ProgrammationDynamique
from FonctionsProduction import FonctionsProduction
from NomadWrapper import NomadWrapper

from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtUiTools import QUiLoader

class Widget(QWidget):

    debitDispo = np.zeros(1);
    Hchute = np.zeros(1);
    DebitsMax = np.zeros(5)
    pathFile = ''
    nbLines = 0
    debitstotaux = np.zeros([1,5])
    powers = np.zeros([1,5])

    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()
        self.DynaButton = self.findChild(QtWidgets.QPushButton,"DynaButton")
        self.DynaButton.clicked.connect(self.clickDynamic)

        self.NOMADButton = self.findChild(QtWidgets.QPushButton,"BBButton")
        self.NOMADButton.clicked.connect(self.clickNOMAD)

        self.BrowseButton = self.findChild(QtWidgets.QPushButton,"browseButton")
        self.BrowseButton.clicked.connect(self.clickBrowse)

        self.GraphButton = self.findChild(QtWidgets.QPushButton,"graphButton")
        self.GraphButton.clicked.connect(self.displayGraph)

        self.Manuel = self.findChild(QtWidgets.QRadioButton,"radioButton")
        self.DebitBox = self.findChild(QtWidgets.QSpinBox,"DebitBox")
        self.HChuteBox = self.findChild(QtWidgets.QDoubleSpinBox,"HchuteBox")
        self.pathDisplay = self.findChild(QtWidgets.QLineEdit,"linePath")
        self.pathDisplay.setReadOnly(True)
        self.lineStartBox = self.findChild(QtWidgets.QSpinBox,"lineStart")
        self.lineEndBox = self.findChild(QtWidgets.QSpinBox,"lineEnd")

        self.T1Box = self.findChild(QtWidgets.QSpinBox,"T1Box")
        self.T2Box = self.findChild(QtWidgets.QSpinBox,"T2Box")
        self.T3Box = self.findChild(QtWidgets.QSpinBox,"T3Box")
        self.T4Box = self.findChild(QtWidgets.QSpinBox,"T4Box")
        self.T5Box = self.findChild(QtWidgets.QSpinBox,"T5Box")

        self.Q1 = self.findChild(QtWidgets.QLabel,"Q1")
        self.Q2 = self.findChild(QtWidgets.QLabel,"Q2")
        self.Q3 = self.findChild(QtWidgets.QLabel,"Q3")
        self.Q4 = self.findChild(QtWidgets.QLabel,"Q4")
        self.Q5 = self.findChild(QtWidgets.QLabel,"Q5")
        self.QTot = self.findChild(QtWidgets.QLabel,"QTot")

        self.P1 = self.findChild(QtWidgets.QLabel,"P1")
        self.P2 = self.findChild(QtWidgets.QLabel,"P2")
        self.P3 = self.findChild(QtWidgets.QLabel,"P3")
        self.P4 = self.findChild(QtWidgets.QLabel,"P4")
        self.P5 = self.findChild(QtWidgets.QLabel,"P5")
        self.PTot = self.findChild(QtWidgets.QLabel,"PTot")

        self.ProgBar = self.findChild(QtWidgets.QProgressBar,"progressBar")
        self.ProgBar.setValue(0)

    def load_ui(self):
        loader = QUiLoader()
        path = Path(__file__).resolve().parent / "form.ui"
        ui_file = QtCore.QFile(path)
        ui_file.open(QtCore.QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    @QtCore.Slot()
    def clickDynamic(self):
        self.getDatasSettings()
        self.debitstotaux = np.zeros([self.nbLines,5])
        self.powers = np.zeros([self.nbLines,5])
        for i in range(self.nbLines):
            solveur = ProgrammationDynamique(self.DebitsMax,self.debitDispo[i],self.Hchute[i])
            debitsturbs,pmw = solveur.solve()
            self.debitstotaux[i]=debitsturbs
            self.powers[i]=np.round(pmw,3)
            self.ProgBar.setValue(((i+1)/self.nbLines)*100)
        self.setResults(i)

    @QtCore.Slot()
    def clickNOMAD(self):
        self.getDatasSettings()
        self.debitstotaux = np.zeros([self.nbLines,5])
        self.powers = np.zeros([self.nbLines,5])
        for i in range(self.nbLines):
            NWrapper = NomadWrapper(self.DebitsMax,self.debitDispo[i],self.Hchute[i])
            NWrapper.SetParam()
            NWrapper.RunNomad()
            debitsturbs,pmwtot = NWrapper.ReadResult()
            self.debitstotaux[i]=debitsturbs
            self.recontructPMW(i)
            print(self.powers[i].sum())
            print(pmwtot)
            self.ProgBar.setValue(((i+1)/self.nbLines)*100)
        self.setResults(i)

    @QtCore.Slot()
    def clickBrowse(self):
        filename,_ = QtWidgets.QFileDialog.getOpenFileName(self, "Selectionnez un fichier", "C:\\", "Excel File (*.xlsb)")
        if filename:
            self.pathFile = str(Path(filename))
            self.pathDisplay.setText(self.pathFile)

    def getDatasSettings(self):
        self.ProgBar.setValue(0)
        if(self.Manuel.isChecked()):
            self.debitDispo = np.zeros(1);
            self.Hchute = np.zeros(1);
            self.Hchute[0] = self.HChuteBox.value()
            self.debitDispo[0] = self.DebitBox.value();
            self.nbLines = 1
        else:
            startLine = self.lineStartBox.value()
            endLine = self.lineEndBox.value()
            self.nbLines = endLine - startLine +1
            self.debitDispo = np.zeros(self.nbLines);
            self.Hchute = np.zeros(self.nbLines);
            datas = pd.read_excel(self.pathFile, engine='pyxlsb', usecols='B,C,F', header=2, nrows=self.nbLines, skiprows=range(3,startLine+2))
            for i in range(self.nbLines):
                self.debitDispo[i] = datas['Qtot (m3/s)'].loc[i]
                self.Hchute[i] = datas['Niv Amont (m)'].loc[i] - datas['Elav (m)'].loc[i]
        self.DebitsMax[0] = self.T1Box.value();
        self.DebitsMax[1] = self.T2Box.value();
        self.DebitsMax[2] = self.T3Box.value();
        self.DebitsMax[3] = self.T4Box.value();
        self.DebitsMax[4] = self.T5Box.value();

    def setResults(self,i):
         self.P1.setText(str(self.powers[i,0]))
         self.P2.setText(str(self.powers[i,1]))
         self.P3.setText(str(self.powers[i,2]))
         self.P4.setText(str(self.powers[i,3]))
         self.P5.setText(str(self.powers[i,4]))
         self.PTot.setText(str(round(self.powers[i].sum(),3)))

         self.Q1.setText(str(self.debitstotaux[i,0]))
         self.Q2.setText(str(self.debitstotaux[i,1]))
         self.Q3.setText(str(self.debitstotaux[i,2]))
         self.Q4.setText(str(self.debitstotaux[i,3]))
         self.Q5.setText(str(self.debitstotaux[i,4]))
         self.QTot.setText(str(self.debitstotaux[i].sum()))

    @QtCore.Slot()
    def displayGraph(self):
        legend = np.arange(self.lineStartBox.value(),self.nbLines+self.lineStartBox.value())
        plt.figure(figsize=(2, 3))
        for i in range(1,6):
            plt.subplot(2,3,i)
            debits = np.zeros(self.nbLines)
            for j in range(self.nbLines):
                debits[j] = self.debitstotaux[j][i-1]
            plt.bar(legend,debits)
            plt.xlabel('Ligne du fichier')
            plt.ylabel('Debit Turbiné '+str(i)+' (m3/s)')
        plt.show()

    def recontructPMW(self,i):
        for j in range(5):
            modele = FonctionsProduction()
            self.powers[i,j] = round(modele.productionturbinei(self.debitstotaux[i,j],self.Hchute[i],j),3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
