# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(935, 690)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget_chara_list = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_chara_list.setObjectName("listWidget_chara_list")
        self.verticalLayout_2.addWidget(self.listWidget_chara_list)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_ve_save_path = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_ve_save_path.setObjectName("lineEdit_ve_save_path")
        self.gridLayout_3.addWidget(self.lineEdit_ve_save_path, 0, 1, 1, 1)
        self.pushButton_ve_select_save_path = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_ve_select_save_path.setObjectName("pushButton_ve_select_save_path")
        self.gridLayout_3.addWidget(self.pushButton_ve_select_save_path, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEdit_ve_proxy = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_ve_proxy.setObjectName("lineEdit_ve_proxy")
        self.gridLayout_3.addWidget(self.lineEdit_ve_proxy, 1, 1, 1, 1)
        self.checkBox_ve_use_proxy = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_ve_use_proxy.setObjectName("checkBox_ve_use_proxy")
        self.gridLayout_3.addWidget(self.checkBox_ve_use_proxy, 1, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.lineEdit_ve_rate = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_ve_rate.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_ve_rate.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lineEdit_ve_rate.setObjectName("lineEdit_ve_rate")
        self.horizontalLayout.addWidget(self.lineEdit_ve_rate)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.lineEdit_ve_bits = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_ve_bits.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lineEdit_ve_bits.setObjectName("lineEdit_ve_bits")
        self.horizontalLayout.addWidget(self.lineEdit_ve_bits)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.lineEdit_ve_channels = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_ve_channels.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lineEdit_ve_channels.setObjectName("lineEdit_ve_channels")
        self.horizontalLayout.addWidget(self.lineEdit_ve_channels)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.checkBox_get_voice_from_all = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_get_voice_from_all.setChecked(True)
        self.checkBox_get_voice_from_all.setObjectName("checkBox_get_voice_from_all")
        self.verticalLayout_5.addWidget(self.checkBox_get_voice_from_all)
        self.checkBox_ve_download_missing = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_ve_download_missing.setChecked(True)
        self.checkBox_ve_download_missing.setObjectName("checkBox_ve_download_missing")
        self.verticalLayout_5.addWidget(self.checkBox_ve_download_missing)
        self.checkBox_ve_usecache = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_ve_usecache.setChecked(True)
        self.checkBox_ve_usecache.setObjectName("checkBox_ve_usecache")
        self.verticalLayout_5.addWidget(self.checkBox_ve_usecache)
        self.tabWidget_4 = QtWidgets.QTabWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_4.sizePolicy().hasHeightForWidth())
        self.tabWidget_4.setSizePolicy(sizePolicy)
        self.tabWidget_4.setMaximumSize(QtCore.QSize(16777215, 10000))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.tab_12)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_ve_single_id = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit_ve_single_id.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_ve_single_id.setObjectName("lineEdit_ve_single_id")
        self.gridLayout_2.addWidget(self.lineEdit_ve_single_id, 0, 1, 1, 1)
        self.pushButton_single_start = QtWidgets.QPushButton(self.tab_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_single_start.sizePolicy().hasHeightForWidth())
        self.pushButton_single_start.setSizePolicy(sizePolicy)
        self.pushButton_single_start.setMinimumSize(QtCore.QSize(0, 100))
        self.pushButton_single_start.setObjectName("pushButton_single_start")
        self.gridLayout_2.addWidget(self.pushButton_single_start, 1, 0, 1, 2)
        self.tabWidget_4.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_13)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget_ve_extarct = QtWidgets.QTableWidget(self.tab_13)
        self.tableWidget_ve_extarct.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_ve_extarct.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_ve_extarct.setObjectName("tableWidget_ve_extarct")
        self.tableWidget_ve_extarct.setColumnCount(2)
        self.tableWidget_ve_extarct.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ve_extarct.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ve_extarct.setHorizontalHeaderItem(1, item)
        self.tableWidget_ve_extarct.horizontalHeader().setVisible(False)
        self.tableWidget_ve_extarct.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ve_extarct.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_ve_extarct.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_ve_extarct.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ve_extarct.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.tableWidget_ve_extarct)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_rm_selecting = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_rm_selecting.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_rm_selecting.setObjectName("pushButton_rm_selecting")
        self.verticalLayout_6.addWidget(self.pushButton_rm_selecting)
        self.pushButton_multi_start = QtWidgets.QPushButton(self.tab_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_multi_start.sizePolicy().hasHeightForWidth())
        self.pushButton_multi_start.setSizePolicy(sizePolicy)
        self.pushButton_multi_start.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_multi_start.setObjectName("pushButton_multi_start")
        self.verticalLayout_6.addWidget(self.pushButton_multi_start)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.tabWidget_4.addTab(self.tab_13, "")
        self.verticalLayout_5.addWidget(self.tabWidget_4)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.listWidget_music_list = QtWidgets.QListWidget(self.groupBox_5)
        self.listWidget_music_list.setObjectName("listWidget_music_list")
        self.verticalLayout_7.addWidget(self.listWidget_music_list)
        self.horizontalLayout_8.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.listWidget_singing_chara_list = QtWidgets.QListWidget(self.groupBox_6)
        self.listWidget_singing_chara_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_singing_chara_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_singing_chara_list.setObjectName("listWidget_singing_chara_list")
        self.verticalLayout_8.addWidget(self.listWidget_singing_chara_list)
        self.horizontalLayout_8.addWidget(self.groupBox_6)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_me_select_save_path = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_me_select_save_path.setObjectName("pushButton_me_select_save_path")
        self.gridLayout_4.addWidget(self.pushButton_me_select_save_path, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit_me_save_path = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_me_save_path.setObjectName("lineEdit_me_save_path")
        self.gridLayout_4.addWidget(self.lineEdit_me_save_path, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)
        self.lineEdit_me_proxy = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_me_proxy.setObjectName("lineEdit_me_proxy")
        self.gridLayout_4.addWidget(self.lineEdit_me_proxy, 1, 1, 1, 1)
        self.checkBox_me_proxy = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_me_proxy.setObjectName("checkBox_me_proxy")
        self.gridLayout_4.addWidget(self.checkBox_me_proxy, 1, 2, 1, 1)
        self.verticalLayout_20.addLayout(self.gridLayout_4)
        self.checkBox_me_download_missing = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_me_download_missing.setChecked(True)
        self.checkBox_me_download_missing.setObjectName("checkBox_me_download_missing")
        self.verticalLayout_20.addWidget(self.checkBox_me_download_missing)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.lineEdit_music_id = QtWidgets.QLineEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_music_id.sizePolicy().hasHeightForWidth())
        self.lineEdit_music_id.setSizePolicy(sizePolicy)
        self.lineEdit_music_id.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_music_id.setObjectName("lineEdit_music_id")
        self.horizontalLayout_9.addWidget(self.lineEdit_music_id)
        self.verticalLayout_20.addLayout(self.horizontalLayout_9)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.lineEdit_chara_id = QtWidgets.QLineEdit(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_chara_id.sizePolicy().hasHeightForWidth())
        self.lineEdit_chara_id.setSizePolicy(sizePolicy)
        self.lineEdit_chara_id.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_chara_id.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_chara_id.setObjectName("lineEdit_chara_id")
        self.horizontalLayout_6.addWidget(self.lineEdit_chara_id)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_9.setContentsMargins(-1, -1, 11, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        self.lineEdit_me_rate = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_me_rate.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_me_rate.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lineEdit_me_rate.setObjectName("lineEdit_me_rate")
        self.gridLayout.addWidget(self.lineEdit_me_rate, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 2, 1, 1)
        self.lineEdit_me_bits = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_me_bits.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lineEdit_me_bits.setObjectName("lineEdit_me_bits")
        self.gridLayout.addWidget(self.lineEdit_me_bits, 0, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)
        self.lineEdit_me_channels = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_me_channels.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lineEdit_me_channels.setObjectName("lineEdit_me_channels")
        self.gridLayout.addWidget(self.lineEdit_me_channels, 1, 1, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox_4)
        self.pushButton_extract_bgm = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_extract_bgm.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_extract_bgm.setObjectName("pushButton_extract_bgm")
        self.verticalLayout_9.addWidget(self.pushButton_extract_bgm)
        self.pushButton_extract_chara_sound = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_extract_chara_sound.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_extract_chara_sound.setObjectName("pushButton_extract_chara_sound")
        self.verticalLayout_9.addWidget(self.pushButton_extract_chara_sound)
        self.pushButton_extract_sound_by_lrc = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_extract_sound_by_lrc.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_extract_sound_by_lrc.setObjectName("pushButton_extract_sound_by_lrc")
        self.verticalLayout_9.addWidget(self.pushButton_extract_sound_by_lrc)
        self.checkBox_remove_silence = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_remove_silence.setChecked(True)
        self.checkBox_remove_silence.setObjectName("checkBox_remove_silence")
        self.verticalLayout_9.addWidget(self.checkBox_remove_silence)
        self.verticalLayout_10.addWidget(self.groupBox_7)
        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 2)
        self.verticalLayout_11.addLayout(self.verticalLayout_10)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_8.setMaximumSize(QtCore.QSize(16777215, 400))
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.label_singing_count = QtWidgets.QLabel(self.groupBox_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_singing_count.sizePolicy().hasHeightForWidth())
        self.label_singing_count.setSizePolicy(sizePolicy)
        self.label_singing_count.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_singing_count.setObjectName("label_singing_count")
        self.horizontalLayout_7.addWidget(self.label_singing_count)
        self.verticalLayout_25.addLayout(self.horizontalLayout_7)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.tabWidget_parts = QtWidgets.QTabWidget(self.groupBox_8)
        self.tabWidget_parts.setMaximumSize(QtCore.QSize(16777215, 10000))
        self.tabWidget_parts.setObjectName("tabWidget_parts")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.listWidget_mx_1 = QtWidgets.QListWidget(self.tab_5)
        self.listWidget_mx_1.setObjectName("listWidget_mx_1")
        self.verticalLayout_12.addWidget(self.listWidget_mx_1)
        self.tabWidget_parts.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab_6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.listWidget_mx_2 = QtWidgets.QListWidget(self.tab_6)
        self.listWidget_mx_2.setObjectName("listWidget_mx_2")
        self.verticalLayout_13.addWidget(self.listWidget_mx_2)
        self.tabWidget_parts.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.listWidget_mx_3 = QtWidgets.QListWidget(self.tab_7)
        self.listWidget_mx_3.setObjectName("listWidget_mx_3")
        self.verticalLayout_14.addWidget(self.listWidget_mx_3)
        self.tabWidget_parts.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.tab_8)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.listWidget_mx_4 = QtWidgets.QListWidget(self.tab_8)
        self.listWidget_mx_4.setObjectName("listWidget_mx_4")
        self.verticalLayout_15.addWidget(self.listWidget_mx_4)
        self.tabWidget_parts.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tab_9)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.listWidget_mx_5 = QtWidgets.QListWidget(self.tab_9)
        self.listWidget_mx_5.setObjectName("listWidget_mx_5")
        self.verticalLayout_16.addWidget(self.listWidget_mx_5)
        self.tabWidget_parts.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.tab_10)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.listWidget_mx_6 = QtWidgets.QListWidget(self.tab_10)
        self.listWidget_mx_6.setObjectName("listWidget_mx_6")
        self.verticalLayout_17.addWidget(self.listWidget_mx_6)
        self.tabWidget_parts.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.tab_11)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.listWidget_mx_7 = QtWidgets.QListWidget(self.tab_11)
        self.listWidget_mx_7.setObjectName("listWidget_mx_7")
        self.verticalLayout_18.addWidget(self.listWidget_mx_7)
        self.tabWidget_parts.addTab(self.tab_11, "")
        self.verticalLayout_23.addWidget(self.tabWidget_parts)
        self.verticalLayout_25.addLayout(self.verticalLayout_23)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_me_delete_select = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_me_delete_select.setObjectName("pushButton_me_delete_select")
        self.horizontalLayout_10.addWidget(self.pushButton_me_delete_select)
        self.pushButton_me_clear = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_me_clear.setObjectName("pushButton_me_clear")
        self.horizontalLayout_10.addWidget(self.pushButton_me_clear)
        self.verticalLayout_25.addLayout(self.horizontalLayout_10)
        self.verticalLayout_19.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_15 = QtWidgets.QLabel(self.groupBox_9)
        self.label_15.setObjectName("label_15")
        self.gridLayout_5.addWidget(self.label_15, 1, 0, 1, 1)
        self.lineEdit_chara_vol = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_chara_vol.setObjectName("lineEdit_chara_vol")
        self.gridLayout_5.addWidget(self.lineEdit_chara_vol, 1, 1, 1, 1)
        self.pushButton_start_mix = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_start_mix.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_start_mix.setMaximumSize(QtCore.QSize(16777215, 80))
        self.pushButton_start_mix.setObjectName("pushButton_start_mix")
        self.gridLayout_5.addWidget(self.pushButton_start_mix, 2, 0, 1, 2)
        self.checkBox_all_singing = QtWidgets.QCheckBox(self.groupBox_9)
        self.checkBox_all_singing.setObjectName("checkBox_all_singing")
        self.gridLayout_5.addWidget(self.checkBox_all_singing, 0, 0, 1, 2)
        self.verticalLayout_19.addWidget(self.groupBox_9)
        self.verticalLayout_24.addLayout(self.verticalLayout_19)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.verticalLayout_20.addWidget(self.tabWidget_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_20)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_parts.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Umamusume Voice Text Extractor"))
        self.groupBox.setTitle(_translate("MainWindow", "Character List"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Config"))
        self.lineEdit_ve_save_path.setText(_translate("MainWindow", "./save"))
        self.pushButton_ve_select_save_path.setText(_translate("MainWindow", "select"))
        self.label.setText(_translate("MainWindow", "Save path"))
        self.label_7.setText(_translate("MainWindow", "Proxy"))
        self.lineEdit_ve_proxy.setPlaceholderText(_translate("MainWindow", "eg. http://127.0.0.1:10087"))
        self.checkBox_ve_use_proxy.setText(_translate("MainWindow", "Use Proxy"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Wave Format"))
        self.label_9.setText(_translate("MainWindow", "Rate: "))
        self.lineEdit_ve_rate.setText(_translate("MainWindow", "22050"))
        self.label_10.setText(_translate("MainWindow", "Bits: "))
        self.lineEdit_ve_bits.setText(_translate("MainWindow", "16"))
        self.label_11.setText(_translate("MainWindow", "Channels: "))
        self.lineEdit_ve_channels.setText(_translate("MainWindow", "1"))
        self.checkBox_get_voice_from_all.setText(_translate("MainWindow", "Get voice from all stories"))
        self.checkBox_ve_download_missing.setText(_translate("MainWindow", "Download missing voice files"))
        self.checkBox_ve_usecache.setText(_translate("MainWindow", "Use cache"))
        self.label_5.setText(_translate("MainWindow", "Character ID"))
        self.pushButton_single_start.setText(_translate("MainWindow", "Start"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_12), _translate("MainWindow", "Single Character Mode"))
        item = self.tableWidget_ve_extarct.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CharaID"))
        item = self.tableWidget_ve_extarct.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "SaveID"))
        self.pushButton_rm_selecting.setText(_translate("MainWindow", "Remove Selecting"))
        self.pushButton_multi_start.setText(_translate("MainWindow", "Start"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_13), _translate("MainWindow", "Multi Character Mode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Voice Extractor"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Music List"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Singing Character List"))
        self.pushButton_me_select_save_path.setText(_translate("MainWindow", "select"))
        self.label_6.setText(_translate("MainWindow", "Save path"))
        self.lineEdit_me_save_path.setText(_translate("MainWindow", "./save"))
        self.label_8.setText(_translate("MainWindow", "Proxy"))
        self.lineEdit_me_proxy.setPlaceholderText(_translate("MainWindow", "eg. http://127.0.0.1:10087"))
        self.checkBox_me_proxy.setText(_translate("MainWindow", "Use Proxy"))
        self.checkBox_me_download_missing.setText(_translate("MainWindow", "Download missing files"))
        self.label_2.setText(_translate("MainWindow", "Music ID"))
        self.label_3.setText(_translate("MainWindow", "Chara ID"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Wave Format"))
        self.label_12.setText(_translate("MainWindow", "Rate: "))
        self.lineEdit_me_rate.setText(_translate("MainWindow", "48000"))
        self.label_13.setText(_translate("MainWindow", "Bits: "))
        self.lineEdit_me_bits.setText(_translate("MainWindow", "16"))
        self.label_14.setText(_translate("MainWindow", "Channels: "))
        self.lineEdit_me_channels.setText(_translate("MainWindow", "2"))
        self.pushButton_extract_bgm.setText(_translate("MainWindow", "Extract BGM"))
        self.pushButton_extract_chara_sound.setText(_translate("MainWindow", "Extract Full Chara Sound"))
        self.pushButton_extract_sound_by_lrc.setText(_translate("MainWindow", "Extract Chara Sound By Lrc"))
        self.checkBox_remove_silence.setText(_translate("MainWindow", "Remove Silence Part"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Extractor"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Position Sets"))
        self.label_4.setText(_translate("MainWindow", "Singing Pos Count:"))
        self.label_singing_count.setText(_translate("MainWindow", "0"))
        self.tabWidget_parts.setTabText(self.tabWidget_parts.indexOf(self.tab_5), _translate("MainWindow", "1"))
        self.tabWidget_parts.setTabText(self.tabWidget_parts.indexOf(self.tab_6), _translate("MainWindow", "2"))
        self.tabWidget_parts.setTabText(self.tabWidget_parts.indexOf(self.tab_7), _translate("MainWindow", "3"))
        self.tabWidget_parts.setTabText(self.tabWidget_parts.indexOf(self.tab_8), _translate("MainWindow", "4"))
        self.tabWidget_parts.setTabText(self.tabWidget_parts.indexOf(self.tab_9), _translate("MainWindow", "5"))
        self.tabWidget_parts.setTabText(self.tabWidget_parts.indexOf(self.tab_10), _translate("MainWindow", "6"))
        self.tabWidget_parts.setTabText(self.tabWidget_parts.indexOf(self.tab_11), _translate("MainWindow", "7"))
        self.pushButton_me_delete_select.setText(_translate("MainWindow", "Remove Selecting"))
        self.pushButton_me_clear.setText(_translate("MainWindow", "Clear"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Mix Config"))
        self.label_15.setText(_translate("MainWindow", "Character Volume"))
        self.lineEdit_chara_vol.setText(_translate("MainWindow", "0.85"))
        self.pushButton_start_mix.setText(_translate("MainWindow", "Start Mix"))
        self.checkBox_all_singing.setText(_translate("MainWindow", "Force All Singing"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Mixer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Live Music Extractor"))
from . import msrc_rc
