import os
import sys
import configparser

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

from form_main import UiMainWindow

if getattr(sys, 'frozen', False):
    Current_Path = os.path.dirname(sys.executable)
else:
    Current_Path = str(os.path.dirname(__file__))

BIN_FOLDER = os.path.join(Current_Path, os.getcwd(), "bin")


class SaveLoadConfig:
    def __init__(self):
        self.file_ini = os.path.join(BIN_FOLDER, "account.ini")
        self.ex_config = configparser.ConfigParser()

    def save(self, exam_class):
        dict_class = {}
        for key, item in exam_class.__dict__.items():
            dict_class[key] = item

        self.ex_config[exam_class.__class__.__name__] = dict_class

        with open(self.file_ini, 'w') as configfile:
            self.ex_config.write(configfile)

    def load(self, exam_class):
        if os.path.exists(self.file_ini):
            self.ex_config.read(self.file_ini)
            for key, value in self.ex_config[exam_class.__class__.__name__].items():
                setattr(exam_class, key, value)
        else:
            self.save(exam_class)


class StartupLineTemplates:
    def __init__(self):
        self.param_dmn = "_param_dmn"
        self.param_dis = "_param_dis"
        self.param_app = "_param_app"
        self.param_wf = "_param_wf"
        self.param_ps = "_param_ps"

        self.start_job = ""
        self.start_wf_test = ""
        self.start_wf_prod = ""
        self.start_app_prod = ""
        self.stop_app_prod = ""

        self.start_job_prefix = {
            "_param_dmn": "-dn",
            "_param_dis": "-ServiceName",
            "_param_app": "-Application",
            "_param_wf": "-Workflow",
            "_param_ps": "-ParameterSet",
        }

        self.start_prod_app_prefix = {
            "_param_dmn": "-dn",
            "_param_dis": "-sn",
            "_param_app": "-a",
        }

        self.stop_prod_app_prefix = {
            "_param_dmn": "-dn",
            "_param_dis": "-sn",
            "_param_app": "-a",
        }

        self.start_prod_wf_prefix = {
            "_param_dmn": "-dn",
            "_param_dis": "-ServiceName",
            "_param_app": "-Application",
            "_param_wf": "-Workflow",
            "_param_ps": "-ParameterSet",
        }

        self.start_test_wf_prefix = {
            "_param_dmn": "-dn",
            "_param_dis": "-ServiceName",
            "_param_app": "-Application",
            "_param_wf": "-Workflow",
            "_param_ps": "-ParameterSet",
        }

        self._load_default()
        # self.load_templates()

    def _load_default(self):
        self.start_job = (
            r"C:\SQLAgentJob\IPC\bat\infacmd_proxy.bat",
            f"wfs startWorkflow",
            f"-Application {self.param_app}",
            f"-Workflow {self.param_wf}",
            f"-ParameterSet {self.param_ps}",
            f"-ServiceName {self.param_dis}",
            f"-dn {self.param_dmn}",
            f"-Wait true"
        )
        self.start_prod_app = (
            r"start C:\Informatica\10.4.1\clients\DeveloperClient\infacmd\infacmd.bat",
            f"dis StartApplication",
            f"-dn {self.param_dmn}",
            f"-sn {self.param_dis}",
            f"-un ipc_user_p",
            f"-pd ipc725p "
            f"-a {self.param_app}"
        )
        self.stop_prod_app = (
            r"start C:\Informatica\10.4.1\clients\DeveloperClient\infacmd\infacmd.bat",
            f"dis StopApplication",
            f"-dn {self.param_dmn}",
            f"-sn {self.param_dis}",
            f"-un ipc_user_p",
            f"-pd ipc725p",
            f"-a {self.param_app}"
        )
        self.start_prod_wf = (
            r"start /b C:\Informatica\10.4.1\clients\DeveloperClient\infacmd\infacmd.bat",
            f"wfs startWorkflow",
            f"-Application {self.param_app}",
            f"-Workflow {self.param_wf}",
            f"-ParameterSet {self.param_ps}",
            f"-ServiceName {self.param_dis}",
            f"-Wait false",
            f"-un ipc_user_p",
            f"-pd ipc725p",
            f"-sdn Native",
            f"-dn {self.param_dmn}"
        )
        self.start_test_wf = (
            r"start /b C:\Informatica\10.4.1\clients\DeveloperClient\infacmd\infacmd.bat",
            f"wfs startWorkflow",
            f"-Application {self.param_app}",
            f"-Workflow {self.param_wf}",
            f"-ParameterSet {self.param_ps}",
            f"-ServiceName {self.param_dis}",
            f"-Wait false",
            f"-un infa_user",
            f"-pd ipc725",
            f"-sdn Native",
            f"-dn {self.param_dmn}"
        )

    def load_templates(self):
        save_load_config = SaveLoadConfig()
        save_load_config.load(self)

    def save_templates(self):
        save_load_config = SaveLoadConfig()
        save_load_config.save(self)


class AppGeneratorCmd(QMainWindow):
    def __init__(self):
        super(AppGeneratorCmd, self).__init__()

        self.templates = StartupLineTemplates()

        self.ui = UiMainWindow(self)


if __name__ == '__main__':
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        print('running in a PyInstaller bundle')
    else:
        print('running in a normal Python process')

    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icon.ico"))
    window = AppGeneratorCmd()
    window.ui.show()

    sys.exit(app.exec_())
