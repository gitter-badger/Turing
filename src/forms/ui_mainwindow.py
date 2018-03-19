# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/media/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_home = QtWidgets.QWidget()
        self.tab_home.setObjectName("tab_home")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_home)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/action/media/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_home, icon1, "")
        self.tab_pseudocode = QtWidgets.QWidget()
        self.tab_pseudocode.setObjectName("tab_pseudocode")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_pseudocode)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_pseudocode)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.header().setVisible(False)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.tabWidget.addTab(self.tab_pseudocode, "")
        self.tab_code = QtWidgets.QWidget()
        self.tab_code.setObjectName("tab_code")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_code)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget.addTab(self.tab_code, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRecent = QtWidgets.QMenu(self.menuFile)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/action/media/recent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRecent.setIcon(icon2)
        self.menuRecent.setObjectName("menuRecent")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuProgram = QtWidgets.QMenu(self.menubar)
        self.menuProgram.setObjectName("menuProgram")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuLanguage = QtWidgets.QMenu(self.menubar)
        self.menuLanguage.setObjectName("menuLanguage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dock_settings = QtWidgets.QDockWidget(MainWindow)
        self.dock_settings.setAccessibleName("")
        self.dock_settings.setFloating(False)
        self.dock_settings.setObjectName("dock_settings")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.dockWidgetContents_3)
        self.tabWidget_2.setDocumentMode(True)
        self.tabWidget_2.setMovable(True)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_6.addWidget(self.pushButton_2)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_7.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_7.addWidget(self.pushButton_4)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget_2)
        self.dock_settings.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_settings)
        self.dock_output = QtWidgets.QDockWidget(MainWindow)
        self.dock_output.setObjectName("dock_output")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.txtOutput = QtWidgets.QTextEdit(self.dockWidgetContents_4)
        self.txtOutput.setAcceptDrops(False)
        self.txtOutput.setUndoRedoEnabled(True)
        self.txtOutput.setReadOnly(True)
        self.txtOutput.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.txtOutput.setAcceptRichText(True)
        self.txtOutput.setObjectName("txtOutput")
        self.horizontalLayout_3.addWidget(self.txtOutput)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btnClearOutput = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.btnClearOutput.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/action/media/log_clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClearOutput.setIcon(icon3)
        self.btnClearOutput.setObjectName("btnClearOutput")
        self.verticalLayout_9.addWidget(self.btnClearOutput)
        self.btnSaveOutput = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.btnSaveOutput.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/action/media/log_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSaveOutput.setIcon(icon4)
        self.btnSaveOutput.setObjectName("btnSaveOutput")
        self.verticalLayout_9.addWidget(self.btnSaveOutput)
        self.btnPrintOutput = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.btnPrintOutput.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/action/media/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrintOutput.setIcon(icon5)
        self.btnPrintOutput.setObjectName("btnPrintOutput")
        self.verticalLayout_9.addWidget(self.btnPrintOutput)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtInput = QtWidgets.QLineEdit(self.dockWidgetContents_4)
        self.txtInput.setEnabled(False)
        self.txtInput.setReadOnly(False)
        self.txtInput.setObjectName("txtInput")
        self.horizontalLayout_2.addWidget(self.txtInput)
        self.btnSendInput = QtWidgets.QPushButton(self.dockWidgetContents_4)
        self.btnSendInput.setEnabled(False)
        self.btnSendInput.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/action/media/accept.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSendInput.setIcon(icon6)
        self.btnSendInput.setObjectName("btnSendInput")
        self.horizontalLayout_2.addWidget(self.btnSendInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.dock_output.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dock_output)
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/action/media/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon7)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/action/media/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon8)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/action/media/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon9)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/action/media/save_as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon10)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/action/media/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon11)
        self.actionExit.setObjectName("actionExit")
        self.actionSaveAll = QtWidgets.QAction(MainWindow)
        self.actionSaveAll.setObjectName("actionSaveAll")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/action/media/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon12)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/action/media/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon13)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/action/media/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon14)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/action/media/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon15)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/action/media/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon16)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/action/media/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon17)
        self.actionSettings.setObjectName("actionSettings")
        self.actionQuickStart = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/action/media/quick_start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuickStart.setIcon(icon18)
        self.actionQuickStart.setObjectName("actionQuickStart")
        self.actionHelpContents = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/action/media/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelpContents.setIcon(icon19)
        self.actionHelpContents.setObjectName("actionHelpContents")
        self.actionAboutTuring = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/action/media/icon_16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAboutTuring.setIcon(icon20)
        self.actionAboutTuring.setObjectName("actionAboutTuring")
        self.actionShowToolbar = QtWidgets.QAction(MainWindow)
        self.actionShowToolbar.setCheckable(True)
        self.actionShowToolbar.setChecked(True)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/action/media/toolbar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowToolbar.setIcon(icon21)
        self.actionShowToolbar.setObjectName("actionShowToolbar")
        self.actionExamples = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/action/media/examples.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExamples.setIcon(icon22)
        self.actionExamples.setObjectName("actionExamples")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setIcon(icon5)
        self.actionPrint.setObjectName("actionPrint")
        self.actionFind = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/action/media/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon23)
        self.actionFind.setObjectName("actionFind")
        self.actionReplace = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/action/media/replace.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReplace.setIcon(icon24)
        self.actionReplace.setObjectName("actionReplace")
        self.actionCalculator = QtWidgets.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/action/media/calculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCalculator.setIcon(icon25)
        self.actionCalculator.setObjectName("actionCalculator")
        self.actionClearRecent = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/action/media/recent_clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClearRecent.setIcon(icon26)
        self.actionClearRecent.setObjectName("actionClearRecent")
        self.actionSelectAll = QtWidgets.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/action/media/select_all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelectAll.setIcon(icon27)
        self.actionSelectAll.setObjectName("actionSelectAll")
        self.actionRun = QtWidgets.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/action/media/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon28)
        self.actionRun.setObjectName("actionRun")
        self.actionStep = QtWidgets.QAction(MainWindow)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/action/media/step.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStep.setIcon(icon29)
        self.actionStep.setObjectName("actionStep")
        self.actionShowToolbarText = QtWidgets.QAction(MainWindow)
        self.actionShowToolbarText.setCheckable(True)
        self.actionShowToolbarText.setChecked(True)
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap(":/action/media/toolbar_text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowToolbarText.setIcon(icon30)
        self.actionShowToolbarText.setObjectName("actionShowToolbarText")
        self.actionConvertToPython = QtWidgets.QAction(MainWindow)
        self.actionConvertToPython.setObjectName("actionConvertToPython")
        self.actionConvertToPseudocode = QtWidgets.QAction(MainWindow)
        self.actionConvertToPseudocode.setObjectName("actionConvertToPseudocode")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setCheckable(True)
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap(":/lang/media/lang/english.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEnglish.setIcon(icon31)
        self.actionEnglish.setText("English")
        self.actionEnglish.setStatusTip("en_US")
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionFrench = QtWidgets.QAction(MainWindow)
        self.actionFrench.setCheckable(True)
        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap(":/lang/media/lang/french.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFrench.setIcon(icon32)
        self.actionFrench.setText("Français")
        self.actionFrench.setStatusTip("fr_FR")
        self.actionFrench.setObjectName("actionFrench")
        self.actionDuplicateLine = QtWidgets.QAction(MainWindow)
        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap(":/action/media/duplicate_line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDuplicateLine.setIcon(icon33)
        self.actionDuplicateLine.setObjectName("actionDuplicateLine")
        self.actionIndent = QtWidgets.QAction(MainWindow)
        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap(":/action/media/indent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIndent.setIcon(icon34)
        self.actionIndent.setObjectName("actionIndent")
        self.actionUnindent = QtWidgets.QAction(MainWindow)
        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap(":/action/media/unindent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnindent.setIcon(icon35)
        self.actionUnindent.setObjectName("actionUnindent")
        self.actionGoToLine = QtWidgets.QAction(MainWindow)
        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap(":/action/media/go_to_line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoToLine.setIcon(icon36)
        self.actionGoToLine.setObjectName("actionGoToLine")
        self.actionFindPrevious = QtWidgets.QAction(MainWindow)
        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap(":/action/media/find_previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFindPrevious.setIcon(icon37)
        self.actionFindPrevious.setObjectName("actionFindPrevious")
        self.actionFindNext = QtWidgets.QAction(MainWindow)
        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap(":/action/media/find_next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFindNext.setIcon(icon38)
        self.actionFindNext.setObjectName("actionFindNext")
        self.menuRecent.addSeparator()
        self.menuRecent.addAction(self.actionClearRecent)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionSaveAll)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuRecent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelectAll)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFindPrevious)
        self.menuEdit.addAction(self.actionFindNext)
        self.menuEdit.addAction(self.actionReplace)
        self.menuEdit.addAction(self.actionGoToLine)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDuplicateLine)
        self.menuEdit.addAction(self.actionIndent)
        self.menuEdit.addAction(self.actionUnindent)
        self.menuSettings.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionQuickStart)
        self.menuHelp.addAction(self.actionHelpContents)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionExamples)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAboutTuring)
        self.menuView.addAction(self.actionShowToolbar)
        self.menuView.addAction(self.actionShowToolbarText)
        self.menuProgram.addAction(self.actionRun)
        self.menuProgram.addAction(self.actionStep)
        self.menuProgram.addSeparator()
        self.menuProgram.addAction(self.actionConvertToPython)
        self.menuProgram.addAction(self.actionConvertToPseudocode)
        self.menuTools.addAction(self.actionCalculator)
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionFrench)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuProgram.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuLanguage.menuAction())
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addAction(self.actionFind)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addAction(self.actionStep)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Turing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), _translate("MainWindow", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_pseudocode), _translate("MainWindow", "Pseudocode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_code), _translate("MainWindow", "Code"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.menuRecent.setTitle(_translate("MainWindow", "Recent files"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.menuSettings.setTitle(_translate("MainWindow", "&Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.menuView.setTitle(_translate("MainWindow", "&View"))
        self.menuProgram.setTitle(_translate("MainWindow", "&Program"))
        self.menuTools.setTitle(_translate("MainWindow", "&Tools"))
        self.menuLanguage.setTitle(_translate("MainWindow", "&Language"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Toolbar"))
        self.dock_settings.setWindowTitle(_translate("MainWindow", "Settings"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.dock_output.setWindowTitle(_translate("MainWindow", "Output"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionSaveAs.setToolTip(_translate("MainWindow", "Save As"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionClose.setToolTip(_translate("MainWindow", "Close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSaveAll.setText(_translate("MainWindow", "Save All"))
        self.actionSaveAll.setToolTip(_translate("MainWindow", "Save All"))
        self.actionSaveAll.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setToolTip(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setToolTip(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setToolTip(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setToolTip(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setToolTip(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionSettings.setToolTip(_translate("MainWindow", "Settings"))
        self.actionQuickStart.setText(_translate("MainWindow", "Quick Start"))
        self.actionQuickStart.setToolTip(_translate("MainWindow", "Quick Start"))
        self.actionHelpContents.setText(_translate("MainWindow", "Help Contents"))
        self.actionHelpContents.setToolTip(_translate("MainWindow", "Help Contents"))
        self.actionHelpContents.setShortcut(_translate("MainWindow", "F1"))
        self.actionAboutTuring.setText(_translate("MainWindow", "About Turing"))
        self.actionAboutTuring.setToolTip(_translate("MainWindow", "About Turing"))
        self.actionShowToolbar.setText(_translate("MainWindow", "Show toolbar"))
        self.actionShowToolbar.setToolTip(_translate("MainWindow", "Show toolbar"))
        self.actionExamples.setText(_translate("MainWindow", "Examples"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setToolTip(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionFind.setToolTip(_translate("MainWindow", "Find"))
        self.actionReplace.setText(_translate("MainWindow", "Replace"))
        self.actionReplace.setToolTip(_translate("MainWindow", "Replace"))
        self.actionCalculator.setText(_translate("MainWindow", "Calculator"))
        self.actionCalculator.setToolTip(_translate("MainWindow", "Calculator"))
        self.actionClearRecent.setText(_translate("MainWindow", "Clear"))
        self.actionClearRecent.setToolTip(_translate("MainWindow", "Clear"))
        self.actionSelectAll.setText(_translate("MainWindow", "Select All"))
        self.actionSelectAll.setToolTip(_translate("MainWindow", "Select All"))
        self.actionSelectAll.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionRun.setToolTip(_translate("MainWindow", "Run"))
        self.actionRun.setShortcut(_translate("MainWindow", "F5"))
        self.actionStep.setText(_translate("MainWindow", "Step-by-step"))
        self.actionStep.setToolTip(_translate("MainWindow", "Step-by-step"))
        self.actionStep.setShortcut(_translate("MainWindow", "F10"))
        self.actionShowToolbarText.setText(_translate("MainWindow", "Show toolbar text"))
        self.actionShowToolbarText.setToolTip(_translate("MainWindow", "Show toolbar text"))
        self.actionConvertToPython.setText(_translate("MainWindow", "Convert to Python"))
        self.actionConvertToPython.setToolTip(_translate("MainWindow", "Convert to Python"))
        self.actionConvertToPseudocode.setText(_translate("MainWindow", "Convert to pseudocode"))
        self.actionConvertToPseudocode.setToolTip(_translate("MainWindow", "Convert to pseudocode"))
        self.actionDuplicateLine.setText(_translate("MainWindow", "Duplicate Line"))
        self.actionDuplicateLine.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionIndent.setText(_translate("MainWindow", "Indent"))
        self.actionIndent.setShortcut(_translate("MainWindow", "Tab"))
        self.actionUnindent.setText(_translate("MainWindow", "Unindent"))
        self.actionUnindent.setShortcut(_translate("MainWindow", "Shift+Tab"))
        self.actionGoToLine.setText(_translate("MainWindow", "Go To Line"))
        self.actionGoToLine.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionFindPrevious.setText(_translate("MainWindow", "Find Previous"))
        self.actionFindPrevious.setShortcut(_translate("MainWindow", "Shift+F3"))
        self.actionFindNext.setText(_translate("MainWindow", "Find Next"))
        self.actionFindNext.setShortcut(_translate("MainWindow", "F3"))

import turing_rc