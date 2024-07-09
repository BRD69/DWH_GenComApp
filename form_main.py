import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from form_text import UiDialogText


def get_index(array, param):
    for index, value in enumerate(array):
        if param in value:
            return index


def get_position(text, param):
    return text.index(param)


class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        super(UiMainWindow, self).__init__()

        self.app = app

        self._param_dmn = self.app.templates.param_dmn
        self._param_dis = self.app.templates.param_dis
        self._param_app = self.app.templates.param_app
        self._param_wf = self.app.templates.param_wf
        self._param_ps = self.app.templates.param_ps

        self._start_job__array = list(self.app.templates.start_job)
        self._start_job__prefix = self.app.templates.start_job_prefix
        self._start_job__index_params = {
            "_param_dmn": get_index(self._start_job__array, self._param_dmn),
            "_param_dis": get_index(self._start_job__array, self._param_dis),
            "_param_app": get_index(self._start_job__array, self._param_app),
            "_param_wf": get_index(self._start_job__array, self._param_wf),
            "_param_ps": get_index(self._start_job__array, self._param_ps),
        }
        self._start_job__position_params = {
            "_param_dmn": get_position(' '.join(self._start_job__array), self._param_dmn),
            "_param_dis": get_position(' '.join(self._start_job__array), self._param_dis),
            "_param_app": get_position(' '.join(self._start_job__array), self._param_app),
            "_param_wf": get_position(' '.join(self._start_job__array), self._param_wf),
            "_param_ps": get_position(' '.join(self._start_job__array), self._param_ps),
        }

        self._start_prod_app__array = list(self.app.templates.start_prod_app)
        self._start_prod_app__prefix = self.app.templates.start_prod_app_prefix
        self._start_prod_app__index_param = {
            "_param_dmn": get_index(self._start_prod_app__array, self._param_dmn),
            "_param_dis": get_index(self._start_prod_app__array, self._param_dis),
            "_param_app": get_index(self._start_prod_app__array, self._param_app),
            "_param_wf": -1,
            "_param_ps": -1,
        }
        self._start_prod_app__position_params = {
            "_param_dmn": get_position(' '.join(self._start_prod_app__array), self._param_dmn),
            "_param_dis": get_position(' '.join(self._start_prod_app__array), self._param_dis),
            "_param_app": get_position(' '.join(self._start_prod_app__array), self._param_app),
            "_param_wf": 0,
            "_param_ps": 0,
        }

        self._stop_prod_app__array = list(self.app.templates.stop_prod_app)
        self._stop_prod_app__prefix = self.app.templates.stop_prod_app_prefix
        self._stop_prod_app__index_param = {
            "_param_dmn": get_index(self._stop_prod_app__array, self._param_dmn),
            "_param_dis": get_index(self._stop_prod_app__array, self._param_dis),
            "_param_app": get_index(self._stop_prod_app__array, self._param_app),
            "_param_wf": -1,
            "_param_ps": -1,
        }
        self._stop_prod_app__position_params = {}

        self._start_prod_wf__array = list(self.app.templates.start_prod_wf)
        self._start_prod_wf__prefix = self.app.templates.start_prod_wf_prefix
        self._start_prod_wf__index_param = {
            "_param_dmn": get_index(self._start_prod_wf__array, self._param_dmn),
            "_param_dis": get_index(self._start_prod_wf__array, self._param_dis),
            "_param_app": get_index(self._start_prod_wf__array, self._param_app),
            "_param_wf": get_index(self._start_prod_wf__array, self._param_wf),
            "_param_ps": get_index(self._start_prod_wf__array, self._param_ps),
        }
        self._start_prod_wf__position_params = {
            "_param_dmn": get_position(' '.join(self._start_prod_wf__array), self._param_dmn),
            "_param_dis": get_position(' '.join(self._start_prod_wf__array), self._param_dis),
            "_param_app": get_position(' '.join(self._start_prod_wf__array), self._param_app),
            "_param_wf": get_position(' '.join(self._start_prod_wf__array), self._param_wf),
            "_param_ps": get_position(' '.join(self._start_prod_wf__array), self._param_ps),
        }

        self._start_test_wf__array = list(self.app.templates.start_test_wf)
        self._start_test_wf__prefix = self.app.templates.start_test_wf_prefix
        self._start_test_wf__index_param = {
            "_param_dmn": get_index(self._start_test_wf__array, self._param_dmn),
            "_param_dis": get_index(self._start_test_wf__array, self._param_dis),
            "_param_app": get_index(self._start_test_wf__array, self._param_app),
            "_param_wf": get_index(self._start_test_wf__array, self._param_wf),
            "_param_ps": get_index(self._start_test_wf__array, self._param_ps),
        }
        self._start_test_wf__position_params = {}

        self._setupUi()
        self._connect_event()

    def _setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 825)
        self.setMinimumSize(QtCore.QSize(800, 825))
        self.setMaximumSize(QtCore.QSize(800, 825))
        self.setBaseSize(QtCore.QSize(800, 825))
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.setStyleSheet("QMainWindow{\n"
                           "    background-color: rgb(255, 255, 255);\n"
                           "}")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setObjectName("widget")
        self.frame_MAIN = QtWidgets.QFrame(self.widget)
        self.frame_MAIN.setGeometry(QtCore.QRect(0, 0, 800, 800))
        self.frame_MAIN.setStyleSheet("#frame_MAIN{\n"
                                      "    \n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "}")
        self.frame_MAIN.setObjectName("frame_MAIN")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_MAIN)
        self.verticalLayout_8.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_8.setSpacing(30)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_INPUT = QtWidgets.QGroupBox(self.frame_MAIN)
        self.groupBox_INPUT.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_INPUT.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_INPUT.setBaseSize(QtCore.QSize(0, 200))
        self.groupBox_INPUT.setStyleSheet("QGroupBox{\n"
                                          "    border: 1px solid rgb(137, 137, 137);\n"
                                          "    border-radius: 5px;\n"
                                          "    background-color: rgb(227, 227, 227);\n"
                                          "}")
        self.groupBox_INPUT.setTitle("")
        self.groupBox_INPUT.setObjectName("groupBox_INPUT")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_INPUT)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_DMN = QtWidgets.QFrame(self.groupBox_INPUT)
        self.frame_DMN.setObjectName("frame_DMN")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_DMN)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_icon_DMN = QtWidgets.QLabel(self.frame_DMN)
        self.lbl_icon_DMN.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_DMN.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_DMN.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_DMN.setText("")
        self.lbl_icon_DMN.setPixmap(QtGui.QPixmap(":/img/img/DMN.png"))
        self.lbl_icon_DMN.setObjectName("lbl_icon_DMN")
        self.horizontalLayout.addWidget(self.lbl_icon_DMN)
        self.lbl_text_DMN = QtWidgets.QLabel(self.frame_DMN)
        self.lbl_text_DMN.setMinimumSize(QtCore.QSize(35, 0))
        self.lbl_text_DMN.setMaximumSize(QtCore.QSize(35, 16777215))
        self.lbl_text_DMN.setBaseSize(QtCore.QSize(35, 0))
        self.lbl_text_DMN.setStyleSheet("QLabel{\n"
                                        "    font-size: 13px;\n"
                                        "    font-weight: 500;\n"
                                        "}")
        self.lbl_text_DMN.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_text_DMN.setScaledContents(False)
        self.lbl_text_DMN.setObjectName("lbl_text_DMN")
        self.horizontalLayout.addWidget(self.lbl_text_DMN)
        self.edit_DMN = QtWidgets.QLineEdit(self.frame_DMN)
        self.edit_DMN.setMinimumSize(QtCore.QSize(0, 20))
        self.edit_DMN.setMaximumSize(QtCore.QSize(16777215, 20))
        self.edit_DMN.setStyleSheet("QLineEdit{\n"
                                    "    padding-left:3px;\n"
                                    "    border: 1px solid rgb(180, 180, 180);\n"
                                    "    border-radius: 3px;\n"
                                    "}")
        self.edit_DMN.setText("")
        self.edit_DMN.setObjectName("edit_DMN")
        self.horizontalLayout.addWidget(self.edit_DMN)
        self.verticalLayout.addWidget(self.frame_DMN)
        self.frame_DIS = QtWidgets.QFrame(self.groupBox_INPUT)
        self.frame_DIS.setObjectName("frame_DIS")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_DIS)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_icon_DIS = QtWidgets.QLabel(self.frame_DIS)
        self.lbl_icon_DIS.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_DIS.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_DIS.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_DIS.setText("")
        self.lbl_icon_DIS.setPixmap(QtGui.QPixmap(":/img/img/DIS.png"))
        self.lbl_icon_DIS.setObjectName("lbl_icon_DIS")
        self.horizontalLayout_2.addWidget(self.lbl_icon_DIS)
        self.lbl_text_DIS = QtWidgets.QLabel(self.frame_DIS)
        self.lbl_text_DIS.setMinimumSize(QtCore.QSize(35, 0))
        self.lbl_text_DIS.setMaximumSize(QtCore.QSize(35, 16777215))
        self.lbl_text_DIS.setBaseSize(QtCore.QSize(35, 0))
        self.lbl_text_DIS.setStyleSheet("QLabel{\n"
                                        "    font-size: 13px;\n"
                                        "    font-weight: 500;\n"
                                        "}")
        self.lbl_text_DIS.setObjectName("lbl_text_DIS")
        self.horizontalLayout_2.addWidget(self.lbl_text_DIS)
        self.edit_DIS = QtWidgets.QLineEdit(self.frame_DIS)
        self.edit_DIS.setMinimumSize(QtCore.QSize(0, 20))
        self.edit_DIS.setMaximumSize(QtCore.QSize(16777215, 20))
        self.edit_DIS.setStyleSheet("QLineEdit{\n"
                                    "    padding-left:3px;\n"
                                    "    border: 1px solid rgb(180, 180, 180);\n"
                                    "}")
        self.edit_DIS.setText("")
        self.edit_DIS.setObjectName("edit_DIS")
        self.horizontalLayout_2.addWidget(self.edit_DIS)
        self.verticalLayout.addWidget(self.frame_DIS)
        self.frame_APP = QtWidgets.QFrame(self.groupBox_INPUT)
        self.frame_APP.setObjectName("frame_APP")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_APP)
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_icon_APP = QtWidgets.QLabel(self.frame_APP)
        self.lbl_icon_APP.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_APP.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_APP.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_APP.setText("")
        self.lbl_icon_APP.setPixmap(QtGui.QPixmap(":/img/img/APP.png"))
        self.lbl_icon_APP.setObjectName("lbl_icon_APP")
        self.horizontalLayout_3.addWidget(self.lbl_icon_APP)
        self.lbl_text_APP = QtWidgets.QLabel(self.frame_APP)
        self.lbl_text_APP.setMinimumSize(QtCore.QSize(35, 0))
        self.lbl_text_APP.setMaximumSize(QtCore.QSize(35, 16777215))
        self.lbl_text_APP.setBaseSize(QtCore.QSize(35, 0))
        self.lbl_text_APP.setStyleSheet("QLabel{\n"
                                        "    font-size: 13px;\n"
                                        "    font-weight: 500;\n"
                                        "}")
        self.lbl_text_APP.setObjectName("lbl_text_APP")
        self.horizontalLayout_3.addWidget(self.lbl_text_APP)
        self.edit_APP = QtWidgets.QLineEdit(self.frame_APP)
        self.edit_APP.setMinimumSize(QtCore.QSize(0, 20))
        self.edit_APP.setMaximumSize(QtCore.QSize(16777215, 20))
        self.edit_APP.setStyleSheet("QLineEdit{\n"
                                    "    padding-left:3px;\n"
                                    "    border: 1px solid rgb(180, 180, 180);\n"
                                    "}")
        self.edit_APP.setText("")
        self.edit_APP.setObjectName("edit_APP")
        self.horizontalLayout_3.addWidget(self.edit_APP)
        self.verticalLayout.addWidget(self.frame_APP)
        self.frame_WF = QtWidgets.QFrame(self.groupBox_INPUT)
        self.frame_WF.setObjectName("frame_WF")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_WF)
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_icon_WF = QtWidgets.QLabel(self.frame_WF)
        self.lbl_icon_WF.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_WF.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_WF.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_WF.setText("")
        self.lbl_icon_WF.setPixmap(QtGui.QPixmap(":/img/img/WF.png"))
        self.lbl_icon_WF.setObjectName("lbl_icon_WF")
        self.horizontalLayout_4.addWidget(self.lbl_icon_WF)
        self.lbl_text_WF = QtWidgets.QLabel(self.frame_WF)
        self.lbl_text_WF.setMinimumSize(QtCore.QSize(35, 0))
        self.lbl_text_WF.setMaximumSize(QtCore.QSize(35, 16777215))
        self.lbl_text_WF.setBaseSize(QtCore.QSize(35, 0))
        self.lbl_text_WF.setStyleSheet("QLabel{\n"
                                       "    font-size: 13px;\n"
                                       "    font-weight: 500;\n"
                                       "}")
        self.lbl_text_WF.setObjectName("lbl_text_WF")
        self.horizontalLayout_4.addWidget(self.lbl_text_WF)
        self.edit_WF = QtWidgets.QLineEdit(self.frame_WF)
        self.edit_WF.setMinimumSize(QtCore.QSize(0, 20))
        self.edit_WF.setMaximumSize(QtCore.QSize(16777215, 20))
        self.edit_WF.setStyleSheet("QLineEdit{\n"
                                   "    padding-left:3px;\n"
                                   "    border: 1px solid rgb(180, 180, 180);\n"
                                   "}")
        self.edit_WF.setText("")
        self.edit_WF.setObjectName("edit_WF")
        self.horizontalLayout_4.addWidget(self.edit_WF)
        self.verticalLayout.addWidget(self.frame_WF)
        self.frame_PS = QtWidgets.QFrame(self.groupBox_INPUT)
        self.frame_PS.setObjectName("frame_PS")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_PS)
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_icon_PS = QtWidgets.QLabel(self.frame_PS)
        self.lbl_icon_PS.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_PS.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_PS.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_PS.setText("")
        self.lbl_icon_PS.setPixmap(QtGui.QPixmap(":/img/img/PS.png"))
        self.lbl_icon_PS.setObjectName("lbl_icon_PS")
        self.horizontalLayout_5.addWidget(self.lbl_icon_PS)
        self.lbl_text_PS = QtWidgets.QLabel(self.frame_PS)
        self.lbl_text_PS.setMinimumSize(QtCore.QSize(35, 0))
        self.lbl_text_PS.setMaximumSize(QtCore.QSize(35, 16777215))
        self.lbl_text_PS.setBaseSize(QtCore.QSize(35, 0))
        self.lbl_text_PS.setStyleSheet("QLabel{\n"
                                       "    font-size: 13px;\n"
                                       "    font-weight: 500;\n"
                                       "}")
        self.lbl_text_PS.setObjectName("lbl_text_PS")
        self.horizontalLayout_5.addWidget(self.lbl_text_PS)
        self.edit_PS = QtWidgets.QLineEdit(self.frame_PS)
        self.edit_PS.setMinimumSize(QtCore.QSize(0, 20))
        self.edit_PS.setMaximumSize(QtCore.QSize(16777215, 20))
        self.edit_PS.setStyleSheet("QLineEdit{\n"
                                   "    padding-left:3px;\n"
                                   "    border: 1px solid rgb(180, 180, 180);\n"
                                   "}")
        self.edit_PS.setText("")
        self.edit_PS.setObjectName("edit_PS")
        self.horizontalLayout_5.addWidget(self.edit_PS)
        self.verticalLayout.addWidget(self.frame_PS)
        self.verticalLayout_8.addWidget(self.groupBox_INPUT)
        self.frame_START = QtWidgets.QFrame(self.frame_MAIN)
        self.frame_START.setStyleSheet("#frame_START{\n"
                                       "    border: 1px solid rgb(137, 137, 137);\n"
                                       "    border-radius: 5px;\n"
                                       "    background-color: rgb(227, 227, 227);\n"
                                       "}")
        self.frame_START.setObjectName("frame_START")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_START)
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_START_JOB = QtWidgets.QGroupBox(self.frame_START)
        self.groupBox_START_JOB.setStyleSheet("QGroupBox{\n"
                                              "    border: 1px solid rgb(137, 137, 137);\n"
                                              "    border-radius: 5px;\n"
                                              "    background-color: rgb(237, 237, 237);\n"
                                              "}")
        self.groupBox_START_JOB.setObjectName("groupBox_START_JOB")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_START_JOB)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_title_START_JOB = QtWidgets.QFrame(self.groupBox_START_JOB)
        self.frame_title_START_JOB.setObjectName("frame_title_START_JOB")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_title_START_JOB)
        self.horizontalLayout_24.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.lbl_icon_START_JOB_0 = QtWidgets.QLabel(self.frame_title_START_JOB)
        self.lbl_icon_START_JOB_0.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_JOB_0.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_JOB_0.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_JOB_0.setStyleSheet("QLabel{\n"
                                                "    padding-left: 7px;\n"
                                                "}")
        self.lbl_icon_START_JOB_0.setText("")
        self.lbl_icon_START_JOB_0.setPixmap(QtGui.QPixmap(":/img/img/APP.png"))
        self.lbl_icon_START_JOB_0.setObjectName("lbl_icon_START_JOB_0")
        self.horizontalLayout_24.addWidget(self.lbl_icon_START_JOB_0)
        self.lbl_icon_START_JOB_1 = QtWidgets.QLabel(self.frame_title_START_JOB)
        self.lbl_icon_START_JOB_1.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_JOB_1.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_JOB_1.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_JOB_1.setStyleSheet("QLabel{\n"
                                                "    padding-left: 7px;\n"
                                                "}")
        self.lbl_icon_START_JOB_1.setText("")
        self.lbl_icon_START_JOB_1.setPixmap(QtGui.QPixmap(":/img/img/start.png"))
        self.lbl_icon_START_JOB_1.setObjectName("lbl_icon_START_JOB_1")
        self.horizontalLayout_24.addWidget(self.lbl_icon_START_JOB_1)
        self.lbl_title_START_JOB = QtWidgets.QLabel(self.frame_title_START_JOB)
        self.lbl_title_START_JOB.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_title_START_JOB.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lbl_title_START_JOB.setBaseSize(QtCore.QSize(0, 30))
        self.lbl_title_START_JOB.setStyleSheet("QLabel{\n"
                                               "    font-size: 13px;\n"
                                               "    font-weight: 500;\n"
                                               "}")
        self.lbl_title_START_JOB.setObjectName("lbl_title_START_JOB")
        self.horizontalLayout_24.addWidget(self.lbl_title_START_JOB)
        self.verticalLayout_6.addWidget(self.frame_title_START_JOB)
        self.frame_action_START_JOB = QtWidgets.QFrame(self.groupBox_START_JOB)
        self.frame_action_START_JOB.setObjectName("frame_action_START_JOB")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_action_START_JOB)
        self.horizontalLayout_25.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.edit_START_JOB = QtWidgets.QLineEdit(self.frame_action_START_JOB)
        self.edit_START_JOB.setMinimumSize(QtCore.QSize(0, 30))
        self.edit_START_JOB.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edit_START_JOB.setBaseSize(QtCore.QSize(0, 30))
        self.edit_START_JOB.setStyleSheet("QLineEdit{\n"
                                          "    padding-left:3px;\n"
                                          "    border: 1px solid rgb(180, 180, 180);\n"
                                          "    border-radius: 3px;\n"
                                          "}")
        self.edit_START_JOB.setReadOnly(True)
        self.edit_START_JOB.setObjectName("edit_START_JOB")
        self.horizontalLayout_25.addWidget(self.edit_START_JOB)
        self.btn_view_START_JOB = QtWidgets.QPushButton(self.frame_action_START_JOB)
        self.btn_view_START_JOB.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_view_START_JOB.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_view_START_JOB.setBaseSize(QtCore.QSize(30, 30))
        self.btn_view_START_JOB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_view_START_JOB.setStyleSheet("QPushButton{\n"
                                              "    border: 1px solid rgb(167, 167, 167);\n"
                                              "    background: rgb(242, 242, 242);\n"
                                              "    font-size: 14px;\n"
                                              "    border-radius: 3px;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "background-color: rgba(200, 200, 200, 128);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed{\n"
                                              "background-color: rgba(255, 255, 255, 128);\n"
                                              "}")
        self.btn_view_START_JOB.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_view_START_JOB.setIcon(icon)
        self.btn_view_START_JOB.setObjectName("btn_view_START_JOB")
        self.horizontalLayout_25.addWidget(self.btn_view_START_JOB)
        self.btn_copy_START_JOB = QtWidgets.QPushButton(self.frame_action_START_JOB)
        self.btn_copy_START_JOB.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_copy_START_JOB.setMaximumSize(QtCore.QSize(100, 30))
        self.btn_copy_START_JOB.setBaseSize(QtCore.QSize(0, 30))
        self.btn_copy_START_JOB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_copy_START_JOB.setStyleSheet("QPushButton{\n"
                                              "    border: 1px solid rgb(167, 167, 167);\n"
                                              "    background: rgb(242, 242, 242);\n"
                                              "    font-size: 14px;\n"
                                              "    border-radius: 3px;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "background-color: rgba(200, 200, 200, 128);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed{\n"
                                              "background-color: rgba(255, 255, 255, 128);\n"
                                              "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_copy_START_JOB.setIcon(icon1)
        self.btn_copy_START_JOB.setObjectName("btn_copy_START_JOB")
        self.horizontalLayout_25.addWidget(self.btn_copy_START_JOB)
        self.verticalLayout_6.addWidget(self.frame_action_START_JOB)
        self.verticalLayout_7.addWidget(self.groupBox_START_JOB)
        self.groupBox_START_PROD_APP = QtWidgets.QGroupBox(self.frame_START)
        self.groupBox_START_PROD_APP.setStyleSheet("QGroupBox{\n"
                                                   "    border: 1px solid rgb(137, 137, 137);\n"
                                                   "    border-radius: 5px;\n"
                                                   "    background-color: rgb(237, 237, 237);\n"
                                                   "}")
        self.groupBox_START_PROD_APP.setObjectName("groupBox_START_PROD_APP")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_START_PROD_APP)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_title_START_PROD_APP = QtWidgets.QFrame(self.groupBox_START_PROD_APP)
        self.frame_title_START_PROD_APP.setObjectName("frame_title_START_PROD_APP")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_title_START_PROD_APP)
        self.horizontalLayout_22.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.lbl_icon_START_PROD_APP_0 = QtWidgets.QLabel(self.frame_title_START_PROD_APP)
        self.lbl_icon_START_PROD_APP_0.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_APP_0.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_APP_0.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_APP_0.setStyleSheet("QLabel{\n"
                                                     "    padding-left: 7px;\n"
                                                     "}")
        self.lbl_icon_START_PROD_APP_0.setText("")
        self.lbl_icon_START_PROD_APP_0.setPixmap(QtGui.QPixmap(":/img/img/APP.png"))
        self.lbl_icon_START_PROD_APP_0.setObjectName("lbl_icon_START_PROD_APP_0")
        self.horizontalLayout_22.addWidget(self.lbl_icon_START_PROD_APP_0)
        self.lbl_icon_START_PROD_APP_2 = QtWidgets.QLabel(self.frame_title_START_PROD_APP)
        self.lbl_icon_START_PROD_APP_2.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_APP_2.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_APP_2.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_APP_2.setStyleSheet("QLabel{\n"
                                                     "    padding-left: 7px;\n"
                                                     "}")
        self.lbl_icon_START_PROD_APP_2.setText("")
        self.lbl_icon_START_PROD_APP_2.setPixmap(QtGui.QPixmap(":/img/img/prod.png"))
        self.lbl_icon_START_PROD_APP_2.setObjectName("lbl_icon_START_PROD_APP_2")
        self.horizontalLayout_22.addWidget(self.lbl_icon_START_PROD_APP_2)
        self.lbl_icon_START_PROD_APP_1 = QtWidgets.QLabel(self.frame_title_START_PROD_APP)
        self.lbl_icon_START_PROD_APP_1.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_APP_1.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_APP_1.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_APP_1.setStyleSheet("QLabel{\n"
                                                     "    padding-left: 7px;\n"
                                                     "}")
        self.lbl_icon_START_PROD_APP_1.setText("")
        self.lbl_icon_START_PROD_APP_1.setPixmap(QtGui.QPixmap(":/img/img/start.png"))
        self.lbl_icon_START_PROD_APP_1.setObjectName("lbl_icon_START_PROD_APP_1")
        self.horizontalLayout_22.addWidget(self.lbl_icon_START_PROD_APP_1)
        self.lbl_title_START_PROD_APP = QtWidgets.QLabel(self.frame_title_START_PROD_APP)
        self.lbl_title_START_PROD_APP.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_title_START_PROD_APP.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lbl_title_START_PROD_APP.setBaseSize(QtCore.QSize(0, 30))
        self.lbl_title_START_PROD_APP.setStyleSheet("QLabel{\n"
                                                    "    font-size: 13px;\n"
                                                    "    font-weight: 500;\n"
                                                    "}")
        self.lbl_title_START_PROD_APP.setObjectName("lbl_title_START_PROD_APP")
        self.horizontalLayout_22.addWidget(self.lbl_title_START_PROD_APP)
        self.verticalLayout_5.addWidget(self.frame_title_START_PROD_APP)
        self.frame_action_START_PROD_APP = QtWidgets.QFrame(self.groupBox_START_PROD_APP)
        self.frame_action_START_PROD_APP.setObjectName("frame_action_START_PROD_APP")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_action_START_PROD_APP)
        self.horizontalLayout_23.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.edit_START_PROD_APP = QtWidgets.QLineEdit(self.frame_action_START_PROD_APP)
        self.edit_START_PROD_APP.setMinimumSize(QtCore.QSize(0, 30))
        self.edit_START_PROD_APP.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edit_START_PROD_APP.setBaseSize(QtCore.QSize(0, 30))
        self.edit_START_PROD_APP.setStyleSheet("QLineEdit{\n"
                                               "    padding-left:3px;\n"
                                               "    border: 1px solid rgb(180, 180, 180);\n"
                                               "    border-radius: 3px;\n"
                                               "}")
        self.edit_START_PROD_APP.setReadOnly(True)
        self.edit_START_PROD_APP.setObjectName("edit_START_PROD_APP")
        self.horizontalLayout_23.addWidget(self.edit_START_PROD_APP)
        self.btn_view_START_PROD_APP = QtWidgets.QPushButton(self.frame_action_START_PROD_APP)
        self.btn_view_START_PROD_APP.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_view_START_PROD_APP.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_view_START_PROD_APP.setBaseSize(QtCore.QSize(30, 30))
        self.btn_view_START_PROD_APP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_view_START_PROD_APP.setStyleSheet("QPushButton{\n"
                                                   "    border: 1px solid rgb(167, 167, 167);\n"
                                                   "    background: rgb(242, 242, 242);\n"
                                                   "    font-size: 14px;\n"
                                                   "    border-radius: 3px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:hover{\n"
                                                   "background-color: rgba(200, 200, 200, 128);\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:pressed{\n"
                                                   "background-color: rgba(255, 255, 255, 128);\n"
                                                   "}")
        self.btn_view_START_PROD_APP.setText("")
        self.btn_view_START_PROD_APP.setIcon(icon)
        self.btn_view_START_PROD_APP.setObjectName("btn_view_START_PROD_APP")
        self.horizontalLayout_23.addWidget(self.btn_view_START_PROD_APP)
        self.btn_copy_START_PROD_APP = QtWidgets.QPushButton(self.frame_action_START_PROD_APP)
        self.btn_copy_START_PROD_APP.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_copy_START_PROD_APP.setMaximumSize(QtCore.QSize(100, 30))
        self.btn_copy_START_PROD_APP.setBaseSize(QtCore.QSize(0, 30))
        self.btn_copy_START_PROD_APP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_copy_START_PROD_APP.setStyleSheet("QPushButton{\n"
                                                   "    border: 1px solid rgb(167, 167, 167);\n"
                                                   "    background: rgb(242, 242, 242);\n"
                                                   "    font-size: 14px;\n"
                                                   "    border-radius: 3px;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:hover{\n"
                                                   "background-color: rgba(200, 200, 200, 128);\n"
                                                   "}\n"
                                                   "\n"
                                                   "QPushButton:pressed{\n"
                                                   "background-color: rgba(255, 255, 255, 128);\n"
                                                   "}\n"
                                                   "")
        self.btn_copy_START_PROD_APP.setIcon(icon1)
        self.btn_copy_START_PROD_APP.setObjectName("btn_copy_START_PROD_APP")
        self.horizontalLayout_23.addWidget(self.btn_copy_START_PROD_APP)
        self.verticalLayout_5.addWidget(self.frame_action_START_PROD_APP)
        self.verticalLayout_7.addWidget(self.groupBox_START_PROD_APP)
        self.groupBox_STOP_PROD_APP = QtWidgets.QGroupBox(self.frame_START)
        self.groupBox_STOP_PROD_APP.setStyleSheet("QGroupBox{\n"
                                                  "    border: 1px solid rgb(137, 137, 137);\n"
                                                  "    border-radius: 5px;\n"
                                                  "    background-color: rgb(237, 237, 237);\n"
                                                  "}")
        self.groupBox_STOP_PROD_APP.setObjectName("groupBox_STOP_PROD_APP")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_STOP_PROD_APP)
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_title_STOP_PROD_APP = QtWidgets.QFrame(self.groupBox_STOP_PROD_APP)
        self.frame_title_STOP_PROD_APP.setObjectName("frame_title_STOP_PROD_APP")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_title_STOP_PROD_APP)
        self.horizontalLayout_20.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.lbl_icon_STOP_PROD_APP_0 = QtWidgets.QLabel(self.frame_title_STOP_PROD_APP)
        self.lbl_icon_STOP_PROD_APP_0.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_STOP_PROD_APP_0.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_STOP_PROD_APP_0.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_STOP_PROD_APP_0.setStyleSheet("QLabel{\n"
                                                    "    padding-left: 7px;\n"
                                                    "}")
        self.lbl_icon_STOP_PROD_APP_0.setText("")
        self.lbl_icon_STOP_PROD_APP_0.setPixmap(QtGui.QPixmap(":/img/img/APP.png"))
        self.lbl_icon_STOP_PROD_APP_0.setObjectName("lbl_icon_STOP_PROD_APP_0")
        self.horizontalLayout_20.addWidget(self.lbl_icon_STOP_PROD_APP_0)
        self.lbl_icon_STOP_PROD_APP_2 = QtWidgets.QLabel(self.frame_title_STOP_PROD_APP)
        self.lbl_icon_STOP_PROD_APP_2.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_STOP_PROD_APP_2.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_STOP_PROD_APP_2.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_STOP_PROD_APP_2.setStyleSheet("QLabel{\n"
                                                    "    padding-left: 7px;\n"
                                                    "}")
        self.lbl_icon_STOP_PROD_APP_2.setText("")
        self.lbl_icon_STOP_PROD_APP_2.setPixmap(QtGui.QPixmap(":/img/img/prod.png"))
        self.lbl_icon_STOP_PROD_APP_2.setObjectName("lbl_icon_STOP_PROD_APP_2")
        self.horizontalLayout_20.addWidget(self.lbl_icon_STOP_PROD_APP_2)
        self.lbl_icon_STOP_PROD_APP_1 = QtWidgets.QLabel(self.frame_title_STOP_PROD_APP)
        self.lbl_icon_STOP_PROD_APP_1.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_STOP_PROD_APP_1.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_STOP_PROD_APP_1.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_STOP_PROD_APP_1.setStyleSheet("QLabel{\n"
                                                    "    padding-left: 7px;\n"
                                                    "}")
        self.lbl_icon_STOP_PROD_APP_1.setText("")
        self.lbl_icon_STOP_PROD_APP_1.setPixmap(QtGui.QPixmap(":/img/img/stop.png"))
        self.lbl_icon_STOP_PROD_APP_1.setObjectName("lbl_icon_STOP_PROD_APP_1")
        self.horizontalLayout_20.addWidget(self.lbl_icon_STOP_PROD_APP_1)
        self.lbl_title_STOP_PROD_APP = QtWidgets.QLabel(self.frame_title_STOP_PROD_APP)
        self.lbl_title_STOP_PROD_APP.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_title_STOP_PROD_APP.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lbl_title_STOP_PROD_APP.setBaseSize(QtCore.QSize(0, 30))
        self.lbl_title_STOP_PROD_APP.setStyleSheet("QLabel{\n"
                                                   "    font-size: 13px;\n"
                                                   "    font-weight: 500;\n"
                                                   "}")
        self.lbl_title_STOP_PROD_APP.setObjectName("lbl_title_STOP_PROD_APP")
        self.horizontalLayout_20.addWidget(self.lbl_title_STOP_PROD_APP)
        self.verticalLayout_4.addWidget(self.frame_title_STOP_PROD_APP)
        self.frame_action_STOP_PROD_APP = QtWidgets.QFrame(self.groupBox_STOP_PROD_APP)
        self.frame_action_STOP_PROD_APP.setObjectName("frame_action_STOP_PROD_APP")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_action_STOP_PROD_APP)
        self.horizontalLayout_21.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.edit_STOP_PROD_APP = QtWidgets.QLineEdit(self.frame_action_STOP_PROD_APP)
        self.edit_STOP_PROD_APP.setMinimumSize(QtCore.QSize(0, 30))
        self.edit_STOP_PROD_APP.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edit_STOP_PROD_APP.setBaseSize(QtCore.QSize(0, 30))
        self.edit_STOP_PROD_APP.setStyleSheet("QLineEdit{\n"
                                              "    padding-left:3px;\n"
                                              "    border: 1px solid rgb(180, 180, 180);\n"
                                              "    border-radius: 3px;\n"
                                              "}")
        self.edit_STOP_PROD_APP.setReadOnly(True)
        self.edit_STOP_PROD_APP.setObjectName("edit_STOP_PROD_APP")
        self.horizontalLayout_21.addWidget(self.edit_STOP_PROD_APP)
        self.btn_view_STOP_PROD_APP = QtWidgets.QPushButton(self.frame_action_STOP_PROD_APP)
        self.btn_view_STOP_PROD_APP.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_view_STOP_PROD_APP.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_view_STOP_PROD_APP.setBaseSize(QtCore.QSize(30, 30))
        self.btn_view_STOP_PROD_APP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_view_STOP_PROD_APP.setStyleSheet("QPushButton{\n"
                                                  "    border: 1px solid rgb(167, 167, 167);\n"
                                                  "    background: rgb(242, 242, 242);\n"
                                                  "    font-size: 14px;\n"
                                                  "    border-radius: 3px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover{\n"
                                                  "background-color: rgba(200, 200, 200, 128);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed{\n"
                                                  "background-color: rgba(255, 255, 255, 128);\n"
                                                  "}")
        self.btn_view_STOP_PROD_APP.setText("")
        self.btn_view_STOP_PROD_APP.setIcon(icon)
        self.btn_view_STOP_PROD_APP.setObjectName("btn_view_STOP_PROD_APP")
        self.horizontalLayout_21.addWidget(self.btn_view_STOP_PROD_APP)
        self.btn_copy_STOP_PROD_APP = QtWidgets.QPushButton(self.frame_action_STOP_PROD_APP)
        self.btn_copy_STOP_PROD_APP.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_copy_STOP_PROD_APP.setMaximumSize(QtCore.QSize(100, 30))
        self.btn_copy_STOP_PROD_APP.setBaseSize(QtCore.QSize(0, 30))
        self.btn_copy_STOP_PROD_APP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_copy_STOP_PROD_APP.setStyleSheet("QPushButton{\n"
                                                  "    border: 1px solid rgb(167, 167, 167);\n"
                                                  "    background: rgb(242, 242, 242);\n"
                                                  "    font-size: 14px;\n"
                                                  "    border-radius: 3px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover{\n"
                                                  "background-color: rgba(200, 200, 200, 128);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed{\n"
                                                  "background-color: rgba(255, 255, 255, 128);\n"
                                                  "}\n"
                                                  "")
        self.btn_copy_STOP_PROD_APP.setIcon(icon1)
        self.btn_copy_STOP_PROD_APP.setObjectName("btn_copy_STOP_PROD_APP")
        self.horizontalLayout_21.addWidget(self.btn_copy_STOP_PROD_APP)
        self.verticalLayout_4.addWidget(self.frame_action_STOP_PROD_APP)
        self.verticalLayout_7.addWidget(self.groupBox_STOP_PROD_APP)
        self.groupBox_START_PROD_WF = QtWidgets.QGroupBox(self.frame_START)
        self.groupBox_START_PROD_WF.setStyleSheet("QGroupBox{\n"
                                                  "    border: 1px solid rgb(137, 137, 137);\n"
                                                  "    border-radius: 5px;\n"
                                                  "    background-color: rgb(237, 237, 237);\n"
                                                  "}")
        self.groupBox_START_PROD_WF.setObjectName("groupBox_START_PROD_WF")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_START_PROD_WF)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_title_START_PROD_WF = QtWidgets.QFrame(self.groupBox_START_PROD_WF)
        self.frame_title_START_PROD_WF.setObjectName("frame_title_START_PROD_WF")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_title_START_PROD_WF)
        self.horizontalLayout_18.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.lbl_icon_START_PROD_WF_0 = QtWidgets.QLabel(self.frame_title_START_PROD_WF)
        self.lbl_icon_START_PROD_WF_0.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_WF_0.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_WF_0.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_WF_0.setStyleSheet("QLabel{\n"
                                                    "    padding-left: 7px;\n"
                                                    "}")
        self.lbl_icon_START_PROD_WF_0.setText("")
        self.lbl_icon_START_PROD_WF_0.setPixmap(QtGui.QPixmap(":/img/img/WF.png"))
        self.lbl_icon_START_PROD_WF_0.setObjectName("lbl_icon_START_PROD_WF_0")
        self.horizontalLayout_18.addWidget(self.lbl_icon_START_PROD_WF_0)
        self.lbl_icon_START_PROD_WF_2 = QtWidgets.QLabel(self.frame_title_START_PROD_WF)
        self.lbl_icon_START_PROD_WF_2.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_WF_2.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_WF_2.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_WF_2.setStyleSheet("QLabel{\n"
                                                    "    padding-left: 7px;\n"
                                                    "}")
        self.lbl_icon_START_PROD_WF_2.setText("")
        self.lbl_icon_START_PROD_WF_2.setPixmap(QtGui.QPixmap(":/img/img/prod.png"))
        self.lbl_icon_START_PROD_WF_2.setObjectName("lbl_icon_START_PROD_WF_2")
        self.horizontalLayout_18.addWidget(self.lbl_icon_START_PROD_WF_2)
        self.lbl_icon_START_PROD_WF_1 = QtWidgets.QLabel(self.frame_title_START_PROD_WF)
        self.lbl_icon_START_PROD_WF_1.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_WF_1.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_WF_1.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_PROD_WF_1.setStyleSheet("QLabel{\n"
                                                    "    padding-left: 7px;\n"
                                                    "}")
        self.lbl_icon_START_PROD_WF_1.setText("")
        self.lbl_icon_START_PROD_WF_1.setPixmap(QtGui.QPixmap(":/img/img/start.png"))
        self.lbl_icon_START_PROD_WF_1.setObjectName("lbl_icon_START_PROD_WF_1")
        self.horizontalLayout_18.addWidget(self.lbl_icon_START_PROD_WF_1)
        self.lbl_title_START_PROD_WF = QtWidgets.QLabel(self.frame_title_START_PROD_WF)
        self.lbl_title_START_PROD_WF.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_title_START_PROD_WF.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lbl_title_START_PROD_WF.setBaseSize(QtCore.QSize(0, 30))
        self.lbl_title_START_PROD_WF.setStyleSheet("QLabel{\n"
                                                   "    font-size: 13px;\n"
                                                   "    font-weight: 500;\n"
                                                   "}")
        self.lbl_title_START_PROD_WF.setObjectName("lbl_title_START_PROD_WF")
        self.horizontalLayout_18.addWidget(self.lbl_title_START_PROD_WF)
        self.verticalLayout_3.addWidget(self.frame_title_START_PROD_WF)
        self.frame_action_START_PROD_WF = QtWidgets.QFrame(self.groupBox_START_PROD_WF)
        self.frame_action_START_PROD_WF.setObjectName("frame_action_START_PROD_WF")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_action_START_PROD_WF)
        self.horizontalLayout_19.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.edit_START_PROD_WF = QtWidgets.QLineEdit(self.frame_action_START_PROD_WF)
        self.edit_START_PROD_WF.setMinimumSize(QtCore.QSize(0, 30))
        self.edit_START_PROD_WF.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edit_START_PROD_WF.setBaseSize(QtCore.QSize(0, 30))
        self.edit_START_PROD_WF.setStyleSheet("QLineEdit{\n"
                                              "    padding-left:3px;\n"
                                              "    border: 1px solid rgb(180, 180, 180);\n"
                                              "    border-radius: 3px;\n"
                                              "}")
        self.edit_START_PROD_WF.setReadOnly(True)
        self.edit_START_PROD_WF.setObjectName("edit_START_PROD_WF")
        self.horizontalLayout_19.addWidget(self.edit_START_PROD_WF)
        self.btn_view_START_PROD_WF = QtWidgets.QPushButton(self.frame_action_START_PROD_WF)
        self.btn_view_START_PROD_WF.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_view_START_PROD_WF.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_view_START_PROD_WF.setBaseSize(QtCore.QSize(30, 30))
        self.btn_view_START_PROD_WF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_view_START_PROD_WF.setStyleSheet("QPushButton{\n"
                                                  "    border: 1px solid rgb(167, 167, 167);\n"
                                                  "    background: rgb(242, 242, 242);\n"
                                                  "    font-size: 14px;\n"
                                                  "    border-radius: 3px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover{\n"
                                                  "background-color: rgba(200, 200, 200, 128);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed{\n"
                                                  "background-color: rgba(255, 255, 255, 128);\n"
                                                  "}")
        self.btn_view_START_PROD_WF.setText("")
        self.btn_view_START_PROD_WF.setIcon(icon)
        self.btn_view_START_PROD_WF.setObjectName("btn_view_START_PROD_WF")
        self.horizontalLayout_19.addWidget(self.btn_view_START_PROD_WF)
        self.btn_copy_START_PROD_WF = QtWidgets.QPushButton(self.frame_action_START_PROD_WF)
        self.btn_copy_START_PROD_WF.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_copy_START_PROD_WF.setMaximumSize(QtCore.QSize(100, 30))
        self.btn_copy_START_PROD_WF.setBaseSize(QtCore.QSize(0, 30))
        self.btn_copy_START_PROD_WF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_copy_START_PROD_WF.setStyleSheet("QPushButton{\n"
                                                  "    border: 1px solid rgb(167, 167, 167);\n"
                                                  "    background: rgb(242, 242, 242);\n"
                                                  "    font-size: 14px;\n"
                                                  "    border-radius: 3px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover{\n"
                                                  "background-color: rgba(200, 200, 200, 128);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed{\n"
                                                  "background-color: rgba(255, 255, 255, 128);\n"
                                                  "}\n"
                                                  "")
        self.btn_copy_START_PROD_WF.setIcon(icon1)
        self.btn_copy_START_PROD_WF.setObjectName("btn_copy_START_PROD_WF")
        self.horizontalLayout_19.addWidget(self.btn_copy_START_PROD_WF)
        self.verticalLayout_3.addWidget(self.frame_action_START_PROD_WF)
        self.verticalLayout_7.addWidget(self.groupBox_START_PROD_WF)
        self.groupBox_START_TEST_WF = QtWidgets.QGroupBox(self.frame_START)
        self.groupBox_START_TEST_WF.setStyleSheet("QGroupBox{\n"
                                                  "    border: 1px solid rgb(137, 137, 137);\n"
                                                  "    border-radius: 5px;\n"
                                                  "    background-color: rgb(237, 237, 237);\n"
                                                  "}")
        self.groupBox_START_TEST_WF.setObjectName("groupBox_START_TEST_WF")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_START_TEST_WF)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_title_START_TEST_WF = QtWidgets.QFrame(self.groupBox_START_TEST_WF)
        self.frame_title_START_TEST_WF.setObjectName("frame_title_START_TEST_WF")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_title_START_TEST_WF)
        self.horizontalLayout_14.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lbl_icon_START_TEST_WF_0 = QtWidgets.QLabel(self.frame_title_START_TEST_WF)
        self.lbl_icon_START_TEST_WF_0.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_TEST_WF_0.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_TEST_WF_0.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_TEST_WF_0.setStyleSheet("QLabel{\n"
                                                    "    padding-left: 7px;\n"
                                                    "}")
        self.lbl_icon_START_TEST_WF_0.setText("")
        self.lbl_icon_START_TEST_WF_0.setPixmap(QtGui.QPixmap(":/img/img/WF.png"))
        self.lbl_icon_START_TEST_WF_0.setObjectName("lbl_icon_START_TEST_WF_0")
        self.horizontalLayout_14.addWidget(self.lbl_icon_START_TEST_WF_0)
        self.lbl_icon_START_TEST_WF_2 = QtWidgets.QLabel(self.frame_title_START_TEST_WF)
        self.lbl_icon_START_TEST_WF_2.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_TEST_WF_2.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_TEST_WF_2.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_TEST_WF_2.setStyleSheet("QLabel{\n"
                                                    "    padding-left: 7px;\n"
                                                    "}")
        self.lbl_icon_START_TEST_WF_2.setText("")
        self.lbl_icon_START_TEST_WF_2.setPixmap(QtGui.QPixmap(":/img/img/test.png"))
        self.lbl_icon_START_TEST_WF_2.setObjectName("lbl_icon_START_TEST_WF_2")
        self.horizontalLayout_14.addWidget(self.lbl_icon_START_TEST_WF_2)
        self.lbl_icon_START_TEST_WF_1 = QtWidgets.QLabel(self.frame_title_START_TEST_WF)
        self.lbl_icon_START_TEST_WF_1.setMinimumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_TEST_WF_1.setMaximumSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_TEST_WF_1.setBaseSize(QtCore.QSize(30, 30))
        self.lbl_icon_START_TEST_WF_1.setStyleSheet("QLabel{\n"
                                                    "    padding-left: 7px;\n"
                                                    "}")
        self.lbl_icon_START_TEST_WF_1.setText("")
        self.lbl_icon_START_TEST_WF_1.setPixmap(QtGui.QPixmap(":/img/img/start.png"))
        self.lbl_icon_START_TEST_WF_1.setObjectName("lbl_icon_START_TEST_WF_1")
        self.horizontalLayout_14.addWidget(self.lbl_icon_START_TEST_WF_1)
        self.lbl_title_START_TEST_WF = QtWidgets.QLabel(self.frame_title_START_TEST_WF)
        self.lbl_title_START_TEST_WF.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_title_START_TEST_WF.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lbl_title_START_TEST_WF.setBaseSize(QtCore.QSize(0, 30))
        self.lbl_title_START_TEST_WF.setStyleSheet("QLabel{\n"
                                                   "    font-size: 13px;\n"
                                                   "    font-weight: 500;\n"
                                                   "}")
        self.lbl_title_START_TEST_WF.setObjectName("lbl_title_START_TEST_WF")
        self.horizontalLayout_14.addWidget(self.lbl_title_START_TEST_WF)
        self.verticalLayout_2.addWidget(self.frame_title_START_TEST_WF)
        self.frame_action_START_TEST_WF = QtWidgets.QFrame(self.groupBox_START_TEST_WF)
        self.frame_action_START_TEST_WF.setObjectName("frame_action_START_TEST_WF")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_action_START_TEST_WF)
        self.horizontalLayout_15.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.edit_START_TEST_WF = QtWidgets.QLineEdit(self.frame_action_START_TEST_WF)
        self.edit_START_TEST_WF.setMinimumSize(QtCore.QSize(0, 30))
        self.edit_START_TEST_WF.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edit_START_TEST_WF.setBaseSize(QtCore.QSize(0, 30))
        self.edit_START_TEST_WF.setStyleSheet("QLineEdit{\n"
                                              "    padding-left:3px;\n"
                                              "    border: 1px solid rgb(180, 180, 180);\n"
                                              "    border-radius: 3px;\n"
                                              "}")
        self.edit_START_TEST_WF.setReadOnly(True)
        self.edit_START_TEST_WF.setObjectName("edit_START_TEST_WF")
        self.horizontalLayout_15.addWidget(self.edit_START_TEST_WF)
        self.btn_view_START_TEST_WF = QtWidgets.QPushButton(self.frame_action_START_TEST_WF)
        self.btn_view_START_TEST_WF.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_view_START_TEST_WF.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_view_START_TEST_WF.setBaseSize(QtCore.QSize(30, 30))
        self.btn_view_START_TEST_WF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_view_START_TEST_WF.setStyleSheet("QPushButton{\n"
                                                  "    border: 1px solid rgb(167, 167, 167);\n"
                                                  "    background: rgb(242, 242, 242);\n"
                                                  "    font-size: 14px;\n"
                                                  "    border-radius: 3px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover{\n"
                                                  "background-color: rgba(200, 200, 200, 128);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed{\n"
                                                  "background-color: rgba(255, 255, 255, 128);\n"
                                                  "}")
        self.btn_view_START_TEST_WF.setText("")
        self.btn_view_START_TEST_WF.setIcon(icon)
        self.btn_view_START_TEST_WF.setObjectName("btn_view_START_TEST_WF")
        self.horizontalLayout_15.addWidget(self.btn_view_START_TEST_WF)
        self.btn_copy_START_TEST_WF = QtWidgets.QPushButton(self.frame_action_START_TEST_WF)
        self.btn_copy_START_TEST_WF.setMinimumSize(QtCore.QSize(100, 30))
        self.btn_copy_START_TEST_WF.setMaximumSize(QtCore.QSize(100, 30))
        self.btn_copy_START_TEST_WF.setBaseSize(QtCore.QSize(0, 30))
        self.btn_copy_START_TEST_WF.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_copy_START_TEST_WF.setStyleSheet("QPushButton{\n"
                                                  "    border: 1px solid rgb(167, 167, 167);\n"
                                                  "    background: rgb(242, 242, 242);\n"
                                                  "    font-size: 14px;\n"
                                                  "    border-radius: 3px;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover{\n"
                                                  "background-color: rgba(200, 200, 200, 128);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed{\n"
                                                  "background-color: rgba(255, 255, 255, 128);\n"
                                                  "}\n"
                                                  "")
        self.btn_copy_START_TEST_WF.setIcon(icon1)
        self.btn_copy_START_TEST_WF.setObjectName("btn_copy_START_TEST_WF")
        self.horizontalLayout_15.addWidget(self.btn_copy_START_TEST_WF)
        self.verticalLayout_2.addWidget(self.frame_action_START_TEST_WF)
        self.verticalLayout_7.addWidget(self.groupBox_START_TEST_WF)
        self.verticalLayout_8.addWidget(self.frame_START)
        self.setCentralWidget(self.widget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self._retranslateUi()
        self._set_texts()
        QtCore.QMetaObject.connectSlotsByName(self)

    def _retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Команды запуска"))
        self.lbl_text_DMN.setText(_translate("MainWindow", "DMN:"))
        self.lbl_text_DIS.setText(_translate("MainWindow", "DIS:"))
        self.lbl_text_APP.setText(_translate("MainWindow", "APP:"))
        self.lbl_text_WF.setText(_translate("MainWindow", "WF:"))
        self.lbl_text_PS.setText(_translate("MainWindow", "PS:"))
        self.lbl_title_START_JOB.setText(_translate("MainWindow", "Запуск JOB"))
        self.lbl_title_START_PROD_APP.setText(_translate("MainWindow", "Запуск APP прод"))
        self.lbl_title_START_PROD_WF.setText(_translate("MainWindow", "Запуск WF прод"))
        self.lbl_title_STOP_PROD_APP.setText(_translate("MainWindow", "Стоп APP прод"))
        self.lbl_title_START_TEST_WF.setText(_translate("MainWindow", "Запуск WF тест"))
        self.btn_copy_START_JOB.setText(_translate("MainWindow", "Copy"))
        self.btn_copy_START_PROD_APP.setText(_translate("MainWindow", "Copy"))
        self.btn_copy_START_PROD_WF.setText(_translate("MainWindow", "Copy"))
        self.btn_copy_STOP_PROD_APP.setText(_translate("MainWindow", "Copy"))
        self.btn_copy_START_TEST_WF.setText(_translate("MainWindow", "Copy"))

    def _set_texts(self):
        _translate = QtCore.QCoreApplication.translate

        self.edit_START_JOB.setText(_translate("MainWindow", ' '.join(self._start_job__array)))
        self.edit_START_JOB.setCursorPosition(0)

        self.edit_START_PROD_APP.setText(_translate("MainWindow", ' '.join(self._start_prod_app__array)))
        self.edit_START_PROD_APP.setCursorPosition(0)

        self.edit_STOP_PROD_APP.setText(_translate("MainWindow", ' '.join(self._stop_prod_app__array)))
        self.edit_STOP_PROD_APP.setCursorPosition(0)

        self.edit_START_PROD_WF.setText(_translate("MainWindow", ' '.join(self._start_prod_wf__array)))
        self.edit_START_PROD_WF.setCursorPosition(0)

        self.edit_START_TEST_WF.setText(_translate("MainWindow", ' '.join(self._start_test_wf__array)))
        self.edit_START_TEST_WF.setCursorPosition(0)

    def _connect_event(self):
        self.btn_copy_START_JOB.clicked.connect(lambda: self._clicked_btn_copy(
            self.edit_START_JOB.text(), "Запуск JOB"
        ))
        self.btn_copy_START_PROD_APP.clicked.connect(lambda: self._clicked_btn_copy(
            self.edit_START_PROD_APP.text(), "Запуск APP прод"
        ))
        self.btn_copy_START_PROD_WF.clicked.connect(lambda: self._clicked_btn_copy(
            self.edit_START_PROD_WF.text(), "Запуск WF прод"
        ))
        self.btn_copy_STOP_PROD_APP.clicked.connect(lambda: self._clicked_btn_copy(
            self.edit_STOP_PROD_APP.text(), "Запуск APP тест"
        ))
        self.btn_copy_START_TEST_WF.clicked.connect(lambda: self._clicked_btn_copy(
            self.edit_START_TEST_WF.text(), "Запуск WF тест"
        ))

        self.btn_view_START_JOB.clicked.connect(lambda: self._clicked_btn_view(
            self.edit_START_JOB.text(), "Запуск JOB"
        ))
        self.btn_view_START_PROD_APP.clicked.connect(lambda: self._clicked_btn_view(
            self.edit_START_PROD_APP.text(), "Запуск APP прод"
        ))
        self.btn_view_START_PROD_WF.clicked.connect(lambda: self._clicked_btn_view(
            self.edit_START_PROD_WF.text(), "Запуск WF прод"
        ))
        self.btn_view_STOP_PROD_APP.clicked.connect(lambda: self._clicked_btn_view(
            self.edit_STOP_PROD_APP.text(), "Запуск APP тест"
        ))
        self.btn_view_START_TEST_WF.clicked.connect(lambda: self._clicked_btn_view(
            self.edit_START_TEST_WF.text(), "Запуск WF тест"
        ))

        #
        self.edit_DMN.textChanged.connect(self._change_edit_dmn)
        self.edit_DMN.editingFinished.connect(self._edit_finish_edit_dmn)

        self.edit_DIS.textChanged.connect(self._change_edit_dis)
        self.edit_DIS.editingFinished.connect(self._edit_finish_edit_dis)

        self.edit_APP.textChanged.connect(self._change_edit_app)
        self.edit_APP.editingFinished.connect(self._edit_finish_edit_app)

        self.edit_WF.textChanged.connect(self._change_edit_wf)
        self.edit_WF.editingFinished.connect(self._edit_finish_edit_wf)

        self.edit_PS.textChanged.connect(self._change_edit_ps)
        self.edit_PS.editingFinished.connect(self._edit_finish_edit_ps)

    def _clicked_btn_copy(self, text, status):
        pyperclip.copy(text)
        self.statusbar.showMessage(f"{status} - скопирован", 3000)

    def _clicked_btn_view(self, text, title):
        dialog = UiDialogText(text=text, title=title)
        dialog.setModal(True)
        dialog.exec_()

    @staticmethod
    def _event_change_text(elem_in, elem_out, array, param, index_params, prefix):
        array[index_params[param]] = f"{prefix[param]} {elem_in.text()}"
        elem_out.setText(' '.join(array))

    def _change_edit_dmn(self):
        # пример
        # self._start_job__array[self._start_job__index_params['_param_dmn']] = f"{self._prefix_start_job['_param_dmn']} {self.edit_DMN.text()}"
        # self.edit_START_JOB.setText(' '.join(self._start_job__array))

        elements_change = (
            {
                "elem_in": self.edit_DMN, "elem_out": self.edit_START_JOB,
                "array": self._start_job__array,
                "param": '_param_dmn', "index_params": self._start_job__index_params,
                "prefix": self._start_job__prefix
            },
            {
                "elem_in": self.edit_DMN, "elem_out": self.edit_START_PROD_APP,
                "array": self._start_prod_app__array,
                "param": '_param_dmn', "index_params": self._start_prod_app__index_param,
                "prefix": self._start_prod_app__prefix
            },
            {
                "elem_in": self.edit_DMN, "elem_out": self.edit_STOP_PROD_APP,
                "array": self._stop_prod_app__array,
                "param": '_param_dmn', "index_params": self._stop_prod_app__index_param,
                "prefix": self._stop_prod_app__prefix
            },
            {
                "elem_in": self.edit_DMN, "elem_out": self.edit_START_PROD_WF,
                "array": self._start_prod_wf__array,
                "param": '_param_dmn', "index_params": self._start_prod_wf__index_param,
                "prefix": self._start_prod_wf__prefix
            },
            {
                "elem_in": self.edit_DMN, "elem_out": self.edit_START_TEST_WF,
                "array": self._start_test_wf__array,
                "param": '_param_dmn', "index_params": self._start_test_wf__index_param,
                "prefix": self._start_test_wf__prefix
            },
        )

        for elem in elements_change:
            self._event_change_text(**elem)

    def _edit_finish_edit_dmn(self):
        pass

    def _change_edit_dis(self):
        elements_change = (
            {
                "elem_in": self.edit_DIS, "elem_out": self.edit_START_JOB,
                "array": self._start_job__array,
                "param": '_param_dis', "index_params": self._start_job__index_params,
                "prefix": self._start_job__prefix
            },
            {
                "elem_in": self.edit_DIS, "elem_out": self.edit_START_PROD_APP,
                "array": self._start_prod_app__array,
                "param": '_param_dis', "index_params": self._start_prod_app__index_param,
                "prefix": self._start_prod_app__prefix
            },
            {
                "elem_in": self.edit_DIS, "elem_out": self.edit_STOP_PROD_APP,
                "array": self._stop_prod_app__array,
                "param": '_param_dis', "index_params": self._stop_prod_app__index_param,
                "prefix": self._stop_prod_app__prefix
            },
            {
                "elem_in": self.edit_DIS, "elem_out": self.edit_START_PROD_WF,
                "array": self._start_prod_wf__array,
                "param": '_param_dis', "index_params": self._start_prod_wf__index_param,
                "prefix": self._start_prod_wf__prefix
            },
            {
                "elem_in": self.edit_DIS, "elem_out": self.edit_START_TEST_WF,
                "array": self._start_test_wf__array,
                "param": '_param_dis', "index_params": self._start_test_wf__index_param,
                "prefix": self._start_test_wf__prefix
            },
        )

        for elem in elements_change:
            self._event_change_text(**elem)

    def _edit_finish_edit_dis(self):
        pass

    def _change_edit_app(self):
        elements_change = (
            {
                "elem_in": self.edit_APP, "elem_out": self.edit_START_JOB,
                "array": self._start_job__array,
                "param": '_param_app', "index_params": self._start_job__index_params,
                "prefix": self._start_job__prefix
            },
            {
                "elem_in": self.edit_APP, "elem_out": self.edit_START_PROD_APP,
                "array": self._start_prod_app__array,
                "param": '_param_app', "index_params": self._start_prod_app__index_param,
                "prefix": self._start_prod_app__prefix
            },
            {
                "elem_in": self.edit_APP, "elem_out": self.edit_STOP_PROD_APP,
                "array": self._stop_prod_app__array,
                "param": '_param_app', "index_params": self._stop_prod_app__index_param,
                "prefix": self._stop_prod_app__prefix
            },
            {
                "elem_in": self.edit_APP, "elem_out": self.edit_START_PROD_WF,
                "array": self._start_prod_wf__array,
                "param": '_param_app', "index_params": self._start_prod_wf__index_param,
                "prefix": self._start_prod_wf__prefix
            },
            {
                "elem_in": self.edit_APP, "elem_out": self.edit_START_TEST_WF,
                "array": self._start_test_wf__array,
                "param": '_param_app', "index_params": self._start_test_wf__index_param,
                "prefix": self._start_test_wf__prefix
            },
        )

        for elem in elements_change:
            self._event_change_text(**elem)

    def _edit_finish_edit_app(self):
        pass

    def _change_edit_wf(self):
        elements_change = (
            {
                "elem_in": self.edit_WF, "elem_out": self.edit_START_JOB,
                "array": self._start_job__array,
                "param": '_param_wf', "index_params": self._start_job__index_params,
                "prefix": self._start_job__prefix
            },
            {
                "elem_in": self.edit_WF, "elem_out": self.edit_START_PROD_WF,
                "array": self._start_prod_wf__array,
                "param": '_param_wf', "index_params": self._start_prod_wf__index_param,
                "prefix": self._start_prod_wf__prefix
            },
            {
                "elem_in": self.edit_WF, "elem_out": self.edit_START_TEST_WF,
                "array": self._start_test_wf__array,
                "param": '_param_wf', "index_params": self._start_test_wf__index_param,
                "prefix": self._start_test_wf__prefix
            },
        )

        for elem in elements_change:
            self._event_change_text(**elem)

    def _edit_finish_edit_wf(self):
        pass

    def _change_edit_ps(self):
        elements_change = (
            {
                "elem_in": self.edit_PS, "elem_out": self.edit_START_JOB,
                "array": self._start_job__array,
                "param": '_param_ps', "index_params": self._start_job__index_params,
                "prefix": self._start_job__prefix
            },
            {
                "elem_in": self.edit_PS, "elem_out": self.edit_START_PROD_WF,
                "array": self._start_prod_wf__array,
                "param": '_param_ps', "index_params": self._start_prod_wf__index_param,
                "prefix": self._start_prod_wf__prefix
            },
            {
                "elem_in": self.edit_PS, "elem_out": self.edit_START_TEST_WF,
                "array": self._start_test_wf__array,
                "param": '_param_ps', "index_params": self._start_test_wf__index_param,
                "prefix": self._start_test_wf__prefix
            },
        )

        for elem in elements_change:
            self._event_change_text(**elem)

    def _edit_finish_edit_ps(self):
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    ui = UiMainWindow()
    ui.show()
    sys.exit(app.exec_())
