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
        self.questionBank = [
            "So, you've got an awesome idea for a website?",
            "Do you have any web related skills?",
            "What can you do?",
            "Sweet! Your're ready to build a site!",
            "Hold it. Just cuz you have the skill, doesn't mean ya got the chops.",
            "What's your idea of good code?",
            "Great. What's your idea of good design?",
            "Great. What's your idea of a good social media strategy?",
            "Are you willing to learn?"
        ]
        self.textBank = [
            ["Sure do!", "Nope.", None, None, None],
            ["Nope.", "I know a little dreamweaver!", "Yeah totally.", None, None],
            ["I can code!", "I can design!", "I'm a social media genius!", None, None],
            ["Nice!", None, None, None, None],
            ["Huh?", None, None, None, None],
            ["Naming variables after my pets.", "Copy and paste from Stack Overflow.", "Lots and lots of nested tables.", "Scalable, well-commented. seamlessly integrated", None],
            ["Rounded corners and plenty of gloss.", "The more fonts, the merrier.", "I dream of geocities.", "Starbursts and drop shadows.", "Clear hierarchy, beautiful interactions, thoughtful styling"],
            ["Finding and seeding brand content in appropriate channels.", "Building engaging conversations around my launch.", "Just feel every page with share buttons.", "Spamming followers with sponsored links.", "Making lots of twitter accounts to retweet myself."],
            []
        ]
        self.buttonBank = [
            [True, True, False, False, False],
            [True, True, True, False, False],
            [True, True, True, False, False],
            [True, False, False, False, False],
            [True, False, False, False, False],
            [True, True, True, True, False],
            [True, True, True, True, True],
            [True, True, True, True, True]
        ]
        self.responses = [
            ["(answer 1 1 \"Sure do!\")", "(answer 1 2 \"Nope.\")", None, None, None],
            ["(answer 2 1 \"Nope.\")", "(answer 2 2 \"I know a little dreamweaver!\")", "(answer 2 3 \"Yeah totally.\")", None, None],
            ["(answer 3 1 \"I can design!\")", "(answer 3 2 \"I can code!\")", "(answer 3 3 \"I'm a social media genius!\")", None, None],
            ["(answer 4 1 \"Nice!\")", None, None, None, None],
            ["(answer 5 1 \"Huh?\")", None, None, None, None],
            ["(answer 6 1 \"Naming variables after my pets.\")", "(answer 6 2 \"Copy and paste from Stack Overflow.\")", "(answer 6 3 \"Lots and lots of nested tables.\")", "(answer 6 4 \"Scalable, well-commented. seamlessly integrated\")", None],
            ["(answer 7 1 \"Rounded corners and plenty of gloss.\")", "(answer 7 2 \"The more fonts, the merrier.\")", "(answer 7 3 \"I dream of geocities.\")", "(answer 7 4 \"Starbursts and drop shadows.\")", "(answer 7 5 \"Clear hierarchy, beautiful interactions, thoughtful styling.\")"],
            ["(answer 8 1 \"Finding and seeding brand content in appropriate channels.\")", "(answer 8 2 \"Building engaging conversations around my launch.\")", "(answer 8 3 \"Just feel every page with share buttons.\")", "(answer 8 4 \"Spamming followers with sponsored links.\")", "(answer 8 5 \"Making lots of twitter accounts to retweet myself.\")"]
        ]
        self.results = [
            "No idea, no dice.",
            "Whoa, that's oldschool! Sounds like it's time for an update.",
            "Yeah. You're gonna need a developer.",
            "We're not letting you anywhere near photoshop.",
            "We're not convinced you know what social media is.",
            "You look great! Go forth with your website brave one!"
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

        self.text = QtWidgets.QLabel(self.questionBank[self.state], alignment=QtCore.Qt.AlignCenter)
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
        self.updateButtons()
        self.text.setText(self.questionBank[self.state])
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
            if f == "question":
                self.changeState(fact[0]-1)
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