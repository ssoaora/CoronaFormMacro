from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PyQt5.QtWidgets import *
import PyQt5.QtCore
import PyQt5.QtGui
import time
import pyperclip
import random
import sys


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        id_label = QLabel('학번', self)
        id_font = id_label.font()
        id_font.setPointSize(14)
        # id_font.setFamily('Times New Roman')
        # id_label.setFont(id_font)
        id_label.move(40, 20)

        name_label = QLabel('이름', self)
        name_font = name_label.font()
        name_font.setPointSize(14)
        # name_font.setFamily('Times New Roman')
        # name_label.setFont(id_font)
        name_label.move(40, 80)

        room_label = QLabel('방 번호', self)
        room_font = room_label.font()
        room_font.setPointSize(14)
        # room_font.setFamily('Times New Roman')
        # room_label.setFont(id_font)
        room_label.move(40, 140)

        self.id_line = QLineEdit(self)
        self.id_line.move(160, 20)

        self.name_line = QLineEdit(self)
        self.name_line.move(160, 80)

        self.room_line = QLineEdit(self)
        self.room_line.move(160, 140)

        start_btn = QPushButton('설문 시작', self)
        start_btn.move(130, 200)
        start_btn.clicked.connect(self.survey)

        self.setWindowTitle('Corona Survey')
        self.move(500, 500)
        self.resize(350, 270)
        self.show()


    def survey(self):
        id = self.id_line.text()
        name = self.name_line.text()
        room = self.room_line.text()
        course = "생활관"
        temp_list = [36.1, 36.2, 36.3, 36.4, 36.5, 36.6, 36.7, 36.8]
        temperature = random.choice(temp_list)

        driver = webdriver.Chrome('C:/Temp/chromedriver.exe')
        driver.implicitly_wait(3)
        driver.get('')
        time.sleep(2)

        pyperclip.copy(f'{id}')
        driver.find_element(By.ID, 'formItem_1').find_element(By.ID, 'answer').send_keys(Keys.CONTROL, 'v')
        # time.sleep(1)

        pyperclip.copy(f'{name}')
        driver.find_element(By.ID, 'formItem_2').find_element(By.ID, 'answer').send_keys(Keys.CONTROL, 'v')
        # time.sleep(1)

        pyperclip.copy(f'{room}')
        driver.find_element(By.ID, 'formItem_5').find_element(By.ID, 'answer').send_keys(Keys.CONTROL, 'v')
        # time.sleep(1)

        out = driver.find_element(By.XPATH, '//*[@id="formItem_6"]/div/div[3]/div/div[2]/div/div[1]')
        out.click()
        # time.sleep(1)

        pyperclip.copy(f'{course}')
        driver.find_element(By.ID, 'formItem_11').find_element(By.ID, 'answer').send_keys(Keys.CONTROL, 'v')
        # time.sleep(1)

        pyperclip.copy(f'{temperature}')
        driver.find_element(By.ID, 'formItem_15').find_element(By.ID, 'answer').send_keys((Keys.CONTROL, 'v'))
        # time.sleep(1)

        symptom = driver.find_element(By.XPATH, '//*[@id="formItem_13"]/div/div[3]/div/div[9]/div/div[1]')
        symptom.click()
        # time.sleep(1)

        plus_symptom = driver.find_element(By.XPATH, '//*[@id="formItem_12"]/div/div[3]/div/div[2]/div/div[1]')
        plus_symptom.click()
        # time.sleep(1)

        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="pageNav"]/button[3]').click()

        QMessageBox.information(self, '제출 완료', '프로그램을 종료해주세요.')
        self.show()
        time.sleep(3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
