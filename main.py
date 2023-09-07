# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import  time
import sys
import os
import platform
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
import cv2
import  numpy as np
import PySide6
from PySide6 import  QtCore,QtWidgets
from PySide6.QtGui import QIcon,QColor,QPixmap,QImage,QImageReader,Qt
from PySide6.QtWidgets import  QApplication,QMainWindow,QMessageBox,QPushButton,QBoxLayout,QWidget
from PySide6.QtCore import Qt,QPropertyAnimation, QRect, QEasingCurve
from modules import *
from widgets import *
from main1020 import Ui_MainWindow
from ui_main import  Ui_MainWindow as Ui_MainWindow2
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import  QUrl




os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
MUSIC_PLAY = True

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        """图像属性"""
        self.is_first_call = True       #用于自适应图片大小
        self.image = None               #图片信息
        self.image_state = "color"      #图片读入状态，默认为彩色图片
        self.image_path = None          #图片本地地址
        self.image_processed = None     #处理后的图片
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "TechXpose"
        description = "TechXpose"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.btn_message.clicked.connect(self.buttonClick)
        widgets.btn_imageprocessing.clicked.connect(self.buttonClick)
#        widgets.pushButton_open_local_file.clicked.connect(self.buttonClick)
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        """图像处理区按钮设置"""
        #渲染部分
        widgets.radioButton_color.clicked.connect(self.getRadioButtonState)
        widgets.radioButton_gray.clicked.connect(self.getRadioButtonState)
        widgets.pushButton_fileOpen.clicked.connect(self.imageReader)
        widgets.pushButton_fileSave.clicked.connect(self.imageSaver)




        """图像显示与处理区"""
        widgets.horizontalSlider_rendering_1.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_1.setValue(50)
        widgets.horizontalSlider_rendering_2.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_2.setValue(50)
        widgets.horizontalSlider_rendering_3.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_3.setValue(50)
        widgets.horizontalSlider_rendering_4.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_4.setValue(50)
        widgets.horizontalSlider_rendering_5.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_5.setValue(50)
        widgets.horizontalSlider_rendering_6.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_6.setValue(50)
        widgets.horizontalSlider_rendering_7.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_7.setValue(50)
        widgets.horizontalSlider_rendering_8.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_8.setValue(50)
        widgets.horizontalSlider_rendering_9.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_9.setValue(50)
        widgets.horizontalSlider_rendering_10.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_10.setValue(50)
        widgets.horizontalSlider_rendering_11.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_11.setValue(50)
        #widgets.label_pic_raw.setScaledContents(True)
        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        if getattr(sys, 'frozen',False):
            absPath = os.path.dirname(os.path.abspath(sys.executable))
        elif __file__:
            absPath = os.path.dirname(os.path.abspath(__file__))
        self.useCustomTheme = True
        self.absPath = absPath
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if self.useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            print("Save BTN clicked!")


        if btnName == "btn_message":
            if self.useCustomTheme:
                themeFile = os.path.abspath(os.path.join(self.absPath,"themes\py_dracula_dark.qss"))
                UIFunctions.theme(self,themeFile,True)
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = False
            else:
                themeFile = os.path.abspath(os.path.join(self.absPath, "themes\py_dracula_light.qss"))
                UIFunctions.theme(self, themeFile, True)
                AppFunctions.setThemeHack(self)
                self.useCustomTheme = True

        if btnName == "btn_imageprocessing":
            widgets.stackedWidget.setCurrentWidget(widgets.page_image)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))



        print(f'Button "{btnName}" pressed!')

    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)
        if self.is_first_call == False:
            self.updateImageSize(self.image_path)
            self.updateImageProcessed()
        if  self.is_first_call:
            self.is_first_call = False

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def getRadioButtonState(self):
        rad = self.sender()
        radName = rad.objectName()
        if radName == "radioButton_color":
            # 读取彩色图片
            self.image_state = "color"
        if radName == "radioButton_gray":
            # 读取灰度图片
            self.image_state = "gray"

    def imageReader(self):
        self.ui.lable_pic_pro.clear()
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Image', '',
                                                           'Image Files (*.png *.jpg *.bmp);;All Files (*)',
                                                           options=options)
        if file_path:
            self.image_path = file_path
            print(file_path)
            if self.image_state == "color":
                self.image = cv2.imdecode(np.fromfile(self.image_path, dtype=np.uint8), -1)
            elif self.image_state == "gray":
                self.image = cv2.imdecode(np.fromfile(self.image_path, dtype=np.uint8), 0)

            self.updateImageSize(self.image_path)
        else:
            QMessageBox.warning("错误","读取图片失败!!!")

    def imageSaver(self):
        self.image_processed = self.image
        if self.image_processed is not None:
            save_path, _ = QFileDialog.getSaveFileName(self, 'Save Image', '',
                                                       'Image Files (*.png *.jpg *.bmp);;All Files (*)')
            if save_path:
                cv2.imwrite(save_path, self.image_processed)
        else:
            QMessageBox.warning(self,"错误","图片未进行修改！！！")

    def updateImageSize(self,img_path):
        if self.image is not None:
            pixmap = QPixmap(img_path)
            self.ui.label_pic_raw.setPixmap(
                pixmap.scaled(self.ui.label_pic_raw.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    def updateImageProcessed(self):
        height, width, channel = self.image_processed.shape
        bytes_per_line = 3*width
        qt_image = QImage(self.image_processed.data,width,height,bytes_per_line,QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(qt_image)
        self.ui.lable_pic_pro.setPixmap(pixmap.scaled(self.ui.lable_pic_pro.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))


    def ImageRendering(self):
        sliderName = self.sender().objectName()
        if  sliderName == "horizontalSlider_rendering_1":
            pass
        elif sliderName == "horizontalSlider_rendering_2":
            brightness = widgets.horizontalSlider_rendering_2.value()
            # 对图像进行处理
            if self.image is not None:
                img_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
                dst = img_hsv.copy().astype(np.float32)
                dst[:, :, 2] = dst[:, :, 2] * (1 + brightness / 100)  # 亮度调整
                dst = np.clip(dst, 0, 255).astype(np.uint8)
                dst = cv2.cvtColor(dst, cv2.COLOR_HSV2BGR)
                self.image_processed = dst
                self.updateImageProcessed()


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.start_x = None
        self.start_y = None
        self.anim = None
        self.setWindowFlag(self.windowFlags() | Qt.FramelessWindowHint)  # 设置窗口标志：隐藏窗口边框
        self.primary_screen = QApplication.primaryScreen()
        self.screen_geometry = self.primary_screen.geometry()
        """self.lineEdit.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)
        self.lineEdit_2.setAttribute(QtCore.Qt.WA_MacShowFocusRect, 0)"""
        self.account = "seu"
        self.passward = "seu2023"
        if MUSIC_PLAY ==True:
            self.music_player()
        self.pushButton.clicked.connect(self.click_solution)  # 忘记密码
        self.pushButton_2.clicked.connect(self.click_solution)  # 登录
        self.pushButton_3.clicked.connect(self.click_solution)  # 注册账户
        self.pushButton_4.clicked.connect(self.click_solution)  # github登录
        self.pushButton_5.clicked.connect(self.click_solution)  # 苹果登录
        self.pushButton_6.clicked.connect(self.click_solution)  # facebook登录
        self.pushButton_7.clicked.connect(self.click_solution)  # google登录
        self.pushButton_8.clicked.connect(self.click_solution)  # 微信登录
        self.pushButton_10.clicked.connect(self.click_solution)  # 关闭窗口
        self.pushButton_11.clicked.connect(self.click_solution) #最小化窗口
        self.resize(self.screen_geometry.width(), self.screen_geometry.height())  # 主窗大小
        self.e = 1
        # 按ESC键开关

    def keyPressEvent(self, QKeyEvent):
        """快捷键"""
        if QKeyEvent.key() == Qt.Key_Escape:  # esc
            if self.e == 1:
                self.animation_exit()
            elif self.e == 0:
                self.animation_start()

    def animation_start(self):
        self.e = 1
        self.show()
        self.anim = QPropertyAnimation(self, b'geometry')  # 动画类型
        self.anim.setStartValue(
            QRect(int(self.screen_geometry.width() / 2 - 230), int(self.screen_geometry.height() / 2 - 338), 461, 676))
        self.anim.setEndValue(QRect(0, 0, int(self.screen_geometry.width()), int(self.screen_geometry.height())))
        self.anim.setDuration(400)
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        main_opacity = QPropertyAnimation(self, b"windowOpacity", self)
        main_opacity.setStartValue(0)
        main_opacity.setEndValue(1)
        main_opacity.setDuration(400)
        main_opacity.start()

        # self.anim.setLoopCount(-1)  # 设置循环旋转
        self.anim.start()

    def animation_exit(self):
        self.e = 0
        self.anim = QPropertyAnimation(self, b'geometry')  # 动画类型
        self.anim.setStartValue(QRect(0, 0, self.width(), self.height()))
        self.anim.setEndValue(
            QRect(int(self.screen_geometry.width() / 2 - 230), int(self.screen_geometry.height() / 2 - 338), 461, 676))
        self.anim.setDuration(400)
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        main_opacity = QPropertyAnimation(self, b"windowOpacity", self)
        main_opacity.setStartValue(1)
        main_opacity.setEndValue(0)
        main_opacity.setDuration(400)
        main_opacity.start()
        # self.anim.setLoopCount(-1)  # 设置循环旋转
        self.anim.start()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            super(MyMainForm, self).mousePressEvent(event)
            self.start_x = event.x()
            self.start_y = event.y()

    def mouseReleaseEvent(self, event):
        self.start_x = None
        self.start_y = None

    def mouseMoveEvent(self, event):
        try:
            super(MyMainForm, self).mouseMoveEvent(event)
            dis_x = event.x() - self.start_x
            dis_y = event.y() - self.start_y
            self.move(self.x() + dis_x, self.y() + dis_y)
        except:
            pass

    def effect_shadow_style(self, widget):
        effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        effect_shadow.setOffset(12, 12)  # 偏移
        effect_shadow.setBlurRadius(128)  # 阴影半径
        effect_shadow.setColor(QColor(155, 230, 237, 150))  # 阴影颜色
        widget.setGraphicsEffect(effect_shadow)

    def music_player(self):
        self.media_player = QMediaPlayer()

        music_url = QUrl.fromLocalFile("bgm.mp3")
        self.media_content = QMediaContent(music_url)
        self.media_player.setMedia(self.media_content)
        self.media_player.play()

    def click_solution(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "pushButton":
            QMessageBox.critical(self, "抱歉", "该功能暂时未开发")

        if btnName == "pushButton_2":
            self.open_new_window()
            """if (self.lineEdit.text() == self.account) and (self.lineEdit_2.text() == self.passward):
                self.open_new_window()

            elif self.lineEdit.text() == "":
                QMessageBox.warning(self, "警告", "请输入账号")

            elif self.lineEdit_2.text() == "":
                QMessageBox.warning(self, "警告", "请输入密码")

            else:
                QMessageBox.warning(self, "警告", "密码错误或账户不存在")
                self.lineEdit_2.clear()"""



        if btnName == "pushButton_3":
            QMessageBox.critical(self, "错误", "抱歉，该功能暂时未开发")

        if btnName == "pushButton_4":
            QMessageBox.critical(self, "错误", "抱歉，该功能暂时未开发")

        if btnName == "pushButton_5":
            QMessageBox.critical(self, "错误", "抱歉，该功能暂时未开发")

        if btnName == "pushButton_6":
            QMessageBox.critical(self, "错误", "抱歉，该功能暂时未开发")

        if btnName == "pushButton_7":
            QMessageBox.critical(self, "错误", "抱歉，该功能暂时未开发")

        if btnName == "pushButton_8":
            QMessageBox.critical(self, "错误", "抱歉，该功能暂时未开发")

        if btnName == "pushButton_10":
            self.close()

        if btnName == "pushButton_11":
            if self.e == 1:
                self.animation_exit()
            elif self.e == 0:
                self.animation_start()

    def open_new_window(self):
        self.new_window = MainWindow()
        self.new_window.show()
        self.close()


if __name__ == "__main__":



   app = QApplication(sys.argv)
   app.setWindowIcon(QIcon('logossw.png'))
   win = MyMainForm()
   win.animation_start()
   sys.exit(app.exec())
