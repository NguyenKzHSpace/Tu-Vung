import sys

from PyQt6 import QtWidgets

from code_over.save_v_over import Ui_MainWindow_Save_v_over

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow_Save_v_over()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
