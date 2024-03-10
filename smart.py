from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox,QFileDialog,QAction )
from PyQt5.QtGui import QKeySequence

import json
import os

def writeToFile():
        with open("notes.json", "w") as file:
            json.dump(notes,file,sort_keys=True)

with open("notes.json", "r", encoding='utf=8') as file:
    notes= json.load(file)

app = QApplication([])
window = QWidget()
main_width, main_height = 800,600

text_editor=QTextEdit()
text_editor.setStyleSheet('background-color: black;')
text_editor.setPlaceholderText("Введіть текст .....")

list_widget_1 = QListWidget()
list_widget_1.setStyleSheet('background-color: red;')

list_widget_2 = QListWidget()
list_widget_2.setStyleSheet('background-color: yellow;')

text_searcher = QLineEdit()
text_searcher.setPlaceholderText("Введіть текст .... ")
text_searcher.setStyleSheet('background-color: purple;')

input_dialog = QLineEdit()
input_dialog.setPlaceholderText("Введіть тег .... ")
input_dialog.setStyleSheet('background-color: purple;')

make_note = QPushButton()
make_note.setStyleSheet('background-color: orange;')
make_note.setText("Створити замітку")

delete_note = QPushButton()
delete_note.setStyleSheet('background-color: orange;')
delete_note.setText("Видалити замітку")

save_note = QPushButton()
save_note.setStyleSheet('background-color: orange;')
save_note.setText("Зберегти замітку")

search_for_text = QPushButton()
search_for_text.setStyleSheet('background-color: orange;')
search_for_text.setText("Шукати замітку по тексту замітку")

search_for_note = QPushButton()
search_for_note.setStyleSheet('background-color: orange;')
search_for_note.setText("Шукати замітку по тегу")

add_to_note = QPushButton()
add_to_note.setStyleSheet('background-color: purple;')
add_to_note.setText("Додати до замітки")

unpin_to_note = QPushButton()
unpin_to_note.setStyleSheet('background-color: purple;')
unpin_to_note.setText("Додати до замітки")

action_theme_btn = QPushButton()
action_theme_btn.setStyleSheet('background-color: black;')

export_as_text = QPushButton()
export_as_text.setText("Конвертувати у text")

row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2 = QHBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1 = QVBoxLayout()
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel("Список запитань"))
col2.addWidget(list_widget_1)
col2.addLayout(row1)
col2.addWidget(save_note)
col2.addWidget(QLabel("Список тегів"))
col2.addWidget(list_widget_2)
col2.addWidget(input_dialog)
col2.addLayout(row2)
col2.addWidget(search_for_note)
col2.addWidget(search_for_text)
col2.addWidget(export_as_text)
col2.addWidget(action_theme_btn)

layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)






window.setStyleSheet('background-color: yellow; font-size:20px')
window.setLayout(layout_note)
window.resize(main_width, main_height)
window.show()
app.exec_()