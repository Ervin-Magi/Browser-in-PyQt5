import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWebEngineView, QAction, QToolBar

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Browser")
        self.setGeometry(50, 50, 800, 600)

        self.view = QWebEngineView(self)
        self.view.load(QUrl("http://www.google.com"))
        self.setCentralWidget(self.view)

        # Create a toolbar and add the back, forward, and reload buttons
        self.toolbar = QToolBar(self)
        self.addToolBar(self.toolbar)

        self.back_button = QAction("Back", self)
        self.back_button.triggered.connect(self.view.back)
        self.toolbar.addAction(self.back_button)

        self.forward_button = QAction("Forward", self)
        self.forward_button.triggered.connect(self.view.forward)
        self.toolbar.addAction(self.forward_button)

        self.reload_button = QAction("Reload", self)
        self.reload_button.triggered.connect(self.view.reload)
        self.toolbar.addAction(self.reload_button)

        # disable the back button when the view can't go back
        self.view.page().backAction().setEnabled(False)
        self.view.page().backAction().triggered.connect(self.back_button.setDisabled)
        self.view.page().forwardAction().triggered.connect(self.forward_button.setEnabled)

app = QApplication(sys.argv)
browser = Browser()
browser.show()
sys.exit(app.exec_())
