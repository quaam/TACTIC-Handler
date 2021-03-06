# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search/ui_search_options.ui'
#
# Created: Thu Apr 27 14:15:17 2017
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from lib.side.Qt import QtWidgets as QtGui
from lib.side.Qt import QtCore

class Ui_searchOptionsGroupBox(object):
    def setupUi(self, searchOptionsGroupBox):
        searchOptionsGroupBox.setObjectName("searchOptionsGroupBox")
        searchOptionsGroupBox.setMaximumSize(QtCore.QSize(16777215, 167))
        searchOptionsGroupBox.setFlat(True)
        self.verticalLayout = QtGui.QVBoxLayout(searchOptionsGroupBox)
        self.verticalLayout.setContentsMargins(4, 2, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchByGroupBox = QtGui.QGroupBox(searchOptionsGroupBox)
        self.searchByGroupBox.setFlat(True)
        self.searchByGroupBox.setObjectName("searchByGroupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.searchByGroupBox)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchNameRadioButton = QtGui.QRadioButton(self.searchByGroupBox)
        self.searchNameRadioButton.setChecked(True)
        self.searchNameRadioButton.setObjectName("searchNameRadioButton")
        self.horizontalLayout_2.addWidget(self.searchNameRadioButton)
        self.searchCodeRadioButton = QtGui.QRadioButton(self.searchByGroupBox)
        self.searchCodeRadioButton.setObjectName("searchCodeRadioButton")
        self.horizontalLayout_2.addWidget(self.searchCodeRadioButton)
        self.searchDescriptionRadioButton = QtGui.QRadioButton(self.searchByGroupBox)
        self.searchDescriptionRadioButton.setObjectName("searchDescriptionRadioButton")
        self.horizontalLayout_2.addWidget(self.searchDescriptionRadioButton)
        self.searchKeywordsRadioButton = QtGui.QRadioButton(self.searchByGroupBox)
        self.searchKeywordsRadioButton.setObjectName("searchKeywordsRadioButton")
        self.horizontalLayout_2.addWidget(self.searchKeywordsRadioButton)
        self.searchParentCodeRadioButton = QtGui.QRadioButton(self.searchByGroupBox)
        self.searchParentCodeRadioButton.setChecked(False)
        self.searchParentCodeRadioButton.setObjectName("searchParentCodeRadioButton")
        self.horizontalLayout_2.addWidget(self.searchParentCodeRadioButton)
        self.parentsComboBox = QtGui.QComboBox(self.searchByGroupBox)
        self.parentsComboBox.setEnabled(False)
        self.parentsComboBox.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.parentsComboBox.setObjectName("parentsComboBox")
        self.parentsComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.parentsComboBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.searchByGroupBox)
        self.sortByGroupBox = QtGui.QGroupBox(searchOptionsGroupBox)
        self.sortByGroupBox.setFlat(True)
        self.sortByGroupBox.setObjectName("sortByGroupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.sortByGroupBox)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sortNameRadioButton = QtGui.QRadioButton(self.sortByGroupBox)
        self.sortNameRadioButton.setObjectName("sortNameRadioButton")
        self.horizontalLayout.addWidget(self.sortNameRadioButton)
        self.sortCodeRadioButton = QtGui.QRadioButton(self.sortByGroupBox)
        self.sortCodeRadioButton.setObjectName("sortCodeRadioButton")
        self.horizontalLayout.addWidget(self.sortCodeRadioButton)
        self.sortTimestampRadioButton = QtGui.QRadioButton(self.sortByGroupBox)
        self.sortTimestampRadioButton.setChecked(True)
        self.sortTimestampRadioButton.setObjectName("sortTimestampRadioButton")
        self.horizontalLayout.addWidget(self.sortTimestampRadioButton)
        self.sortNothingRadioButton = QtGui.QRadioButton(self.sortByGroupBox)
        self.sortNothingRadioButton.setObjectName("sortNothingRadioButton")
        self.horizontalLayout.addWidget(self.sortNothingRadioButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.sortByGroupBox)
        self.miscGroupBox = QtGui.QGroupBox(searchOptionsGroupBox)
        self.miscGroupBox.setFlat(True)
        self.miscGroupBox.setObjectName("miscGroupBox")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.miscGroupBox)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.saveAsDefaultsPushButton = QtGui.QPushButton(self.miscGroupBox)
        self.saveAsDefaultsPushButton.setObjectName("saveAsDefaultsPushButton")
        self.horizontalLayout_3.addWidget(self.saveAsDefaultsPushButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label = QtGui.QLabel(self.miscGroupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.displayLimitSpinBox = QtGui.QSpinBox(self.miscGroupBox)
        self.displayLimitSpinBox.setMinimum(5)
        self.displayLimitSpinBox.setMaximum(200)
        self.displayLimitSpinBox.setSingleStep(5)
        self.displayLimitSpinBox.setObjectName("displayLimitSpinBox")
        self.horizontalLayout_3.addWidget(self.displayLimitSpinBox)
        self.showAllProcessCheckBox = QtGui.QCheckBox(self.miscGroupBox)
        self.showAllProcessCheckBox.setChecked(True)
        self.showAllProcessCheckBox.setObjectName("showAllProcessCheckBox")
        self.horizontalLayout_3.addWidget(self.showAllProcessCheckBox)
        self.verticalLayout.addWidget(self.miscGroupBox)

        self.retranslateUi(searchOptionsGroupBox)
        QtCore.QObject.connect(self.searchParentCodeRadioButton, QtCore.SIGNAL("toggled(bool)"), self.parentsComboBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(searchOptionsGroupBox)
        searchOptionsGroupBox.setTabOrder(self.searchNameRadioButton, self.searchCodeRadioButton)
        searchOptionsGroupBox.setTabOrder(self.searchCodeRadioButton, self.searchDescriptionRadioButton)
        searchOptionsGroupBox.setTabOrder(self.searchDescriptionRadioButton, self.searchKeywordsRadioButton)
        searchOptionsGroupBox.setTabOrder(self.searchKeywordsRadioButton, self.sortNameRadioButton)
        searchOptionsGroupBox.setTabOrder(self.sortNameRadioButton, self.sortCodeRadioButton)
        searchOptionsGroupBox.setTabOrder(self.sortCodeRadioButton, self.sortTimestampRadioButton)
        searchOptionsGroupBox.setTabOrder(self.sortTimestampRadioButton, self.sortNothingRadioButton)
        searchOptionsGroupBox.setTabOrder(self.sortNothingRadioButton, self.showAllProcessCheckBox)
        searchOptionsGroupBox.setTabOrder(self.showAllProcessCheckBox, self.displayLimitSpinBox)
        searchOptionsGroupBox.setTabOrder(self.displayLimitSpinBox, self.saveAsDefaultsPushButton)

    def retranslateUi(self, searchOptionsGroupBox):
        searchOptionsGroupBox.setWindowTitle(QtGui.QApplication.translate("searchOptionsGroupBox", "GroupBox", None))
        searchOptionsGroupBox.setTitle(QtGui.QApplication.translate("searchOptionsGroupBox", "Options:", None))
        self.searchByGroupBox.setTitle(QtGui.QApplication.translate("searchOptionsGroupBox", "Search by:", None))
        self.searchNameRadioButton.setText(QtGui.QApplication.translate("searchOptionsGroupBox", "Name", None))
        self.searchCodeRadioButton.setText(QtGui.QApplication.translate("searchOptionsGroupBox", "Search Code", None))
        self.searchDescriptionRadioButton.setText(QtGui.QApplication.translate("searchOptionsGroupBox", "Description", None))
        self.searchKeywordsRadioButton.setText(QtGui.QApplication.translate("searchOptionsGroupBox", "Keywords", None))
        self.searchParentCodeRadioButton.setText(QtGui.QApplication.translate("searchOptionsGroupBox", "Parent Code:", None))
        self.parentsComboBox.setItemText(0, QtGui.QApplication.translate("searchOptionsGroupBox", "All", None))
        self.sortByGroupBox.setTitle(QtGui.QApplication.translate("searchOptionsGroupBox", "Sort by:", None))
        self.sortNameRadioButton.setText(QtGui.QApplication.translate("searchOptionsGroupBox", "Name", None))
        self.sortCodeRadioButton.setText(QtGui.QApplication.translate("searchOptionsGroupBox", "Search Code", None))
        self.sortTimestampRadioButton.setText(QtGui.QApplication.translate("searchOptionsGroupBox", "Timestamp", None))
        self.sortNothingRadioButton.setText(QtGui.QApplication.translate("searchOptionsGroupBox", "Nothing", None))
        self.miscGroupBox.setTitle(QtGui.QApplication.translate("searchOptionsGroupBox", "Misc:", None))
        self.saveAsDefaultsPushButton.setText(QtGui.QApplication.translate("searchOptionsGroupBox", "Apply to All Tabs", None))
        self.label.setText(QtGui.QApplication.translate("searchOptionsGroupBox", "Search results limit:", None))
        self.showAllProcessCheckBox.setText(QtGui.QApplication.translate("searchOptionsGroupBox", "Show hidden Processes", None))

