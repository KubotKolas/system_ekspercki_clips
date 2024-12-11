import sys

import clips
import random
from PySide6 import QtCore, QtWidgets, QtGui
def setup():
    env = clips.Environment()
    rules = ""
    facts = ""
    with open("rules.clp", 'r') as f:
        for line in f.readlines():
            rules += line
    with open("facts.clp", 'r') as f:
        for line in f.readlines():
            facts += line
    env.build(rules)
    env.build(facts)
    env.reset()
    return env

i = 0
class MyWidget(QtWidgets.QWidget):

    state = 0
    env = None
    def __init__(self, newEnv):
        super().__init__()
        self.env = newEnv

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button1 = QtWidgets.QPushButton("Run clips")
        self.button2 = QtWidgets.QPushButton("Next fact")
        self.button3 = QtWidgets.QPushButton("Option 3")
        self.button4 = QtWidgets.QPushButton("Option 4")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)

        self.button1.clicked.connect(self.update)
        self.button2.clicked.connect(self.nextFact)
        self.button3.clicked.connect(self.update)
        self.button4.clicked.connect(self.update)

    @QtCore.Slot()
    def update(self):
        self.runClipsLogic()

    def nextFact(self):
        global i
        self.changeState(i)
        i += 1
        i = i % len(self.hello)
        self.text.setText(self.hello[self.state])
    def changeState(self, newState):
        self.state = newState


    def runClipsLogic(self):
        self.env.run()
        self.hello = []
        for fact in self.env.facts():
            print(fact, type(fact))
            for x in fact:
                print('\t', x)
            self.hello.append(str(fact))






if __name__ == "__main__":
    # setup

    env = setup()
    app = QtWidgets.QApplication()
    window = MyWidget(env)
    window.resize(800, 600)
    window.show()
    # print("run app")
    ret = app.exec()
    # print(ret)
    sys.exit(ret)