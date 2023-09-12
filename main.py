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
import  math
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
        self.image_processed = None     #渲染处理后的图片
        self.image_forStyle = None      #滤镜处理完的图片
        self.image_Sized = None         #裁剪完的图片

        self.image_Printed = None       #涂鸦完成的图片
        self.image_style = "Normal"     #图片的风格
        self.ChangeSize = False
        self.Changerotation = False
        self.Points = []
        self.TransformFlag = False
        self.TransformPointNum = None
        self.TransformStart = False
        self.SpecialEffect = False
        self.SpecialEffectArea = None
        self.img_transpancy = None

        self.drawing = False  # 是否开始绘制
        self.tpPointsChoose = []  # 用于存储多边形的顶点
        self.drawing = False  # 是否在绘制多边形
        self.tempFlag = False  # 是否按下右键



        widgets.lable_pic_pro.clicked.connect(self.handle_click)
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
        widgets.pushButton_fileSave_2.clicked.connect(self.imageSaver)
        widgets.pushButton_Resize.clicked.connect(self.ChangeImageSize)
        widgets.radioButton_Fangshe.clicked.connect(self.Transform)
        widgets.radioButton_Toushi.clicked.connect(self.Transform)
        widgets.radioButton_AoTou.clicked.connect(self.SpecialEffectStart)
        widgets.radioButton_TuTou.clicked.connect(self.SpecialEffectStart)
        widgets.radioButton_CaoTu.clicked.connect(self.SpecialEffectStart)
        widgets.radioButton_NONE.clicked.connect(self.SpecialEffectStart)
        widgets.pushButton_2.clicked.connect(self.AreaSpecialEffectStart)
        widgets.pushButton_3.clicked.connect(self.AreaSpecialEffectStart)
        widgets.pushButton_4.clicked.connect(self.AreaSpecialEffectStart)

        """图像显示与处理区"""
        widgets.horizontalSlider_rendering_2.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_2.setValue(50)
        widgets.horizontalSlider_rendering_4.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_4.setValue(50)
        widgets.horizontalSlider_rendering_5.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_5.setValue(50)
        widgets.horizontalSlider_rendering_6.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_6.setValue(180)
        widgets.horizontalSlider_rendering_7.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_7.setValue(50)
        widgets.horizontalSlider_rendering_8.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_8.setValue(0)
        widgets.horizontalSlider_rendering_9.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_9.setValue(0)
        widgets.horizontalSlider_rendering_10.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_10.setValue(0)
        widgets.horizontalSlider_rendering_11.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_rendering_11.setValue(0)
        widgets.horizontalSlider_Rotation.valueChanged.connect(self.ChangeImageRotation)
        widgets.horizontalSlider_Rotation.setValue(360)
        widgets.horizontalSlider_2.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_3.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_4.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_2.setValue(50)
        widgets.horizontalSlider_3.setValue(50)
        widgets.horizontalSlider_4.setValue(50)
        widgets.horizontalSlider_5.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_6.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_7.valueChanged.connect(self.ImageRendering)
        widgets.horizontalSlider_5.setValue(50)
        widgets.horizontalSlider_6.setValue(50)
        widgets.horizontalSlider_7.setValue(50)
        """风格区"""
        widgets.Button_Style_1.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_2.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_3.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_4.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_5.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_6.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_7.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_8.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_9.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_10.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_11.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_12.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_13.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_14.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_15.clicked.connect(self.ChangeImageStyle)
        widgets.Button_Style_15.setChecked(True)
        widgets.radioButton_color.setChecked(True)






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

    def handle_click(self,x,y):
        if self.TransformFlag == True:
            self.Points.append((x,y))
            if len(self.Points)==self.TransformPointNum:
                self.TransformStart = True
                self.ImageRendering()

    def filter_convex_lens(self,img,center_x, center_y, scale, fixed_radius):
        row, col, channel = img.shape
        y_indices, x_indices = np.indices((row, col))
        distance = (x_indices - center_x)**2 + (y_indices - center_y)**2
        valid_indices = distance <= fixed_radius**2
        new_dist = np.sqrt(distance[valid_indices]) * scale
        new_x = ((new_dist * (x_indices[valid_indices] - center_x) / fixed_radius + center_x))
        new_y = ((new_dist * (y_indices[valid_indices] - center_y) / fixed_radius + center_y))
        new_x = np.clip(new_x, 0, col - 1).astype(int)
        new_y = np.clip(new_y, 0, row - 1).astype(int)
        new_img = np.zeros_like(img)
        new_img[y_indices[valid_indices], x_indices[valid_indices]] = img[new_y, new_x]
        new_img[~valid_indices] = img[~valid_indices]
        return new_img

    def filter_concave_lens(self, src_img, cx, cy, sc):
        height, width = src_img.shape[:2]
        center = (cx, cy)
        img2 = np.zeros(src_img.shape, dtype=np.uint8)
        y, x = np.indices((height, width))
        theta = np.arctan2(y - center[1], x - center[0])
        R2 = np.sqrt(np.linalg.norm(np.dstack([x, y]) - center, axis=2)) * sc
        newX = center[0] + R2 * np.cos(theta)
        newY = center[1] + R2 * np.sin(theta)

        newX[newX < 0] = 0
        newX[newX >= width] = width - 1
        newY[newY < 0] = 0
        newY[newY >= height] = height - 1

        img2[y, x] = src_img[newY.astype(int), newX.astype(int)]
        return img2

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

    #亮度
    def BrightnessChange(self, img, brightness):
        brightness = brightness - 50
        # 对图像进行处理
        if img is not None:
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            dst = img_hsv.copy().astype(np.float32)
            dst[:, :, 2] = dst[:, :, 2] * (1 + brightness / 100)  # 亮度调整
            dst = np.clip(dst, 0, 255).astype(np.uint8)
            dst = cv2.cvtColor(dst, cv2.COLOR_HSV2BGR)
            return dst
    #对比度
    def Contrast_color(self, img, factor):
        # 对每个通道应用对比度增强
        b, g, r = cv2.split(img)
        b_enhanced = cv2.addWeighted(b, 1 + factor / 100, b, 0, 0)
        g_enhanced = cv2.addWeighted(g, 1 + factor / 100, g, 0, 0)
        r_enhanced = cv2.addWeighted(r, 1 + factor / 100, r, 0, 0)
        # 合并增强后的通道以获取彩色图像
        enhanced_image = cv2.merge((b_enhanced, g_enhanced, r_enhanced))
        return enhanced_image

    def adjust_image(self, img, brightness, contrast, saturation, temperature, hue_factor):
        hue_factor = (hue_factor-180)/10
        adjusted_image = cv2.convertScaleAbs(img, alpha=contrast / 50.0, beta=brightness - 50)
        hsv_image = cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2HSV)
        hue_channel = hsv_image[:, :, 0]
        hue_channel = (hue_channel + hue_factor) % 180
        hsv_image[:, :, 0] = hue_channel
        h, s, v = cv2.split(hsv_image)
        s = np.clip(s.astype(np.int32) + saturation - 50, 0, 255).astype(
            np.uint8)  # clip函数用于截取数值，将小于0的数值截取为0，将大于255的数值截取为255
        h = np.clip(h.astype(np.int32) + temperature - 50, 0, 255).astype(np.uint8)
        adjusted_hsv_image = cv2.merge((h, s, v))

        final_image = cv2.cvtColor(adjusted_hsv_image, cv2.COLOR_HSV2BGR)
        return final_image

    #色温
    def color_temperature(self,img,level):
        if img is not None:
            level = level - 50
            result = img.copy().astype(np.int16)  # 复制图像并转为int16数据类型防止数据溢出

            result[..., 2] = np.clip(result[..., 2] + level, 0, 255)  # R通道
            result[..., 1] = np.clip(result[..., 1] + level, 0, 255)  # G通道
            result[..., 0] = np.clip(result[..., 0] - level, 0, 255)  # B通道

            return result.astype(np.uint8)  # 转换回uint8数据类型
    #锐化
    def ImproveUSM(self, img, level):
        """Ths = 30  # 锐化阈值
        Factor = Factor-50
        DiffMask = np.zeros(img.shape, img.dtype)
        BlurImg = cv2.GaussianBlur(img, (9, 9), 0)
        if len(img.shape) == 2:  # 灰度单通道
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    Value_diff = abs(int(img[i, j]) - int(BlurImg[i, j]))
                    DiffMask[i, j] = 1 if Value_diff < Ths else 0

        elif len(img.shape) == 3:  # 三通道BGR
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    for k in range(img.shape[2]):
                        Value_diff = abs(int(img[i, j, k]) - int(BlurImg[i, j, k]))
                        DiffMask[i, j, k] = 1 if Value_diff < Ths else 0

        dst = cv2.addWeighted(img, 1 + Factor, BlurImg, -Factor, 0)
        dst = np.where(DiffMask == 1, img, dst)
        return dst"""
        # 根据锐化系数level生成锐化卷积核
        if level == 0:
            return img  # 当level等于0时，不进行锐化
        elif 0<level<25:
            kernel = np.array([[0, 0, 0],
                       [0, 1, 0],
                       [0, 0, 0]])
        elif 25<=level<50:
            kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
        elif 50<=level<75:
            kernel = np.array([[-1, -1, -1],
                               [-1, 9, -1],
                               [-1, -1, -1]])
        else:
            kernel = np.array([[1, 1, 1],
                               [1, -7, 1],
                               [1, 1, 1]])
        # 使用filter2D函数应用卷积核来锐化图像
        sharpened_img = cv2.filter2D(img, -1, kernel)
        # 将结果图像的亮度缩放到0-255范围内
        sharpened_img = cv2.convertScaleAbs(sharpened_img)
        return sharpened_img
    #阴影
    def ShadowImg(self,img,level):
        factor = level  # 范围在0到100之间的系数
        # 调整阴影效果的强度
        # 自适应阈值化
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        dst = shadow_effect = cv2.addWeighted(img, 1 - factor / 100, cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR), factor / 100,0)
        return dst

    #纹理
    def texture_flatten(self, img, smoothing_level):
        if smoothing_level<=25:
            blurred_image = cv2.GaussianBlur(img, (5, 5), 0)  # 调整卷积核大小和标准差以控制模糊程度
        elif smoothing_level<=50:
            blurred_image = cv2.medianBlur(img, 5)  # 调整窗口大小以控制模糊程度
        elif smoothing_level<=75:
            kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])  # 自定义卷积核，可以调整以实现不同的纹理效果
            blurred_image = cv2.filter2D(img, -1, kernel)
        else:
            blurred_image = cv2.Canny(img, 30, 70)  # 调整阈值以控制边缘检测的强度
        return blurred_image

    # 颗粒
    def Grainy(self, src, level):
        level /= 2
        if level > 50:
            level = 50
        if level < 0:
            level = 0

        noise = np.random.randint(-level, level + 1, src.shape, dtype=np.int32)
        result = np.clip(src + noise, 0, 255).astype(np.uint8)# 添加随机噪声
        return result

    def imageReader(self):
        self.ui.lable_pic_pro.clear()
        self.image_style = "Normal"
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
            self.ImageRendering()
            self.updateImageProcessed()
        else:
            QMessageBox.warning("错误","读取图片失败!!!")

    def imageSaver(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "pushButton_fileSave":
            if self.image_processed is not None:
                save_path, _ = QFileDialog.getSaveFileName(self, 'Save Image', '',
                                                           'Image Files (*.png *.jpg *.bmp);;All Files (*)')
                if save_path:
                    cv2.imwrite(save_path, self.image_processed)
            else:
                QMessageBox.warning(self,"错误","图片未进行修改！！！")
        elif btnName == "pushButton_fileSave_2":
            if self.img_transpancy is not None:

                save_path, _ = QFileDialog.getSaveFileName(self, 'Save Image', '',
                                                           'Image Files (*.png *.jpg *.bmp);;All Files (*)')
                if save_path:
                    cv2.imwrite(save_path,self.img_transpancy)
                else:
                    QMessageBox.warning(self, "错误", "图片未进行修改！！！")

    def updateImageSize(self,img_path):
        if self.image is not None:
            height, width, channel = self.image.shape
            bytes_per_line = 3 * width
            qt_image = QImage(self.image.data, width, height, bytes_per_line,
                              QImage.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(qt_image)

            self.ui.label_pic_raw.setPixmap(
                pixmap.scaled(self.ui.label_pic_raw.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def updateImageProcessed(self):
        if self.image_processed is not None:
            height, width, channel = self.image_processed.shape
            bytes_per_line = 3*width
            qt_image = QImage(self.image_processed.data,width,height,bytes_per_line,QImage.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(qt_image)
            self.ui.lable_pic_pro.setPixmap(
                pixmap.scaled(self.ui.lable_pic_pro.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.ui.lable_pic_pro.setimage_size(self.image_processed)

    def ChangeImageStyle(self):
        btn = self.sender()
        btnName = btn.objectName()
        # SHOW HOME PAGE
        if btnName == "Button_Style_1":
            self.image_style = "AUTUMN"
        elif btnName == "Button_Style_2":
            self.image_style = "BONE"
        elif btnName == "Button_Style_3":
            self.image_style = "JET"
        elif btnName == "Button_Style_4":
            self.image_style = "HSV"
        elif btnName == "Button_Style_5":
            self.image_style = "SPRING"
        elif btnName == "Button_Style_6":
            self.image_style = "SUMMER"
        elif btnName == "Button_Style_7":
            self.image_style = "WINTER"
        elif btnName == "Button_Style_8":
            self.image_style = "OCEAN"
        elif btnName == "Button_Style_9":
            self.image_style = "HOT"
        elif btnName == "Button_Style_10":
            self.image_style = "COOL"
        elif btnName == "Button_Style_11":
            self.image_style = "RAINBOW"
        elif btnName == "Button_Style_12":
            self.image_style = "PINK"
        elif btnName == "Button_Style_13":
            self.image_style = "SKETCH"
        elif btnName == "Button_Style_14":
            self.image_style = "CARTOON"
        elif btnName == "Button_Style_15":
            self.image_style = "Normal"
        self.ImageRendering()

    def ChangeImageSize(self):
        self.ChangeSize = True
        self.ImageRendering()

    def ChangeImageRotation(self):
        self.Changerotation = True
        self.ImageRendering()

    def Transform(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        self.TransformFlag = True
        if btnName == "radioButton_Fangshe":
            self.Points = []
            self.TransformPointNum = 3
        if btnName == "radioButton_Toushi":
            self.Points = []
            self.TransformPointNum = 4

    def SpecialEffectStart(self):
        self.SpecialEffect = True
        self.ImageRendering()

    def AreaSpecialEffectStart(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName =="pushButton_2":
            self.SpecialEffectArea = 2
        elif btnName == "pushButton_3":
            self.SpecialEffectArea = 3
        elif btnName == "pushButton_4":
            self.SpecialEffectArea = 4
        self.ImageRendering()

    def draw_ROI(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.tpPointsChoose.append((x, y))  # 保存顶点
            self.drawing = True
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.drawing = True
            self.tempFlag = True  # 按下右键，表示多边形绘制完成


    def ImageRendering(self):

       if self.image is not None:
            img = self.image.copy()

            if (self.ui.horizontalSlider_rendering_2.value() != 50) or (self.ui.horizontalSlider_rendering_5.value() != 50) or (self.ui.horizontalSlider_rendering_4.value() != 50) or (self.ui.horizontalSlider_rendering_7.value() != 50) or (self.ui.horizontalSlider_rendering_6.value() != 180):
                brightness = self.ui.horizontalSlider_rendering_2.value()
                contrast = self.ui.horizontalSlider_rendering_5.value()
                saturation = self.ui.horizontalSlider_rendering_4.value()
                temperature = self.ui.horizontalSlider_rendering_7.value()
                color_tone = self.ui.horizontalSlider_rendering_6.value()
                img = self.adjust_image(img,brightness,contrast,saturation,temperature,color_tone)
            if self.ui.horizontalSlider_rendering_8.value() != 0:
                USM = widgets.horizontalSlider_rendering_8.value()
                img = self.ImproveUSM(img,USM)
            if self.ui.horizontalSlider_rendering_9.value() != 0:
                level = self.ui.horizontalSlider_rendering_9.value()
                img = self.Grainy(img,level)
            if self.ui.horizontalSlider_rendering_10.value() != 0:
                level = widgets.horizontalSlider_rendering_10.value()
                img = self.texture_flatten(img,level)
            if self.ui.horizontalSlider_rendering_11.value() != 0:
                level = widgets.horizontalSlider_rendering_11.value()
                img = self.ShadowImg(img,level)
            if self.image_style!="Normal":
                if self.image_style == "CARTOON":
                    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    img_gray = cv2.medianBlur(img_gray, 7)
                    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
                    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
                    img_small = cv2.resize(img, None, fx=1, fy=1.0 ,
                                           interpolation=cv2.INTER_AREA)
                    num_repetitions = 10
                    sigma_color = 5
                    sigma_space = 7
                    size = 5
                    for i in range(num_repetitions):
                        img_small = cv2.bilateralFilter(img_small, size, sigma_color, sigma_space)
                    img_output = cv2.resize(img_small, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
                    dst = np.zeros(img_gray.shape)
                    img = cv2.bitwise_and(img_output, img_output, mask=mask)
                elif self.image_style == "SKETCH":
                    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    img_gray = cv2.medianBlur(img_gray, 7)
                    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
                    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
                    img = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
                else:
                    # 根据颜色映射名称获取OpenCV中对应的常量值
                    lut = getattr(cv2, 'COLORMAP_' + self.image_style)
                    # 应用颜色映射到图片
                    result = cv2.applyColorMap(img, lut)
                    # 在图片上添加颜色映射名称文本
                    #result = cv2.putText(result, self.image_style, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    img = result

            if self.ChangeSize == True:
                    width = int(self.ui.lineEdit_Width.text())
                    height = int(self.ui.lineEdit_Height.text())
                    scale_percent = 10
                    dim = (width, height)
                    resized_image = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                    img = resized_image
            if self.Changerotation == True:
                # 获取滚动条的值
                angle = self.ui.horizontalSlider_Rotation.value()
                # 旋转
                rows, cols = img.shape[:2]
                M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
                dst = cv2.warpAffine(img, M, (cols, rows), borderValue=(255, 255, 255))
                img = dst
                self.Changerotation = False
            if self.TransformStart == True:
                self.TransformFlag = False
                self.TransformPointNum = None
                self.TransformStart = False
                if self.ui.radioButton_Fangshe.isChecked():
                    rows, cols = img.shape[:2]
                    mask = np.zeros((rows, cols), dtype=np.uint8)
                    pts1 = np.float32(self.Points)
                    pts2 = np.float32([[0, 0], [cols, 0], [cols, rows]])
                    M = cv2.getAffineTransform(pts1, pts2)
                    cv2.fillPoly(mask, [np.array(self.Points)], (255, 255, 255))
                    dst = cv2.warpAffine(img, M, (cols, rows))
                    dst_trans = cv2.cvtColor(dst, cv2.COLOR_BGR2BGRA)
                    dst_trans[:, :, 3] = mask
                    self.img_transpancy = dst_trans
                    img = dst
                    self.ui.radioButton_Fangshe.setChecked(False)
                elif self.ui.radioButton_Toushi.isChecked():
                    img_2 = img.copy()
                    height, width, channel = img.shape
                    mask = np.zeros((height, width))
                    M = cv2.getPerspectiveTransform(
                        np.float32([[0, 0], [0, width - 1], [height - 1, width - 1], [height - 1, 0]]),
                        np.float32(self.Points))
                    cv2.fillPoly(mask, [np.array(self.Points)], color=255)
                    dst = cv2.warpPerspective(img_2, M, (width, height))
                    dst_trans = cv2.cvtColor(dst, cv2.COLOR_BGR2BGRA)
                    dst_trans[:, :, 3] = mask
                    self.img_transpancy = dst_trans
                    img = dst
                    self.ui.radioButton_Toushi.setChecked(False)
                self.Points = []

            if self.SpecialEffect == True:
                if self.ui.radioButton_AoTou.isChecked():
                    """凹透镜"""
                    cy = img.shape[0] // 2
                    cx = img.shape[1] // 2
                    sc = 1.0

                    cx = self.ui.horizontalSlider_2.value()/200*img.shape[1]
                    cy = self.ui.horizontalSlider_3.value()/200*img.shape[0]
                    sc = self.ui.horizontalSlider_4.value()/5+10
                    filtered_img = self.filter_concave_lens(img, cx, cy, sc)
                    scale_percent = 50

                    width = int(img.shape[1] * scale_percent / 100)
                    height = int(img.shape[0] * scale_percent / 100)
                    dim = (width, height)
                    # resized_input = cv2.resize(self.image, dim, interpolation=cv2.INTER_AREA)
                    resized_input = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                    resized_filtered = cv2.resize(filtered_img, dim, interpolation=cv2.INTER_AREA)
                    img = resized_filtered

                elif self.ui.radioButton_TuTou.isChecked():
                    """凸透镜"""
                    cy = img.shape[0] // 2
                    cx = img.shape[1] // 2
                    sc = 1.0
                    fixed_radius = max(cx, cy) * 2

                    cx = self.ui.horizontalSlider_5.value()*5
                    cy = self.ui.horizontalSlider_6.value()*5
                    scale = self.ui.horizontalSlider_7.value() / 50
                    filtered_img = self.filter_convex_lens(img, cx, cy, scale, fixed_radius)

                    scale_percent = 50
                    width = int(img.shape[1] * scale_percent / 100)
                    height = int(img.shape[0] * scale_percent / 100)
                    dim = (width, height)
                    # resized_input = cv2.resize(self.image, dim, interpolation=cv2.INTER_AREA)
                    resized_filtered = cv2.resize(filtered_img, dim, interpolation=cv2.INTER_AREA)

                    img = resized_filtered

                elif self.ui.radioButton_CaoTu.isChecked():
                    dst = cv2.Sobel(img, -1, 1, 1)
                    dst = 255 - dst
                    img = dst

                elif self.ui.radioButton_NONE.isChecked():
                    self.SpecialEffect = False

            if self.SpecialEffectArea is not None:
                if self.SpecialEffectArea == 2:
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    imgg = img.copy()
                    r, c = img.shape
                    cv2.namedWindow('image')
                    cv2.setMouseCallback('image', self.draw_ROI)
                    mask = np.zeros((r, c), dtype=np.uint8)
                    while True:
                        if self.tempFlag and self.drawing:
                            if len(self.tpPointsChoose) >= 3:
                                cv2.fillPoly(mask, [np.array(self.tpPointsChoose)], 255)
                                cv2.polylines(img, [np.array(self.tpPointsChoose)], isClosed=True, color=(0, 255, 0),
                                              thickness=1)
                        else:
                            if len(self.tpPointsChoose) > 0:
                                cv2.polylines(img, [np.array(self.tpPointsChoose)], isClosed=False, color=(0, 255, 0),
                                              thickness=1)
                        cv2.imshow('image', imgg)
                        if cv2.waitKey(1) & 0xFF == 13:  # 按enter键保存图像
                            self.tempFlag = False
                            break

                    cv2.destroyAllWindows()

                    key = np.random.randint(0, 256, size=[r, c], dtype=np.uint8)
                    imgXorKey = cv2.bitwise_xor(img, key)  # 异或运算，加密
                    encryptFace = cv2.bitwise_and(imgXorKey, mask)  # 与运算，提取前景
                    noFace1 = cv2.bitwise_and(img, 255 - mask)  # 与运算，提取背景
                    masked_img = cv2.add(encryptFace, noFace1)  # 加运算，合成图像
                    img = masked_img
                    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                    cv2.destroyAllWindows()

                elif self.SpecialEffectArea == 3:
                    pass
                elif self.SpecialEffectArea == 4:
                    pass

            self.image_processed = img
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
