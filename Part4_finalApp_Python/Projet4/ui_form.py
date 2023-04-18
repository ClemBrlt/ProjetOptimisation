# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(599, 476)
        Widget.setContextMenuPolicy(Qt.NoContextMenu)
        self.verticalLayout_11 = QVBoxLayout(Widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(48, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.linePath = QLineEdit(Widget)
        self.linePath.setObjectName(u"linePath")

        self.horizontalLayout_3.addWidget(self.linePath)

        self.browseButton = QPushButton(Widget)
        self.browseButton.setObjectName(u"browseButton")

        self.horizontalLayout_3.addWidget(self.browseButton)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineStart = QSpinBox(Widget)
        self.lineStart.setObjectName(u"lineStart")
        self.lineStart.setMinimum(1)
        self.lineStart.setMaximum(99999)

        self.horizontalLayout_2.addWidget(self.lineStart)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEnd = QSpinBox(Widget)
        self.lineEnd.setObjectName(u"lineEnd")
        self.lineEnd.setMinimum(1)
        self.lineEnd.setMaximum(99999)

        self.horizontalLayout_2.addWidget(self.lineEnd)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.line = QFrame(Widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radioButton = QRadioButton(Widget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_5.addWidget(self.radioButton)

        self.horizontalSpacer = QSpacerItem(57, 22, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.DebitBox = QSpinBox(Widget)
        self.DebitBox.setObjectName(u"DebitBox")
        self.DebitBox.setMaximum(1000)

        self.horizontalLayout_5.addWidget(self.DebitBox)

        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.HchuteBox = QDoubleSpinBox(Widget)
        self.HchuteBox.setObjectName(u"HchuteBox")

        self.horizontalLayout_5.addWidget(self.HchuteBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_11.addLayout(self.verticalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(Widget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.T1Box = QSpinBox(Widget)
        self.T1Box.setObjectName(u"T1Box")
        self.T1Box.setMaximum(160)
        self.T1Box.setValue(160)

        self.horizontalLayout_6.addWidget(self.T1Box)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(Widget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.T4Box = QSpinBox(Widget)
        self.T4Box.setObjectName(u"T4Box")
        self.T4Box.setMaximum(160)
        self.T4Box.setValue(160)

        self.horizontalLayout_9.addWidget(self.T4Box)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_11.addLayout(self.verticalLayout_3)

        self.line_7 = QFrame(Widget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_7)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(Widget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.T2Box = QSpinBox(Widget)
        self.T2Box.setObjectName(u"T2Box")
        self.T2Box.setMaximum(160)
        self.T2Box.setValue(160)

        self.horizontalLayout_7.addWidget(self.T2Box)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(Widget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.T5Box = QSpinBox(Widget)
        self.T5Box.setObjectName(u"T5Box")
        self.T5Box.setMaximum(160)
        self.T5Box.setValue(160)

        self.horizontalLayout_10.addWidget(self.T5Box)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_2)

        self.line_8 = QFrame(Widget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_8)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(Widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(True)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.T3Box = QSpinBox(Widget)
        self.T3Box.setObjectName(u"T3Box")
        self.T3Box.setMaximum(160)
        self.T3Box.setValue(160)

        self.horizontalLayout_8.addWidget(self.T3Box)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_11.addLayout(self.verticalLayout)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.DynaButton = QPushButton(Widget)
        self.DynaButton.setObjectName(u"DynaButton")

        self.horizontalLayout_12.addWidget(self.DynaButton)

        self.BBButton = QPushButton(Widget)
        self.BBButton.setObjectName(u"BBButton")

        self.horizontalLayout_12.addWidget(self.BBButton)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_11.addWidget(self.progressBar)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_14 = QLabel(Widget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)


        self.verticalLayout_11.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_15 = QLabel(Widget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_16.addWidget(self.label_15)

        self.Q1 = QLabel(Widget)
        self.Q1.setObjectName(u"Q1")

        self.horizontalLayout_16.addWidget(self.Q1)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_16 = QLabel(Widget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_15.addWidget(self.label_16)

        self.P1 = QLabel(Widget)
        self.P1.setObjectName(u"P1")

        self.horizontalLayout_15.addWidget(self.P1)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_25.addLayout(self.verticalLayout_5)

        self.line_2 = QFrame(Widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_19 = QLabel(Widget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_17.addWidget(self.label_19)

        self.Q2 = QLabel(Widget)
        self.Q2.setObjectName(u"Q2")

        self.horizontalLayout_17.addWidget(self.Q2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_21 = QLabel(Widget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_18.addWidget(self.label_21)

        self.P2 = QLabel(Widget)
        self.P2.setObjectName(u"P2")

        self.horizontalLayout_18.addWidget(self.P2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_25.addLayout(self.verticalLayout_6)

        self.line_3 = QFrame(Widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_23 = QLabel(Widget)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_19.addWidget(self.label_23)

        self.Q3 = QLabel(Widget)
        self.Q3.setObjectName(u"Q3")

        self.horizontalLayout_19.addWidget(self.Q3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_25 = QLabel(Widget)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_20.addWidget(self.label_25)

        self.P3 = QLabel(Widget)
        self.P3.setObjectName(u"P3")

        self.horizontalLayout_20.addWidget(self.P3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_25.addLayout(self.verticalLayout_7)

        self.line_4 = QFrame(Widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_4)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_27 = QLabel(Widget)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_21.addWidget(self.label_27)

        self.Q4 = QLabel(Widget)
        self.Q4.setObjectName(u"Q4")

        self.horizontalLayout_21.addWidget(self.Q4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_29 = QLabel(Widget)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_22.addWidget(self.label_29)

        self.P4 = QLabel(Widget)
        self.P4.setObjectName(u"P4")

        self.horizontalLayout_22.addWidget(self.P4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_22)


        self.horizontalLayout_25.addLayout(self.verticalLayout_8)

        self.line_5 = QFrame(Widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_31 = QLabel(Widget)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_23.addWidget(self.label_31)

        self.Q5 = QLabel(Widget)
        self.Q5.setObjectName(u"Q5")

        self.horizontalLayout_23.addWidget(self.Q5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_33 = QLabel(Widget)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_24.addWidget(self.label_33)

        self.P5 = QLabel(Widget)
        self.P5.setObjectName(u"P5")

        self.horizontalLayout_24.addWidget(self.P5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_25.addLayout(self.verticalLayout_9)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_25)

        self.line_6 = QFrame(Widget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_28.addWidget(self.line_6)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_35 = QLabel(Widget)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_26.addWidget(self.label_35)

        self.QTot = QLabel(Widget)
        self.QTot.setObjectName(u"QTot")

        self.horizontalLayout_26.addWidget(self.QTot)


        self.verticalLayout_10.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_37 = QLabel(Widget)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_27.addWidget(self.label_37)

        self.PTot = QLabel(Widget)
        self.PTot.setObjectName(u"PTot")

        self.horizontalLayout_27.addWidget(self.PTot)


        self.verticalLayout_10.addLayout(self.horizontalLayout_27)


        self.horizontalLayout_28.addLayout(self.verticalLayout_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_28)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)

        self.graphButton = QPushButton(Widget)
        self.graphButton.setObjectName(u"graphButton")

        self.verticalLayout_11.addWidget(self.graphButton)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Choix des donn\u00e9es :", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Fichier xlsb", None))
        self.browseButton.setText(QCoreApplication.translate("Widget", u"Parcourir", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Ligne", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u00e0", None))
        self.radioButton.setText(QCoreApplication.translate("Widget", u"Mode Manuel", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"D\u00e9bit Disponible", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Hauteur de chute", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Param\u00e8tres :", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"D\u00e9bit MaxTurbine 1", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"D\u00e9bit Max Turbine 4", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"D\u00e9bit Max Turbine 2", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"D\u00e9bit Max Turbine 5", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"D\u00e9bit Max Turbine 3", None))
        self.DynaButton.setText(QCoreApplication.translate("Widget", u"Optmiser par Programmation Dynamique", None))
        self.BBButton.setText(QCoreApplication.translate("Widget", u"Optimiser par boite noire (algorithme MADS)", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"R\u00e9sultats :", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"D\u00e9bit 1", None))
        self.Q1.setText(QCoreApplication.translate("Widget", u"000", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"PMW 1", None))
        self.P1.setText(QCoreApplication.translate("Widget", u"00.0", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"D\u00e9bit 2", None))
        self.Q2.setText(QCoreApplication.translate("Widget", u"000", None))
        self.label_21.setText(QCoreApplication.translate("Widget", u"PMW 2", None))
        self.P2.setText(QCoreApplication.translate("Widget", u"00.0", None))
        self.label_23.setText(QCoreApplication.translate("Widget", u"D\u00e9bit 3", None))
        self.Q3.setText(QCoreApplication.translate("Widget", u"000", None))
        self.label_25.setText(QCoreApplication.translate("Widget", u"PMW 3", None))
        self.P3.setText(QCoreApplication.translate("Widget", u"00.0", None))
        self.label_27.setText(QCoreApplication.translate("Widget", u"D\u00e9bit 4", None))
        self.Q4.setText(QCoreApplication.translate("Widget", u"000", None))
        self.label_29.setText(QCoreApplication.translate("Widget", u"PMW 4", None))
        self.P4.setText(QCoreApplication.translate("Widget", u"00.0", None))
        self.label_31.setText(QCoreApplication.translate("Widget", u"D\u00e9bit 5", None))
        self.Q5.setText(QCoreApplication.translate("Widget", u"000", None))
        self.label_33.setText(QCoreApplication.translate("Widget", u"PMW 5", None))
        self.P5.setText(QCoreApplication.translate("Widget", u"00.0", None))
        self.label_35.setText(QCoreApplication.translate("Widget", u"D\u00e9bit Total", None))
        self.QTot.setText(QCoreApplication.translate("Widget", u"000", None))
        self.label_37.setText(QCoreApplication.translate("Widget", u"PMW Total", None))
        self.PTot.setText(QCoreApplication.translate("Widget", u"000.0", None))
        self.graphButton.setText(QCoreApplication.translate("Widget", u"Afficher Graphique des d\u00e9bits turbin\u00e9s", None))
    # retranslateUi

