# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\image_editor_ui_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QRubberBand, QMessageBox
import numpy as np
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_frame = QtWidgets.QFrame(self.centralwidget)
        self.image_frame.setGeometry(QtCore.QRect(130, 20, 591, 511))
        self.image_frame.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_frame.setObjectName("image_frame")
        self.pictureBox = QtWidgets.QLabel(self.image_frame)
        self.pictureBox.setGeometry(QtCore.QRect(10, 10, 571, 491))
        self.pictureBox.setText("")
        self.pictureBox.setPixmap(QtGui.QPixmap("images/gallery.png"))
        self.pictureBox.setScaledContents(True)
        self.pictureBox.setObjectName("pictureBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 61, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fileBrowserButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.fileBrowserButton.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/photo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileBrowserButton.setIcon(icon)
        self.fileBrowserButton.setIconSize(QtCore.QSize(50, 50))
        self.fileBrowserButton.setAutoRaise(True)
        self.fileBrowserButton.setObjectName("fileBrowserButton")
        self.verticalLayout.addWidget(self.fileBrowserButton)
        self.cropButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.cropButton.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/crop-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cropButton.setIcon(icon1)
        self.cropButton.setIconSize(QtCore.QSize(50, 50))
        self.cropButton.setAutoRaise(True)
        self.cropButton.setObjectName("cropButton")
        self.verticalLayout.addWidget(self.cropButton)
        self.automaticEnhancementButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/enhancement.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.automaticEnhancementButton.setIcon(icon2)
        self.automaticEnhancementButton.setIconSize(QtCore.QSize(50, 50))
        self.automaticEnhancementButton.setAutoRaise(True)
        self.automaticEnhancementButton.setObjectName("automaticEnhancementButton")
        self.verticalLayout.addWidget(self.automaticEnhancementButton)
        self.inverseButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/invert-tool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inverseButton.setIcon(icon3)
        self.inverseButton.setIconSize(QtCore.QSize(50, 50))
        self.inverseButton.setAutoRaise(True)
        self.inverseButton.setObjectName("inverseButton")
        self.verticalLayout.addWidget(self.inverseButton)
        self.blurButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/drop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.blurButton.setIcon(icon4)
        self.blurButton.setIconSize(QtCore.QSize(50, 50))
        self.blurButton.setAutoRaise(True)
        self.blurButton.setObjectName("blurButton")
        self.verticalLayout.addWidget(self.blurButton)
        self.resetButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resetButton.setIcon(icon5)
        self.resetButton.setIconSize(QtCore.QSize(50, 50))
        self.resetButton.setAutoRaise(True)
        self.resetButton.setObjectName("resetButton")
        self.verticalLayout.addWidget(self.resetButton)
        self.saveButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon6)
        self.saveButton.setIconSize(QtCore.QSize(50, 50))
        self.saveButton.setAutoRaise(True)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(130, 543, 251, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.brighterLabel = QtWidgets.QLabel(self.frame)
        self.brighterLabel.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.brighterLabel.setFont(font)
        self.brighterLabel.setObjectName("brighterLabel")
        self.darkerLabel = QtWidgets.QLabel(self.frame)
        self.darkerLabel.setGeometry(QtCore.QRect(12, 40, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.darkerLabel.setFont(font)
        self.darkerLabel.setObjectName("darkerLabel")
        self.brighterSlider = QtWidgets.QSlider(self.frame)
        self.brighterSlider.setGeometry(QtCore.QRect(70, 10, 160, 22))
        self.brighterSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brighterSlider.setObjectName("brighterSlider")
        self.darkerSlider = QtWidgets.QSlider(self.frame)
        self.darkerSlider.setGeometry(QtCore.QRect(70, 40, 160, 22))
        self.darkerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.darkerSlider.setObjectName("darkerSlider")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(430, 542, 291, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.incContrastLabel = QtWidgets.QLabel(self.frame_2)
        self.incContrastLabel.setGeometry(QtCore.QRect(10, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.incContrastLabel.setFont(font)
        self.incContrastLabel.setObjectName("incContrastLabel")
        self.decContrastLabel = QtWidgets.QLabel(self.frame_2)
        self.decContrastLabel.setGeometry(QtCore.QRect(12, 40, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.decContrastLabel.setFont(font)
        self.decContrastLabel.setObjectName("decContrastLabel")
        self.incContrastSlider = QtWidgets.QSlider(self.frame_2)
        self.incContrastSlider.setGeometry(QtCore.QRect(110, 10, 160, 22))
        self.incContrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.incContrastSlider.setObjectName("incContrastSlider")
        self.decContrastSlider = QtWidgets.QSlider(self.frame_2)
        self.decContrastSlider.setGeometry(QtCore.QRect(110, 40, 160, 22))
        self.decContrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.decContrastSlider.setObjectName("decContrastSlider")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 640, 251, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.flipVerticalButton = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/flipVertical.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flipVerticalButton.setIcon(icon7)
        self.flipVerticalButton.setIconSize(QtCore.QSize(50, 50))
        self.flipVerticalButton.setAutoRaise(True)
        self.flipVerticalButton.setObjectName("flipVerticalButton")
        self.horizontalLayout.addWidget(self.flipVerticalButton)
        self.flipHorizontalButton = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/flipHorizontal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flipHorizontalButton.setIcon(icon8)
        self.flipHorizontalButton.setIconSize(QtCore.QSize(50, 50))
        self.flipHorizontalButton.setAutoRaise(True)
        self.flipHorizontalButton.setObjectName("flipHorizontalButton")
        self.horizontalLayout.addWidget(self.flipHorizontalButton)
        self.flipLabel = QtWidgets.QLabel(self.centralwidget)
        self.flipLabel.setGeometry(QtCore.QRect(240, 623, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.flipLabel.setFont(font)
        self.flipLabel.setObjectName("flipLabel")
        self.degreeBox = QtWidgets.QLineEdit(self.centralwidget)
        self.degreeBox.setGeometry(QtCore.QRect(490, 677, 113, 22))
        self.degreeBox.setObjectName("degreeBox")
        self.rotateLabel = QtWidgets.QLabel(self.centralwidget)
        self.rotateLabel.setGeometry(QtCore.QRect(580, 620, 60, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rotateLabel.setFont(font)
        self.rotateLabel.setObjectName("rotateLabel")
        self.degreeLabel = QtWidgets.QLabel(self.centralwidget)
        self.degreeLabel.setGeometry(QtCore.QRect(430, 675, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.degreeLabel.setFont(font)
        self.degreeLabel.setObjectName("degreeLabel")
        self.rotateButton = QtWidgets.QToolButton(self.centralwidget)
        self.rotateButton.setGeometry(QtCore.QRect(637, 660, 57, 56))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/rotation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotateButton.setIcon(icon9)
        self.rotateButton.setIconSize(QtCore.QSize(50, 50))
        self.rotateButton.setAutoRaise(True)
        self.rotateButton.setObjectName("rotateButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mini Photoshop"))
        self.fileBrowserButton.setToolTip(_translate("MainWindow", "Upload File"))
        self.fileBrowserButton.setText(_translate("MainWindow", "..."))
        self.cropButton.setToolTip(_translate("MainWindow", "Crop Image"))
        self.cropButton.setText(_translate("MainWindow", "..."))
        self.automaticEnhancementButton.setToolTip(_translate("MainWindow", "Automatic Enhancement"))
        self.automaticEnhancementButton.setText(_translate("MainWindow", "..."))
        self.inverseButton.setToolTip(_translate("MainWindow", "Reverse Image"))
        self.inverseButton.setText(_translate("MainWindow", "..."))
        self.blurButton.setToolTip(_translate("MainWindow", "Blur"))
        self.blurButton.setText(_translate("MainWindow", "..."))
        self.resetButton.setToolTip(_translate("MainWindow", "Reset"))
        self.resetButton.setText(_translate("MainWindow", "..."))
        self.saveButton.setToolTip(_translate("MainWindow", "Save Image"))
        self.saveButton.setText(_translate("MainWindow", "..."))
        self.brighterLabel.setText(_translate("MainWindow", "Brighter"))
        self.darkerLabel.setText(_translate("MainWindow", "Darker"))
        self.incContrastLabel.setText(_translate("MainWindow", "Inc. Contrast"))
        self.decContrastLabel.setText(_translate("MainWindow", "Dec. Contrast"))
        self.flipVerticalButton.setToolTip(_translate("MainWindow", "Vertical Flip"))
        self.flipVerticalButton.setText(_translate("MainWindow", "..."))
        self.flipHorizontalButton.setToolTip(_translate("MainWindow", "Horizontal Flip"))
        self.flipHorizontalButton.setText(_translate("MainWindow", "..."))
        self.flipLabel.setText(_translate("MainWindow", "Flip"))
        self.rotateLabel.setText(_translate("MainWindow", "Rotate"))
        self.degreeLabel.setText(_translate("MainWindow", "Degree"))
        self.rotateButton.setToolTip(_translate("MainWindow", "Rotate"))
        self.rotateButton.setText(_translate("MainWindow", "..."))

        self.isCropping = False

        def message_box(title, message, icon = QMessageBox.Information):
            msg = QMessageBox()
            msg.setIcon(icon)
            msg.setText(message)
            msg.setWindowTitle(title)
            msg.exec()

        def enable_buttons(bool):
            self.cropButton.setEnabled(bool)
            self.automaticEnhancementButton.setEnabled(bool)
            self.inverseButton.setEnabled(bool)
            self.blurButton.setEnabled(bool)
            self.resetButton.setEnabled(bool)
            self.saveButton.setEnabled(bool)
            self.flipVerticalButton.setEnabled(bool)
            self.flipHorizontalButton.setEnabled(bool)
            self.rotateButton.setEnabled(bool)
            self.degreeBox.setEnabled(bool)
            self.darkerSlider.setEnabled(bool)
            self.brighterSlider.setEnabled(bool)
            self.incContrastSlider.setEnabled(bool)
            self.decContrastSlider.setEnabled(bool)
            self.pictureBox.setEnabled(bool)

        #----------START----------

        enable_buttons(False)

        def ndarray2qimage(image):
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            h = image.shape[0]
            w = image.shape[1]
            bytesPerLine = 3 * w
            qimage = QtGui.QImage(image, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            return qimage

        def show_picture(image):
            qimage = ndarray2qimage(image)
            self.pictureBox.setPixmap(QtGui.QPixmap(qimage))
        
        def upload_image():
            file_dialog = QFileDialog.getOpenFileName(None, 'Load Image', '', 'Image file (*.jpg | *.png | *.jpeg)')
            path = file_dialog[0]
            if not(path == ''):
                self.original_image = cv2.imread(path)
                self.final_image = self.original_image
                show_picture(self.final_image)
                enable_buttons(True)
            else:
                message_box("File Error", "You did not select an image!")

        def crop(image):
            w,h,c = image.shape

            sizeW = self.pictureBox.size().width()
            sizeH = self.pictureBox.size().height()

            x1 = int(w*(self.origin.x())/sizeW) 
            y1 = int(h*(self.origin.y())/sizeH)
            x2 = int(w*(self.finish.x())/sizeW)
            y2 = int(h*(self.finish.y())/sizeH)

            self.final_image = image[min(x1,x2):max(x1,x2),
                                     min(y1,y2):max(y1,y2)]
            show_picture(self.final_image)
            
        def crop_image():
            self.rubberband = QRubberBand(QRubberBand.Rectangle, self.pictureBox)
            palette = QtGui.QPalette()
            palette.setBrush(QtGui.QPalette.Highlight, QtGui.QBrush(QtCore.Qt.red))
            self.rubberband.setPalette(palette)
            self.rubberband.setWindowOpacity(1.0)
            self.isCropping = True

        def mousePressEvent(event):
            if self.isCropping:
                self.origin = event.pos()
                if not self.rubberband:
                    self.rubberband = QRubberBand(QRubberBand.Rectangle, self.pictureBox)
                self.rubberband.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
                self.rubberband.show()
        def mouseMoveEvent(event):
            if self.isCropping:
                self.rubberband.setGeometry(QtCore.QRect(self.origin, event.pos()).normalized())
        def mouseReleaseEvent(event):
            if self.isCropping:
                self.rubberband.hide()
                self.isCropping = False
                self.finish = event.pos()
                crop(self.final_image)

        def histogram_image(image, L):
            hist, bins = np.histogram(image, bins = L, range = (0, L))
            return hist

        def normalize_histogram(histogram, image):
            w, h, c = image.shape
            return histogram/(w*h*c)

        def cumulative_distribution(probablities):
            return np.cumsum(probablities)

        def histogram_equalization(image, cumulative_distribution, L):
            transformation_function = (L-1) * cumulative_distribution
            shape = image.shape
            one_dim_image = image.ravel()
            equalized_image = np.zeros(shape[0]*shape[1]*shape[2])
            for index, pixel in enumerate(one_dim_image):
                equalized_image[index] = transformation_function[pixel]
            equalized_image = equalized_image.reshape(shape).astype(np.uint8)
            return equalized_image

        def auto_enhancement():
            L = 2**8
            histogram = histogram_image(self.final_image, L)
            normalized_histogram = normalize_histogram(histogram, self.final_image)
            cumulative_distribution = np.cumsum(normalized_histogram)
            self.final_image = histogram_equalization(self.final_image, cumulative_distribution, L)
            show_picture(self.final_image)

        def reverse():
            self.final_image = 255-self.final_image
            show_picture(self.final_image)

        def zero_pad(X, pad):
            X_pad = np.pad(X,((pad,pad),(pad,pad)), 'constant')
            return X_pad 

        def conv_single(matrix, kernel):
            Z = np.multiply(matrix, kernel).sum()
            return Z

        def convolution(image2D, kernel, padding, stride):
            (n_H, n_W) = image2D.shape
            (f, f) = kernel.shape

            n_H = int(((n_H-f+2*padding)/stride)+1)
            n_W = int(((n_W-f+2*padding)/stride)+1)

            new_image = np.zeros([n_H, n_W])

            new_image_pad = zero_pad(image2D, padding)

            for h in range(n_H):
                for w in range(n_W):
                    vert_start = h * stride
                    vert_end = vert_start + f
                    horiz_start = w * stride
                    horiz_end = horiz_start + f
                    
                    sliced = new_image_pad[vert_start:vert_end, horiz_start:horiz_end]
                    if(sliced.shape == (f,f)):
                        new_image[h, w] = conv_single(sliced, kernel)

            return new_image

        def conv_color(image, kernel, padding, stride):
            
            r = image[:,:,0]
            g = image[:,:,1]
            b = image[:,:,2]

            c_r = convolution(r,kernel,padding,stride)
            c_g = convolution(g,kernel,padding,stride)
            c_b = convolution(b,kernel,padding,stride)
            
            rgb = np.dstack([c_r, c_g, c_b])

            return rgb

        def blur():
            filter = np.array([[1,4,7,4,1],[4,16,26,16,4],[7,26,41,26,7],[4,16,26,16,4],[1,4,7,4,1]])/273
            self.final_image = conv_color(self.final_image, filter, 1, 1).astype(np.uint8)
            show_picture(self.final_image)

        def reset():
            self.final_image = self.original_image
            show_picture(self.final_image)

        def save_image():
            image = self.pictureBox.pixmap().toImage()
            file_dialog = QFileDialog.getSaveFileName(None, 'Save Image', 'edited_image.jpg',  "Images (*.png *.jpg *.jpeg)")
            image.save(file_dialog[0])

        def save_img(image, path):
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            cv2.imwrite(path, image)

        def flipX(image):
            n_H, n_W, n_C = image.shape
            new_image = np.zeros_like(image)
            for h in range(n_H):
                for w in range(n_W):
                    for c in range(n_C):
                        new_image[h, w, c] = image[h, n_W - w - 1, c]
            return new_image

        def flipY(image):
            n_H, n_W, n_C = image.shape
            new_image = np.zeros_like(image)
            for h in range(n_H):
                for w in range(n_W):
                    for c in range(n_C):
                        new_image[h, w, c] = image[n_H - h - 1, w , c]
            return new_image

        def flipVertical():
            self.final_image = flipX(self.final_image)
            show_picture(self.final_image)

        def flipHorizontal():
            self.final_image = flipY(self.final_image)
            show_picture(self.final_image)

        def brightness_image(image, value):
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            hue, sat, val = cv2.split(hsv)
            val = cv2.add(val, value)

            val[val > 255] = 255
            val[val < 0] = 0

            new_hsv = cv2.merge((hue, sat, val))
            new_image = cv2.cvtColor(new_hsv, cv2.COLOR_HSV2BGR)
            return new_image

        def bright():
            self.final_image = brightness_image(self.final_image, int(self.brighterSlider.value()/20))
            show_picture(self.final_image)

        def dark():
            self.final_image = brightness_image(self.final_image, -int(self.darkerSlider.value()/20))
            show_picture(self.final_image)
            
        self.pictureBox.mousePressEvent = mousePressEvent
        self.pictureBox.mouseMoveEvent = mouseMoveEvent
        self.pictureBox.mouseReleaseEvent = mouseReleaseEvent

        self.fileBrowserButton.clicked.connect(upload_image)
        self.cropButton.clicked.connect(crop_image)
        self.automaticEnhancementButton.clicked.connect(auto_enhancement)
        self.inverseButton.clicked.connect(reverse)
        self.blurButton.clicked.connect(blur)
        self.resetButton.clicked.connect(reset)
        self.saveButton.clicked.connect(save_image)

        self.flipVerticalButton.clicked.connect(flipVertical)
        self.flipHorizontalButton.clicked.connect(flipHorizontal)

        self.brighterSlider.valueChanged.connect(bright)
        self.darkerSlider.valueChanged.connect(dark)

        # ----------END----------


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
