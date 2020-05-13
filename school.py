# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'school.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1003, 625)
        Form.setStyleSheet("#Form{\n"
"background-image:url(C:/Users/Python/Desktop/scl/bg5.jpg);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("QFrame{\n"
"background-color:rgba(0,0,0,.5);\n"
"}\n"
"\n"
"QTabWidget{\n"
"background-color:red;\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.Teachers = QtWidgets.QWidget()
        self.Teachers.setObjectName("Teachers")
        self.label = QtWidgets.QLabel(self.Teachers)
        self.label.setGeometry(QtCore.QRect(340, 20, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"border:none;\n"
"border-bottom:1px solid black;\n"
"color:white;\n"
"}")
        self.label.setObjectName("label")
        self.studenfirstnamelabel = QtWidgets.QLabel(self.Teachers)
        self.studenfirstnamelabel.setGeometry(QtCore.QRect(20, 90, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.studenfirstnamelabel.setFont(font)
        self.studenfirstnamelabel.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.studenfirstnamelabel.setObjectName("studenfirstnamelabel")
        self.studenlastnamelabel = QtWidgets.QLabel(self.Teachers)
        self.studenlastnamelabel.setGeometry(QtCore.QRect(20, 150, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.studenlastnamelabel.setFont(font)
        self.studenlastnamelabel.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.studenlastnamelabel.setObjectName("studenlastnamelabel")
        self.Dobla = QtWidgets.QLabel(self.Teachers)
        self.Dobla.setGeometry(QtCore.QRect(20, 200, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Dobla.setFont(font)
        self.Dobla.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.Dobla.setObjectName("Dobla")
        self.label_5 = QtWidgets.QLabel(self.Teachers)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Teachers)
        self.label_6.setGeometry(QtCore.QRect(10, 310, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.stu_fatherN_label = QtWidgets.QLabel(self.Teachers)
        self.stu_fatherN_label.setGeometry(QtCore.QRect(500, 100, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stu_fatherN_label.setFont(font)
        self.stu_fatherN_label.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.stu_fatherN_label.setObjectName("stu_fatherN_label")
        self.stu_motherN_label = QtWidgets.QLabel(self.Teachers)
        self.stu_motherN_label.setGeometry(QtCore.QRect(500, 160, 130, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stu_motherN_label.setFont(font)
        self.stu_motherN_label.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.stu_motherN_label.setObjectName("stu_motherN_label")
        self.stu_father_occ_label = QtWidgets.QLabel(self.Teachers)
        self.stu_father_occ_label.setGeometry(QtCore.QRect(490, 210, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stu_father_occ_label.setFont(font)
        self.stu_father_occ_label.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.stu_father_occ_label.setObjectName("stu_father_occ_label")
        self.stu_mother_occ_labe = QtWidgets.QLabel(self.Teachers)
        self.stu_mother_occ_labe.setGeometry(QtCore.QRect(490, 270, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stu_mother_occ_labe.setFont(font)
        self.stu_mother_occ_labe.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.stu_mother_occ_labe.setObjectName("stu_mother_occ_labe")
        self.stufirstnametext = QtWidgets.QLineEdit(self.Teachers)
        self.stufirstnametext.setGeometry(QtCore.QRect(140, 100, 190, 22))
        self.stufirstnametext.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.stufirstnametext.setObjectName("stufirstnametext")
        self.stulastnametext = QtWidgets.QLineEdit(self.Teachers)
        self.stulastnametext.setGeometry(QtCore.QRect(140, 160, 190, 22))
        self.stulastnametext.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.stulastnametext.setObjectName("stulastnametext")
        self.stuidtext = QtWidgets.QLineEdit(self.Teachers)
        self.stuidtext.setGeometry(QtCore.QRect(140, 255, 190, 22))
        self.stuidtext.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.stuidtext.setObjectName("stuidtext")
        self.stuplaceofbirthtext = QtWidgets.QLineEdit(self.Teachers)
        self.stuplaceofbirthtext.setGeometry(QtCore.QRect(140, 315, 190, 22))
        self.stuplaceofbirthtext.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.stuplaceofbirthtext.setObjectName("stuplaceofbirthtext")
        self.stu_nationnality_text = QtWidgets.QLineEdit(self.Teachers)
        self.stu_nationnality_text.setGeometry(QtCore.QRect(130, 440, 190, 22))
        self.stu_nationnality_text.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.stu_nationnality_text.setObjectName("stu_nationnality_text")
        self.stu_fatherN_text = QtWidgets.QLineEdit(self.Teachers)
        self.stu_fatherN_text.setGeometry(QtCore.QRect(680, 110, 190, 22))
        self.stu_fatherN_text.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.stu_fatherN_text.setObjectName("stu_fatherN_text")
        self.stu_motherN_text = QtWidgets.QLineEdit(self.Teachers)
        self.stu_motherN_text.setGeometry(QtCore.QRect(680, 160, 190, 22))
        self.stu_motherN_text.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.stu_motherN_text.setObjectName("stu_motherN_text")
        self.stu_father_occ_text = QtWidgets.QLineEdit(self.Teachers)
        self.stu_father_occ_text.setGeometry(QtCore.QRect(680, 220, 190, 22))
        self.stu_father_occ_text.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.stu_father_occ_text.setObjectName("stu_father_occ_text")
        self.stu_mother_occ_text = QtWidgets.QLineEdit(self.Teachers)
        self.stu_mother_occ_text.setGeometry(QtCore.QRect(680, 280, 190, 22))
        self.stu_mother_occ_text.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.stu_mother_occ_text.setObjectName("stu_mother_occ_text")
        self.label_12 = QtWidgets.QLabel(self.Teachers)
        self.label_12.setGeometry(QtCore.QRect(10, 380, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Teachers)
        self.label_13.setGeometry(QtCore.QRect(10, 440, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_13.setObjectName("label_13")
        self.frame_3 = QtWidgets.QFrame(self.Teachers)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 880, 10))
        self.frame_3.setStyleSheet("QFrame{\n"
"background-color:red;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_5 = QtWidgets.QFrame(self.Teachers)
        self.frame_5.setGeometry(QtCore.QRect(410, 70, 10, 420))
        self.frame_5.setStyleSheet("QFrame{\n"
"background-color:#ff9100;\n"
"border-radius:20px;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.stu_father_sal_label = QtWidgets.QLabel(self.Teachers)
        self.stu_father_sal_label.setGeometry(QtCore.QRect(490, 330, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stu_father_sal_label.setFont(font)
        self.stu_father_sal_label.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.stu_father_sal_label.setObjectName("stu_father_sal_label")
        self.stu_father_sal_text = QtWidgets.QLineEdit(self.Teachers)
        self.stu_father_sal_text.setGeometry(QtCore.QRect(680, 335, 190, 22))
        self.stu_father_sal_text.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.stu_father_sal_text.setObjectName("stu_father_sal_text")
        self.stu_mother_sal_text = QtWidgets.QLineEdit(self.Teachers)
        self.stu_mother_sal_text.setGeometry(QtCore.QRect(680, 400, 190, 22))
        self.stu_mother_sal_text.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.stu_mother_sal_text.setText("")
        self.stu_mother_sal_text.setObjectName("stu_mother_sal_text")
        self.label_28 = QtWidgets.QLabel(self.Teachers)
        self.label_28.setGeometry(QtCore.QRect(480, 395, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_28.setObjectName("label_28")
        self.stugendertext = QtWidgets.QComboBox(self.Teachers)
        self.stugendertext.setGeometry(QtCore.QRect(150, 380, 74, 22))
        self.stugendertext.setObjectName("stugendertext")
        self.stugendertext.addItem("")
        self.stugendertext.setItemText(0, "")
        self.stugendertext.addItem("")
        self.stugendertext.addItem("")
        self.stugendertext.addItem("")
        self.DOBtext = QtWidgets.QDateEdit(self.Teachers)
        self.DOBtext.setGeometry(QtCore.QRect(140, 205, 110, 22))
        self.DOBtext.setObjectName("DOBtext")
        self.pushButtonstu = QtWidgets.QPushButton(self.Teachers)
        self.pushButtonstu.setGeometry(QtCore.QRect(370, 510, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButtonstu.setFont(font)
        self.pushButtonstu.setStyleSheet("QPushButton{color: #fff !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #ed3330;\n"
"padding: 20px;\n"
"border-radius: 5px;\n"
"display: inline-block;\n"
"border: none;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #434343;\n"
"letter-spacing: 1px;\n"
"box-shadow: 5px 40px -10px rgba(0,0,0,0.57);\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButtonstu.setObjectName("pushButtonstu")
        self.tabWidget.addTab(self.Teachers, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_12.setGeometry(QtCore.QRect(130, 100, 190, 22))
        self.lineEdit_12.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(10, 140, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(10, 90, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_14.setObjectName("label_14")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_14.setGeometry(QtCore.QRect(130, 40, 190, 22))
        self.lineEdit_14.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setGeometry(QtCore.QRect(10, 30, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_16.setObjectName("label_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_17.setGeometry(QtCore.QRect(130, 380, 190, 22))
        self.lineEdit_17.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setGeometry(QtCore.QRect(10, 310, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setGeometry(QtCore.QRect(10, 370, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setGeometry(QtCore.QRect(10, 200, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_19.setObjectName("label_19")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_18.setGeometry(QtCore.QRect(130, 210, 190, 22))
        self.lineEdit_18.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 900, 10))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color:red;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(self.widget)
        self.frame_4.setGeometry(QtCore.QRect(410, 30, 10, 440))
        self.frame_4.setStyleSheet("QFrame{\n"
"background-color:#ff9100;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setGeometry(QtCore.QRect(440, 40, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_20.setObjectName("label_20")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_19.setGeometry(QtCore.QRect(570, 40, 190, 22))
        self.lineEdit_19.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_19.setText("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_20.setGeometry(QtCore.QRect(130, 265, 190, 22))
        self.lineEdit_20.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setGeometry(QtCore.QRect(10, 260, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_21.setObjectName("label_21")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_21.setGeometry(QtCore.QRect(570, 95, 190, 22))
        self.lineEdit_21.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setGeometry(QtCore.QRect(440, 90, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_22.setObjectName("label_22")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_22.setGeometry(QtCore.QRect(570, 155, 190, 22))
        self.lineEdit_22.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_23 = QtWidgets.QLabel(self.widget)
        self.label_23.setGeometry(QtCore.QRect(440, 150, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_23.setObjectName("label_23")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_23.setGeometry(QtCore.QRect(570, 210, 190, 22))
        self.lineEdit_23.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_24 = QtWidgets.QLabel(self.widget)
        self.label_24.setGeometry(QtCore.QRect(440, 205, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.widget)
        self.label_25.setGeometry(QtCore.QRect(440, 260, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_25.setObjectName("label_25")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_24.setGeometry(QtCore.QRect(570, 265, 190, 22))
        self.lineEdit_24.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_26 = QtWidgets.QLabel(self.widget)
        self.label_26.setGeometry(QtCore.QRect(10, 430, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_26.setObjectName("label_26")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_25.setGeometry(QtCore.QRect(130, 435, 190, 22))
        self.lineEdit_25.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.label_27 = QtWidgets.QLabel(self.widget)
        self.label_27.setGeometry(QtCore.QRect(10, 475, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_27.setObjectName("label_27")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_26.setGeometry(QtCore.QRect(120, 480, 190, 22))
        self.lineEdit_26.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 315, 74, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setGeometry(QtCore.QRect(130, 150, 90, 20))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButtonteacher = QtWidgets.QPushButton(self.widget)
        self.pushButtonteacher.setGeometry(QtCore.QRect(400, 540, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButtonteacher.setFont(font)
        self.pushButtonteacher.setStyleSheet("QPushButton{color: #fff !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #ed3330;\n"
"padding: 20px;\n"
"border-radius: 5px;\n"
"display: inline-block;\n"
"border: none;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #434343;\n"
"letter-spacing: 1px;\n"
"box-shadow: 5px 40px -10px rgba(0,0,0,0.57);\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButtonteacher.setObjectName("pushButtonteacher")
        self.tabWidget.addTab(self.widget, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.frame = QtWidgets.QFrame(self.tab3)
        self.frame.setGeometry(QtCore.QRect(0, 0, 880, 10))
        self.frame.setStyleSheet("QFrame{\n"
"background-color:red;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.tab3)
        self.lineEdit_47.setGeometry(QtCore.QRect(140, 220, 190, 22))
        self.lineEdit_47.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.lineEdit_48 = QtWidgets.QLineEdit(self.tab3)
        self.lineEdit_48.setGeometry(QtCore.QRect(140, 390, 190, 22))
        self.lineEdit_48.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.label_57 = QtWidgets.QLabel(self.tab3)
        self.label_57.setGeometry(QtCore.QRect(20, 100, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.tab3)
        self.label_58.setGeometry(QtCore.QRect(20, 485, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.tab3)
        self.label_59.setGeometry(QtCore.QRect(20, 440, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.tab3)
        self.label_60.setGeometry(QtCore.QRect(20, 380, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.tab3)
        self.label_61.setGeometry(QtCore.QRect(20, 40, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_61.setObjectName("label_61")
        self.dateEdit_5 = QtWidgets.QDateEdit(self.tab3)
        self.dateEdit_5.setGeometry(QtCore.QRect(140, 160, 90, 20))
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.lineEdit_49 = QtWidgets.QLineEdit(self.tab3)
        self.lineEdit_49.setGeometry(QtCore.QRect(140, 50, 190, 22))
        self.lineEdit_49.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.label_62 = QtWidgets.QLabel(self.tab3)
        self.label_62.setGeometry(QtCore.QRect(20, 320, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_62.setObjectName("label_62")
        self.lineEdit_50 = QtWidgets.QLineEdit(self.tab3)
        self.lineEdit_50.setGeometry(QtCore.QRect(140, 445, 190, 22))
        self.lineEdit_50.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.label_63 = QtWidgets.QLabel(self.tab3)
        self.label_63.setGeometry(QtCore.QRect(20, 270, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_63.setObjectName("label_63")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab3)
        self.comboBox_5.setGeometry(QtCore.QRect(140, 325, 74, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.setItemText(0, "")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_64 = QtWidgets.QLabel(self.tab3)
        self.label_64.setGeometry(QtCore.QRect(20, 210, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_64.setFont(font)
        self.label_64.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.tab3)
        self.label_65.setGeometry(QtCore.QRect(20, 150, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_65.setFont(font)
        self.label_65.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_65.setObjectName("label_65")
        self.lineEdit_51 = QtWidgets.QLineEdit(self.tab3)
        self.lineEdit_51.setGeometry(QtCore.QRect(140, 275, 190, 22))
        self.lineEdit_51.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.lineEdit_52 = QtWidgets.QLineEdit(self.tab3)
        self.lineEdit_52.setGeometry(QtCore.QRect(130, 490, 190, 22))
        self.lineEdit_52.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.lineEdit_53 = QtWidgets.QLineEdit(self.tab3)
        self.lineEdit_53.setGeometry(QtCore.QRect(140, 110, 190, 22))
        self.lineEdit_53.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.lineEdit_84 = QtWidgets.QLineEdit(self.tab3)
        self.lineEdit_84.setGeometry(QtCore.QRect(600, 60, 190, 22))
        self.lineEdit_84.setStyleSheet("QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.lineEdit_84.setObjectName("lineEdit_84")
        self.label_103 = QtWidgets.QLabel(self.tab3)
        self.label_103.setGeometry(QtCore.QRect(510, 50, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_103.setFont(font)
        self.label_103.setStyleSheet("QLabel{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"\n"
"")
        self.label_103.setObjectName("label_103")
        self.frame_16 = QtWidgets.QFrame(self.tab3)
        self.frame_16.setGeometry(QtCore.QRect(460, 50, 10, 440))
        self.frame_16.setStyleSheet("QFrame{\n"
"background-color:#ff9100;\n"
"}")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.pushButtonotherstuff = QtWidgets.QPushButton(self.tab3)
        self.pushButtonotherstuff.setGeometry(QtCore.QRect(420, 540, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButtonotherstuff.setFont(font)
        self.pushButtonotherstuff.setStyleSheet("QPushButton{color: #fff !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #ed3330;\n"
"padding: 20px;\n"
"border-radius: 5px;\n"
"display: inline-block;\n"
"border: none;\n"
"transition: all 0.4s ease 0s;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #434343;\n"
"letter-spacing: 1px;\n"
"box-shadow: 5px 40px -10px rgba(0,0,0,0.57);\n"
"transition: all 0.4s ease 0s;\n"
"}")
        self.pushButtonotherstuff.setObjectName("pushButtonotherstuff")
        self.tabWidget.addTab(self.tab3, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Student Details"))
        self.studenfirstnamelabel.setText(_translate("Form", "First Name :"))
        self.studenlastnamelabel.setText(_translate("Form", "Last  Name :"))
        self.Dobla.setText(_translate("Form", "DOB :"))
        self.label_5.setText(_translate("Form", "StudD :"))
        self.label_6.setText(_translate("Form", "Place Of Birth :"))
        self.stu_fatherN_label.setText(_translate("Form", "Father Name :"))
        self.stu_motherN_label.setText(_translate("Form", "Mother  Name :"))
        self.stu_father_occ_label.setText(_translate("Form", "Father Occupation :"))
        self.stu_mother_occ_labe.setText(_translate("Form", "Mother Occupation :"))
        self.label_12.setText(_translate("Form", "Gender"))
        self.label_13.setText(_translate("Form", "Nationnality"))
        self.stu_father_sal_label.setText(_translate("Form", "Father Salary"))
        self.label_28.setText(_translate("Form", "Mother Salary"))
        self.stugendertext.setItemText(1, _translate("Form", "Male"))
        self.stugendertext.setItemText(2, _translate("Form", "Female"))
        self.stugendertext.setItemText(3, _translate("Form", "Custom"))
        self.pushButtonstu.setText(_translate("Form", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Teachers), _translate("Form", "Students"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.Teachers), _translate("Form", "Student Details"))
        self.label_7.setText(_translate("Form", "DOB :"))
        self.label_14.setText(_translate("Form", "Last  Name :"))
        self.label_16.setText(_translate("Form", "First Name :"))
        self.label_17.setText(_translate("Form", "Gender"))
        self.label_18.setText(_translate("Form", "Nationnality"))
        self.label_19.setText(_translate("Form", "Qualification"))
        self.label_20.setText(_translate("Form", "Mail Id :"))
        self.label_21.setText(_translate("Form", "Age"))
        self.label_22.setText(_translate("Form", "Contact No :"))
        self.label_23.setText(_translate("Form", "Adress 1 :"))
        self.label_24.setText(_translate("Form", "Adress 2 :"))
        self.label_25.setText(_translate("Form", "Adress 3 :"))
        self.label_26.setText(_translate("Form", "Salary"))
        self.label_27.setText(_translate("Form", "Subject"))
        self.comboBox_2.setItemText(1, _translate("Form", "Male"))
        self.comboBox_2.setItemText(2, _translate("Form", "Female"))
        self.comboBox_2.setItemText(3, _translate("Form", "Custom"))
        self.pushButtonteacher.setText(_translate("Form", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Form", "Teachers"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.widget), _translate("Form", "Teachers Details"))
        self.label_57.setText(_translate("Form", "Last  Name :"))
        self.label_58.setText(_translate("Form", "Subject"))
        self.label_59.setText(_translate("Form", "Salary"))
        self.label_60.setText(_translate("Form", "Nationnality"))
        self.label_61.setText(_translate("Form", "First Name :"))
        self.label_62.setText(_translate("Form", "Gender"))
        self.label_63.setText(_translate("Form", "Age"))
        self.comboBox_5.setItemText(1, _translate("Form", "Male"))
        self.comboBox_5.setItemText(2, _translate("Form", "Female"))
        self.comboBox_5.setItemText(3, _translate("Form", "Custom"))
        self.label_64.setText(_translate("Form", "Qualification"))
        self.label_65.setText(_translate("Form", "DOB :"))
        self.label_103.setText(_translate("Form", "Position :"))
        self.pushButtonotherstuff.setText(_translate("Form", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("Form", "Other Stuffs"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
