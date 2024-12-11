import sys
import clips
from PySide6 import QtCore, QtWidgets, QtGui
def setup():
    env = clips.Environment()
    # # TODO: add proper rules
    # rules = ""
    # # TODO: add proper facts
    # facts = ""
    # with open("rules.clp", 'r') as f:
    #     for line in f.readlines():
    #         rules += line
    # with open("facts.clp", 'r') as f:
    #     for line in f.readlines():
    #         facts += line
    # env.build(rules)
    env.load("rules.clp")
    # env.build(facts)
    env.load("facts.clp")
    env.reset()
    return env


class MyWidget(QtWidgets.QWidget):

    def __init__(self, newEnv):
        super().__init__()
        self.env = newEnv
        self.state = 0
        self.finished = 0
        self.textBank = [
            ["Sure do!", "Nope.", None, None, None]
        ]
        self.buttonBank = [
            [True, True, False, False, False]
        ]
        self.responses = [
            ["(answer 1 1 \"Sure do!\")", "(answer 1 2 \"Nope.\")", None, None, None]
        ]
        self.results = [
            "No idea, no dice."
        ]
        self.finalButtons = [
            ["Ok.", "Go again.", None, None, None],
            [True, True, False, False, False]
        ]

        self.answers = self.textBank[self.state]
        self.buttonStates = []
        self.currentResponse = []
        self.allButtons = [
            QtWidgets.QPushButton("1"),
            QtWidgets.QPushButton("2"),
            QtWidgets.QPushButton("3"),
            QtWidgets.QPushButton("4"),
            QtWidgets.QPushButton("5")
        ]
        self.updateButtons()
        # self.button1 = QtWidgets.QPushButton("1")
        # self.button2 = QtWidgets.QPushButton("2")
        # self.button3 = QtWidgets.QPushButton("3")
        # self.button4 = QtWidgets.QPushButton("4")
        # self.button5 = QtWidgets.QPushButton("5")

        self.text = QtWidgets.QLabel("So, you've got an awesome idea for a website?", alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.allButtons[0])
        self.layout.addWidget(self.allButtons[1])
        self.layout.addWidget(self.allButtons[2])
        self.layout.addWidget(self.allButtons[3])
        self.layout.addWidget(self.allButtons[4])

        self.allButtons[0].clicked.connect(lambda: self.update(self.currentResponse[0]))
        self.allButtons[1].clicked.connect(lambda: self.update(self.currentResponse[1]))
        self.allButtons[2].clicked.connect(lambda: self.update(self.currentResponse[2]))
        self.allButtons[3].clicked.connect(lambda: self.update(self.currentResponse[3]))
        self.allButtons[4].clicked.connect(lambda: self.update(self.currentResponse[4]))

        # Possibly useful in the future

        # self.button1.setEnabled()
        # self.button1.setDisabled()

    @QtCore.Slot()
    def update(self, fact_string):
        if self.finished > 0: # TODO:temporary solution, delete later
            app.exit()
        self.runClipsLogic(fact_string)
        self.answers = self.textBank[self.state]
        if self.finished > 0:
            self.answers = self.finalButtons[0]
            self.currentResponse = self.finalButtons[1]
            self.text.setText(self.results[self.finished-1])
            self.updateButtons()
            # TODO: add proper exit and retry
            print("Finished!: ", self.finished)
            # app.exit()

    def nextFact(self): # for testing purposes only
        global i
        self.changeState(i)
        i += 1
        i = i % len(self.answers)
        self.text.setText(self.answers[self.state])
    def changeState(self, newState):
        self.state = newState


    def runClipsLogic(self, fact_string): # TODO: implement updating facts
        if fact_string is not None:
            self.env.assert_string(fact_string)
        for ac in self.env.activations():
            print(ac)
        self.env.run(1)
        self.answers = []
        for fact in self.env.facts():
            print(fact)
            # self.answers.append(str(fact))
            f = str(fact).split()[0][1::]
            if f == "result":
                self.finished = fact[0]

    def updateButtons(self):
        self.buttonStates = self.buttonBank[self.state]
        for i in range(5):
            self.allButtons[i].setText(self.answers[i])
            self.allButtons[i].setEnabled(self.buttonStates[i])
        self.currentResponse = self.responses[self.state]







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