import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QPixmap 
from PyQt5 import QtGui,QtCore 
from PyQt5.QtGui import QCursor 

widgets={
    "logo":[],
    "button":[],
    "score":[],
    "question":[],
    "answer1":[],
    "answer2":[],
    "answer3":[],
    "answer4":[],}

app = QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Wooooow")
window.setFixedWidth(1000)
#window.move(2700,200)
window.setStyleSheet("background: #161219;")

grid=QGridLayout()

def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0,len(widgets[widget])):
            widgets[widget].pop()

def start_game():
    clear_widgets()
    frame2()

def main_menu():
    clear_widgets()
    frame1()

def print_message():
    print("Hiiii")

def create_buttons(answer,l_margin,r_margin):
    button=QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(
        "*{border:4px solid #BC006C;"+
        "margin-left:"+str(l_margin)+"px;"+
        "margin-right:"+str(r_margin)+"px;"+
        "border-radius: 25px;"+
        "font-size: 16px;"+
        "color: 'white';"+
        "font-family: 'shanti';"+
        "padding: 15px 0;"+
        "margin-top: 20px;}"+
        "*:hover{background: '#BC006C';}"
    )
    button.clicked.connect(main_menu)
    return button

def frame1():
    #Display logo
    image = QPixmap("logo_cat.png").scaled(200,200,True)
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 50px;")
    widgets["logo"].append(logo)
    grid.addWidget(widgets["logo"][-1],0,0,1,2)

    #Button Widget
    button=QPushButton("Play")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border:4px solid #BC006C;"+
        "border-radius: 45px;"+
        "font-size: 35px;"+
        "color: 'white';"+
        "padding: 25px 0;"+
        "margin: 100px 200px;}"+
        "*:hover{background: '#BC006C';}"
        )
    button.clicked.connect(start_game)
    widgets["button"].append(button)
    grid.addWidget(widgets["button"][-1],1,0,1,2)

def frame2():
    score=QLabel("80")
    score.setAlignment(QtCore.Qt.AlignCenter)
    score.setStyleSheet(
        "font-size: 35px;"+
        "color:'white';"+
        "padding: 25px 20px 0px 20px;"+
        "margin: 20px 200px;"+
        "background: '#64A314';"+
        "border: 1px solid '#64A314';"+
        "border-radius: 32px;")
    widgets["score"].append(score)

    question=QLabel("Placeholder text will go here")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-size: 25px;"+
        "font-family: Shanti;"+
        "color: white;"+
        "margin: 10px 20px;"+
        "padding: 75px;")
    widgets["question"].append(question)
    grid.addWidget(widgets["score"][-1],0,1)
    grid.addWidget(widgets["question"][-1],1,0,1,2)

    button1=create_buttons("Answer 1",85,5)
    button2=create_buttons("Answer 2",5,85)
    button3=create_buttons("Answer 3",85,5)
    button4=create_buttons("Answer 4",5,85)

    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)

    grid.addWidget(widgets["answer1"][-1],2,0)
    grid.addWidget(widgets["answer2"][-1],2,1)
    grid.addWidget(widgets["answer3"][-1],3,0)
    grid.addWidget(widgets["answer4"][-1],3,1)

    cb = QComboBox()
    cb.setStyleSheet(
        "font-size: 15px;"+
        "color:'white';")
    cb.addItem("C")
    cb.addItem("C++")
    cb.addItems(["Java", "C#", "Python"])
    cb.currentIndexChanged.connect(lambda:print(cb.currentText()))
    grid.addWidget(cb)

window.setLayout(grid)
frame1()
window.show()
sys.exit(app.exec())