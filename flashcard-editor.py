# %%

import json
import sys

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget

# %%

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.define_page_layout()

    def get_unique_identifier(self):
        self.load()
        self.df = pd.DataFrame(self.data['cards'])
        max_index = pd.to_numeric(self.df['index']).max()
        return str(max_index + 1)

    def load(self):
        self.data = json.load(open(self.inputSavePath.text()))

    def append_data(self):
        list_cards = self.data['cards']

        dict_currentcard = dict()
        dict_currentcard['name'] = self.inputPrompt.toPlainText()
        dict_currentcard['answer'] = self.inputAnswer.toPlainText()
        dict_currentcard['index'] = self.get_unique_identifier()

        list_cards.append(dict_currentcard)
        self.data['cards'] = list_cards

    def save(self):
        self.load()
        self.append_data()
        json.dump(self.data, open(self.inputSavePath.text(), 'w'))
        self.inputPrompt.setText("")
        self.inputAnswer.setText("")

    def define_page_layout(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("flashcard-editor")

        self.buttonSave = QtWidgets.QPushButton(self)
        self.buttonSave.setText("Save")
        self.buttonSave.clicked.connect(self.save)

        self.inputPrompt = QtWidgets.QTextEdit()
        self.inputPrompt.setPlainText('')
        self.labelPrompt = QtWidgets.QLabel(self)
        self.labelPrompt.setText('Prompt:')

        self.inputAnswer = QtWidgets.QTextEdit()
        self.inputAnswer.setPlainText('')
        self.labelAnswer = QtWidgets.QLabel(self)
        self.labelAnswer.setText('Answer:')

        self.inputSavePath = QtWidgets.QLineEdit()
        self.inputSavePath.setText('flashcards.json')
        self.labelSavePath = QtWidgets.QLabel(self)
        self.labelSavePath.setText('Save Path:')

        self.layout_page = QVBoxLayout()
        self.layout_inputs = QVBoxLayout()
        self.layout_saveui = QHBoxLayout()

        self.layout_page.addLayout(self.layout_inputs)
        self.layout_page.addLayout(self.layout_saveui)

        self.layout_inputs.addWidget(self.labelPrompt)
        self.layout_inputs.addWidget(self.inputPrompt)
        self.layout_inputs.addWidget(self.labelAnswer)
        self.layout_inputs.addWidget(self.inputAnswer)

        self.layout_saveui.addWidget(self.buttonSave)
        self.layout_saveui.addWidget(self.labelSavePath)
        self.layout_saveui.addWidget(self.inputSavePath)

        self.layout_inputs.setContentsMargins(10, 10, 10, 10)
        self.layout_page.setContentsMargins(10, 10, 10, 10)

        self.layout_inputs.setSpacing(20)
        self.layout_page.setSpacing(20)

        widget = QWidget()
        widget.setLayout(self.layout_page)
        self.setCentralWidget(widget)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


# %%

window()

# %%
