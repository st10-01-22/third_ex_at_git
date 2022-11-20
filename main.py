import sys
import sqlite3 as sq
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        coffee = self.comboBox_check.currentText()
        connect = sq.connect("coffee.db")
        cur = connect.cursor()
        ans = cur.execute("""SELECT * FROM coffee WHERE name = ?""", (coffee,)).fetchall()
        self.lineEdit_id.setText(str(ans[0][0]))
        self.lineEdit_name.setText(str(ans[0][1]))
        self.lineEdit_rotate.setText(str(ans[0][2]))
        self.lineEdit_type.setText(str(ans[0][3]))
        self.lineEdit_taste.setText(str(ans[0][4]))
        self.lineEdit_cost.setText(str(ans[0][5]))
        self.lineEdit_volume.setText(str(ans[0][6]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    style = """
            QWidget{
                background: #262D37;
            }
            QLabel{
                color: #fff;
            }
            QLineEdit{
                padding: 1px;
                color: #fff;
                border: 2px solid #fff;
                border-radius: 8px;
            }
            QPushButton{
                color: white;
                background: #0577a8;
                border: 1px #DADADA solid;
                padding: 5px 10px;
                border-radius: 2px;
                font-weight: bold;
                font-size: 9pt;
                outline: none;
            }
            QPushButton:hover{
                border: 1px #C6C6C6 solid;
                background: #0892D0;
            }
            QComboBox{
                color: white;
                background: #0577a8;
                border: 1px #DADADA solid;
                padding: 5px 10px;
                border-radius: 2px;
                font-weight: bold;
                font-size: 9pt;
                outline: none;
            }
            
        """
    app.setStyleSheet(style)
    ex = Example()
    ex.show()
    sys.exit(app.exec())