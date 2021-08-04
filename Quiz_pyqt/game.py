import retro
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer

import numpy as np

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        #창 크기 고정
        self.setFixedSize(240, 224)
        #창 제목 설정
        self.setWindowTitle('GA-mario')

        self.env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
        self.env.reset()

        screen = self.env.get_screen()

        #타이머 생성
        self.qtimer = QTimer(self)
        #타이머에 호출할 함수 연결
        self.qtimer.timeout.connect(self.game_timer)
        #1초(=1000밀리초)마다 연결된 함수를 실행
        self.qtimer.start(1000)

        #이미지
        image = np.array(screen)
        qimage = QImage(screen, screen.shape[1], screen.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(self.screen_width, self.screen_hight, Qt.IgnoreAspectRatio)

        self.label_image.setPixmap(pixmap)

        #창 띄우기
        self.show()

    def timer(self):
        self.env.step(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0]))

        #변경된 게임 화면을 가져와서 화면에 표시
        self.update_screen()


    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_UP:
            self.press_buttons[4] = 1
        elif key == Qt.Key_Down:
            self.press_buttons[5] = 1
        elif key == Qt.Key_Down:
            self.press_buttons[6] = 1
        elif key == Qt.Key_Down:
            self.press_buttons[7] = 1
        elif key == Qt.Key_Down:
            self.press_buttons[8] = 1
        elif key == Qt.Key_Down:
            self.press_buttons[0] = 1

    def keyReleaseEvent(self, event):
        key = event.key()
        if key == Qt.Key_UP:
            self.release_buttons[4] = 0
        elif key == Qt.Key_Down:
            self.release_buttons[5] = 0
        elif key == Qt.Key_Down:
            self.release_buttons[6] = 0
        elif key == Qt.Key_Down:
            self.release_buttons[7] = 0
        elif key == Qt.Key_Down:
            self.release_buttons[8] = 0
        elif key == Qt.Key_Down:
            self.release_buttons[0] = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())