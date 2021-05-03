# Form implementation generated from reading ui file '.\image_editor_ui_designer.ui'
# Created by: PyQt5 UI code generator 5.15.2

#I used PyQT5 library for UI. Coding UI is too hard, so I used QT Designer for it. Then I changed little things.
#QTDesigner file is image_editor_ui_designer.ui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QRubberBand, QMessageBox
import numpy as np
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 780)
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(770, 0, 160, 711))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button1.setObjectName("button1")
        self.verticalLayout_2.addWidget(self.button1)
        self.button2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button2.setObjectName("button2")
        self.verticalLayout_2.addWidget(self.button2)
        self.button3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button3.setObjectName("button3")
        self.verticalLayout_2.addWidget(self.button3)
        self.button4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button4.setObjectName("button4")
        self.verticalLayout_2.addWidget(self.button4)
        self.button5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button5.setObjectName("button5")
        self.verticalLayout_2.addWidget(self.button5)
        self.button6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button6.setObjectName("button6")
        self.verticalLayout_2.addWidget(self.button6)
        self.button7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button7.setObjectName("button7")
        self.verticalLayout_2.addWidget(self.button7)
        self.button8 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button8.setObjectName("button8")
        self.verticalLayout_2.addWidget(self.button8)
        self.button9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button9.setObjectName("button9")
        self.verticalLayout_2.addWidget(self.button9)
        self.button10 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button10.setObjectName("button10")
        self.verticalLayout_2.addWidget(self.button10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 986, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gurkan's Mini Photoshop"))
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
        self.button1.setText(_translate("MainWindow", "Sepia"))
        self.button2.setText(_translate("MainWindow", "Sketch"))
        self.button3.setText(_translate("MainWindow", "Emboss"))
        self.button4.setText(_translate("MainWindow", "Shriveled Paper"))
        self.button5.setText(_translate("MainWindow", "Cartoon"))
        self.button6.setText(_translate("MainWindow", "Daylight"))
        self.button7.setText(_translate("MainWindow", "Soul"))
        self.button8.setText(_translate("MainWindow", "Pixelizer"))
        self.button9.setText(_translate("MainWindow", "Angelize"))
        self.button10.setText(_translate("MainWindow", "Devil"))

        self.isCropping = False #It shows cropping status

        #I don't want to use print function, so I created a messagebox for information like in C# form applications.
        def message_box(title, message, icon = QMessageBox.Information):
            msg = QMessageBox()
            msg.setIcon(icon)
            msg.setText(message)
            msg.setWindowTitle(title)
            msg.exec()
        
        #Before uploading and image to program, all buttons are like "you can click on me". I can disable or enable with this method.
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
            self.button1.setEnabled(bool)
            self.button2.setEnabled(bool)
            self.button3.setEnabled(bool)
            self.button4.setEnabled(bool)
            self.button5.setEnabled(bool)
            self.button6.setEnabled(bool)
            self.button7.setEnabled(bool)
            self.button8.setEnabled(bool)
            self.button9.setEnabled(bool)
            self.button10.setEnabled(bool)

        #----------START----------

        #!!! I call picture are as a pictureBox, but it is originally a label. !!!
        
        enable_buttons(False)  #All buttons except upload button are disabled in the beginning of the program.

        # This method converts numpy array to QImage for pictureBox.
        #I can assign an image by using QImage type
        def ndarray2qimage(image):
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #Converting BGR image to RGB image
            h = image.shape[0] #height of the image
            w = image.shape[1] #width of the image
            bytesPerLine = 3 * w
            qimage = QtGui.QImage(image, w, h, bytesPerLine, QtGui.QImage.Format_RGB888) #This method converts RGB image to QImage
            return qimage

        #This method shows the image on the pictureBox. 
        def show_picture(image):
            qimage = ndarray2qimage(image) 
            self.pictureBox.setPixmap(QtGui.QPixmap(qimage))
        
        #This method uploads the specified image to the program.
        def upload_image():
            file_dialog = QFileDialog.getOpenFileName(None, 'Load Image', '', 'Image file (*.jpg | *.png | *.jpeg)') #OpenFileDialog
            path = file_dialog[0] #Taking path of the specified image
            if not(path == ''):
                self.original_image = cv2.imread(path) #Reading image from the path
                self.final_image = self.original_image #final_image variable keeps the image I will work on
                show_picture(self.final_image) #Showing image on the pictureBox after uploading the image
                enable_buttons(True) #Enable all buttons now
            else:
                message_box("File Error", "You did not select an image!") #If the user doesn't select an image, this error message will be showed up.
        
        #This method crops the image according to origin and final coordinates
        def crop(image):
            w,h,c = image.shape #width, height, channel of the image

            sizeW = self.pictureBox.size().width()  #width of the pictureBox
            sizeH = self.pictureBox.size().height() #height of the pictureBox

            #The point that I select on the pictureBox may not be the same with the point on the image. 
            #For this reason, I used similarity between these two images. Basic rectangle similarity.
            
            x1 = int(w*(self.origin.x())/sizeW) 
            y1 = int(h*(self.origin.y())/sizeH)
            x2 = int(w*(self.finish.x())/sizeW)
            y2 = int(h*(self.finish.y())/sizeH)
            
            #Now I got original points for the image. I can slice the image according to theese points.
            #I used min and max because start points can be bigger than end points. 
            #We can select the area that we want to crop by starting different points and end point may be smaller than this point.

            self.final_image = image[min(x1,x2):max(x1,x2),
                                     min(y1,y2):max(y1,y2)]
            show_picture(self.final_image)
            
        def crop_image(): #Firstly click on crop button then select an area by mouse movement. After releasing button, the image will be cropped.
            self.rubberband = QRubberBand(QRubberBand.Rectangle, self.pictureBox) #Creating QRubberBand. This helped me to draw rectangle on the image for selecting and area
            palette = QtGui.QPalette() 
            palette.setBrush(QtGui.QPalette.Highlight, QtGui.QBrush(QtCore.Qt.red)) # Setting up QRubberBand properties
            self.rubberband.setPalette(palette)
            self.rubberband.setWindowOpacity(1.0)
            self.isCropping = True #The user is in cropping mode, that means
        
        #This event controls I clicked on pictureBox or not. 
        def mousePressEvent(event):
            if self.isCropping:
                self.origin = event.pos() #origin is the point that I started to select an area
                if not self.rubberband:
                    self.rubberband = QRubberBand(QRubberBand.Rectangle, self.pictureBox) #I used QRubberBand for the selecting are
                self.rubberband.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
                self.rubberband.show()
                
        #This event watches mouse movements            
        def mouseMoveEvent(event):
            if self.isCropping:
                self.rubberband.setGeometry(QtCore.QRect(self.origin, event.pos()).normalized()) #When I drag my mouse, the size of the rectangle will change
        
        #This event controls that I release the clicking or not.        
        def mouseReleaseEvent(event):
            if self.isCropping:
                self.rubberband.hide()
                self.isCropping = False
                self.finish = event.pos() #finish is the end point
                crop(self.final_image) #We can crop the image now
        
        #Calculating histogram of the image by using numpy.histogram
        def histogram_image(image, L):
            hist, bins = np.histogram(image, bins = L, range = (0, L))
            return hist
        
        #Normalizing histograk
        def normalize_histogram(histogram, image):
            w, h, c = image.shape
            return histogram/(w*h*c) #I divided histogram by size of the image
        
        #Calculating cumulative distribution by using numpy.cumsum function
        def cumulative_distribution(probablities):
            return np.cumsum(probablities)
        
        #I used histogram equalization formula in this function
        def histogram_equalization(image, cumulative_distribution, L):
            transformation_function = (L-1) * cumulative_distribution #I calculated transformation function
            shape = image.shape
            one_dim_image = image.ravel() #Converting image to 1D array
            equalized_image = np.zeros(shape[0]*shape[1]*shape[2]) #zero array with the same shape of the image
            for index, pixel in enumerate(one_dim_image):
                equalized_image[index] = transformation_function[pixel] #Assigning transformation function values to image
            equalized_image = equalized_image.reshape(shape).astype(np.uint8) #Converting the image 3D back.
            return equalized_image
        
        #Click on magic wand button.
        def auto_enhancement():
            L = 2**8 #We have 8 bytes in the pixel
            histogram = histogram_image(self.final_image, L)
            normalized_histogram = normalize_histogram(histogram, self.final_image)
            cumulative_distribution = np.cumsum(normalized_histogram)
            self.final_image = histogram_equalization(self.final_image, cumulative_distribution, L)
            show_picture(self.final_image) #After histogram equalization we can show the enhanced image
        
        #Click on reverse button.
        def reverse():
            self.final_image = 255-self.final_image #I subtracted 255 from the image basically.
            show_picture(self.final_image)
        
        #Padding for one-channel images by using numpy.pad function
        def zero_pad(X, pad):
            X_pad = np.pad(X,((pad,pad),(pad,pad)), 'constant')
            return X_pad 
        
        #Single convolution calculation
        def conv_single(matrix, kernel):
            Z = np.multiply(matrix, kernel).sum() #For example kernel is 5 by 5 and matrix is 5 by by. We can multiply them directly and sum the final matrix.
            return Z
        
        #This method calculates the convolution according to image, kernel, padding and stride
        #I learnt this method from Andrew NG in coursera courses, so these convolution methods are nearly the same with Andrew's.
        def convolution(image2D, kernel, padding, stride):
            (n_H, n_W) = image2D.shape #Taking height and width of the image
            (f, f) = kernel.shape #kernel width and height

            n_H = int(((n_H-f+2*padding)/stride)+1) #I calculated new height and width
            n_W = int(((n_W-f+2*padding)/stride)+1)

            new_image = np.zeros([n_H, n_W]) #Creating new image with the same shape of the image

            new_image_pad = zero_pad(image2D, padding) #I applied padding to image
            
            #Iterating through height and width of the image
            for h in range(n_H):
                for w in range(n_W):
                    #I calculate fxf matrix from the image according to stride number
                    vert_start = h * stride 
                    vert_end = vert_start + f
                    horiz_start = w * stride
                    horiz_end = horiz_start + f
                    
                    sliced = new_image_pad[vert_start:vert_end, horiz_start:horiz_end] #We have fxf matrix from the image
                    if(sliced.shape == (f,f)): #If the matrix that is sliced from the image, is fxf
                        new_image[h, w] = conv_single(sliced, kernel) #We can calculate convolution

            return new_image

        def conv_color(image, kernel, padding, stride):
            
            #When we want to apply convolution to color image we apply convolution to each channels.
            
            r = image[:,:,0]
            g = image[:,:,1]
            b = image[:,:,2]

            #I applied convolution red, green and blue channel separately
                
            c_r = convolution(r,kernel,padding,stride)
            c_g = convolution(g,kernel,padding,stride)
            c_b = convolution(b,kernel,padding,stride)
            
            rgb = np.dstack([c_r, c_g, c_b]) #Then merging red, green and blue channels to get a RGB image back

            return rgb
        
        #You can click on drop button to blur the image
        def blur():
            #Gaussian filter 5x5 sigma is 1
            filter = np.array([[1,4,7,4,1],[4,16,26,16,4],[7,26,41,26,7],[4,16,26,16,4],[1,4,7,4,1]])/273 
            self.final_image = conv_color(self.final_image, filter, 1, 1).astype(np.uint8) #I applied convolution to image with gaussian blur kernel
            show_picture(self.final_image)
        
        #You can click on reset button to go back the image that you uploaded
        def reset():
            self.final_image = self.original_image
            show_picture(self.final_image)
        
        #You can click on floppy disk button to save the image on the pictureBox
        def save_image():
            image = self.pictureBox.pixmap().toImage() #Taking image on the pictureBox
            file_dialog = QFileDialog.getSaveFileName(None, 'Save Image', 'edited_image.jpg',  "Images (*.png *.jpg *.jpeg)") #Select a path to save the image
            image.save(file_dialog[0])
        
        #This methods saves the specified image into the path by using imwrite function in opencv.
        def save_img(image, path):
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            cv2.imwrite(path, image)
        
        #This method flips the image according to X axis
        def flipX(image):
            n_H, n_W, n_C = image.shape
            new_image = np.zeros_like(image)
            for h in range(n_H):
                for w in range(n_W):
                    for c in range(n_C):
                        #When a coordinate flip according to x axis, y value changes
                        new_image[h, w, c] = image[h, n_W - w - 1, c]
            return new_image
        
        #This method flips the image according to Y axis
        def flipY(image):
            n_H, n_W, n_C = image.shape
            new_image = np.zeros_like(image)
            for h in range(n_H):
                for w in range(n_W):
                    for c in range(n_C):
                        #When we want to flip a coordinate according to Y axis, we change only x value.
                        new_image[h, w, c] = image[n_H - h - 1, w , c]
            return new_image
        
        #Click on vertical flip button to flip the image.
        def flipVertical():
            self.final_image = flipX(self.final_image)
            show_picture(self.final_image)

        #Click on horizontal flip button to flip the image.    
        def flipHorizontal():
            self.final_image = flipY(self.final_image)
            show_picture(self.final_image)
        
        #This method changes the brightness of the image according to value parameter.
        def brightness_image(image, value):
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #I convert the BGR image to HSV image because I can change the brightness(value) of the image basically.
            hue, sat, val = cv2.split(hsv)

            val = cv2.add(val, value) #I add the value param to brightness of the image

            #If v is greater than 255, assign 255 to v
            #If v is less than 0, assign 0 to v 
            val[val > 255] = 255
            val[val < 0] = 0

            new_hsv = cv2.merge((hue, sat, val)) #Merging H, S and V
            new_image = cv2.cvtColor(new_hsv, cv2.COLOR_HSV2BGR) #Converting HSV image to BGR back
            return new_image
        
        #You can slide the brighten slider
        def bright():
            #The slider value is too high, so I divided it by 20.
            self.final_image = brightness_image(self.final_image, int(self.brighterSlider.value()/20))
            show_picture(self.final_image)
            
        #You can slide the darken slider
        def dark():
            #The slider value is too high, so I divided it by 20.
            #I want to darken the image in this method, so the value parameter is going to be negative.
            self.final_image = brightness_image(self.final_image, -int(self.darkerSlider.value()/20))
            show_picture(self.final_image)
        
        #This methods changes contrast of an image according to alpha and beta values.
        def contrast(image, alpha, beta = 0):
            #I wanted to write contrast function from scratch too, but it is too slow when I use my own codes.
            #It makes the program freezed for a while
            """ 
            n_W, n_H, n_C = image.shape
            new_image = np.zeros_like(image)
            for w in range(n_W):
                for h in range(n_H):
                    for c in range(n_C):
                        value = image[w, h, c]
                        new_value = alpha*value+beta
                        if new_value > 255:
                            new_value = 255
                        elif new_value < 0:
                            new_value = 0
                        new_image[w, h, c] = new_value
            return new_image
            """
            #I used opencv's convenience method for increasing and decreasing contrast of the image because this is deathly faster than mine.
            return cv2.addWeighted(image, alpha, np.zeros(image.shape, image.dtype), 0, beta)
        
        #You can slide the increase contrast slider
        def increase_contrast():
            #When the slider value is 0 the image will be full black, so I added 1 to alpha. The slider value is too high, so I divived it by 100.
            alpha = 1 + self.incContrastSlider.value()/100.0
            #beta value is for brightness but it makes the contrast better
            beta = 1
            self.final_image = contrast(self.final_image, alpha, beta)
            show_picture(self.final_image)
            
        #You can slide the decrease contrast slider
        def decrease_contrast():
            alpha = 1 + self.incContrastSlider.value()/100.0
            beta = 1
            #I passed 1/a and -b/a to contrast function because I applied reverse of increasing contrast. n = a*x+b  x = (n-b)/a = n*1/a -b/a
            self.final_image = contrast(self.final_image, 1/alpha, -beta/alpha)
            show_picture(self.final_image)

        def rotate_image(image, angle):
            (h, w,c) = image.shape
            (centerX, centerY) = (w // 2, h // 2) #Calculating center coordinate
            
            M = cv2.getRotationMatrix2D((centerX, centerY), -angle, 1.0) #Creating rotationmatrix by using open cv function
            cos = np.abs(M[0, 0]) #Cos(angle)
            sin = np.abs(M[0, 1]) #Sin(angle)
            #New width and height values.
            nW = int((h * sin) + (w * cos))
            nH = int((h * cos) + (w * sin))
            M[0, 2] += (nW / 2) - centerX #Calculating new points
            M[1, 2] += (nH / 2) - centerY
            return cv2.warpAffine(image, M, (nW, nH)) #Rotating image and assigning it to image with the new width and height 
        
        #Firstly enter a degree into textBox then click on rotate button.
        def rotate():
            if not self.degreeBox.text(): #If the textbox is empty show a messagebox
                message_box("Empty Error", "You must enter a degree!")
            else:
                self.final_image = rotate_image(self.final_image, int(self.degreeBox.text())).astype(np.uint8) #Rotate the image according to textbox value
                show_picture(self.final_image)

        # Artistic Filters and Effects        

        def sepia(image):
            #Sebia filter
            filter = np.array([[272, 534, 131],
                               [349, 686, 168],
                               [393, 769, 189]])/1000
            #filter2D is a basic convolution process. My own conv function works too but it is too slow.
            return cv2.filter2D(self.final_image, -1, filter)

        #Sepia button event
        def sepia_effect():
            self.final_image = sepia(self.final_image)
            show_picture(self.final_image)

        def sketch(image):
            #I used pencilSketch function for sketch effect. I found value of the arguments by trying. 
            #These values are good for images generally.
            gray_sketch, color_sketch = cv2.pencilSketch(image, sigma_s = 100, sigma_r = 0.04, shade_factor = 0.2)
            return color_sketch

        #Sketch button event
        def sketch_effect():
            self.final_image = sketch(self.final_image)
            show_picture(self.final_image)

        def emboss(image):
            #Emboss filter
            filter = np.array([[0, -1, -1],
                               [1, 0, -1],
                               [1, 1, 0]])
            return cv2.filter2D(self.final_image, -1, filter)

        #Emboss button event
        def emboss_effect():
            self.final_image = emboss(self.final_image)
            show_picture(self.final_image)

        def shriveled_paper(image):
            #normalizing image by dividing it by 255
            img = image.astype("float32")/255.0
            h, w, c  = img.shape

            #reading crumpled paper image as gray and then normalizing it
            crumpled = cv2.imread('images/crumpled_paper.jpg', 0).astype("float32") / 255.0

            #resize crumpled image to same size with image given to this function
            crumpled  = cv2.resize(crumpled , (w, h))

            #applying linear transform to stretch crumpled image and to make it shade derker. 
            #1.33 and -0.33 numbers are from an equation.
            crumpled  = 1.33 * crumpled  -0.33

            #threshold crumpled image and inverting it
            threshold = cv2.thresholdold(crumpled ,0.5,1,cv2.THRESH_BINARY)[1]
            threshold = cv2.cvtColor(threshold,cv2.COLOR_GRAY2BGR) 
            threshold_inverse = 1-threshold

            #Brighting crumpled image 
            mean = np.mean(crumpled)
            shift = mean - 0.5
            crumpled  = cv2.subtract(crumpled , shift)

            #cumpled image was gray so I converted it to BGR back.
            crumpled  = cv2.cvtColor(crumpled , cv2.COLOR_GRAY2BGR) 

            #Hard light composite
            low = 2.0 * img * crumpled 
            high = 1 - 2.0 * (1 - img) * (1 - crumpled)
            new_image = 255 * (low * threshold_inverse + high * threshold)
            return new_image.clip(0, 255).astype(np.uint8) #Taking image in range 0 to 255 as int

        #Shriveled Paper button event
        def shriveled_paper_effect():
            self.final_image = shriveled_paper(self.final_image)
            show_picture(self.final_image)

        def cartoon(image):
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 7) #median blur with kernel size 7
            edges2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7) #thick lines
            dst = cv2.edgePreservingFilter(image, flags = 2, sigma_s = 55, sigma_r = 0.3) #it is like bilateral filter. I found the values by trying.
            cartoon2 = cv2.bitwise_and(dst, dst, mask = edges2) #smooth image and edged image are merging.
            return cartoon2

        def cartoon_effect():
            self.final_image = cartoon(self.final_image)
            show_picture(self.final_image)

        def daylight(image):
            #Firstly I tried it with HSV, but it is not as good as HLS. 
            hls_image = cv2.cvtColor(image,cv2.COLOR_BGR2HLS) #converting image to HLS
            hls_image = np.array(hls_image, dtype = np.float64)
            daylight = 1.2
            hls_image[:,:,1] = hls_image[:,:,1] * daylight # L(light) values are multiplying by daylight variable
            hls_image[:,:,1][hls_image[:,:,1]>255] = 255 # If a value is greater than 255, that value is going to be 255
            hls_image = np.array(hls_image, dtype = np.uint8)
            image_RGB = cv2.cvtColor(hls_image,cv2.COLOR_HLS2BGR) # Converting hls image to BGR back
            return image_RGB

        #Daylight button event
        def daylight_effect():
            self.final_image = daylight(self.final_image)
            show_picture(self.final_image)

        def soul(image):
            #I applied some colormaps to image. I found them randomly they are not special. Then I used sharpening filter.
            image = cv2.applyColorMap(image, cv2.COLORMAP_BONE)
            image = cv2.applyColorMap(image, cv2.COLORMAP_HOT)
            filter = np.array([[-1, -1, -1], 
                               [-1, 9, -1], 
                               [-1, -1, -1]])
            return cv2.filter2D(image, -1, filter)

        def soul_effect():
            self.final_image = soul(self.final_image)
            show_picture(self.final_image)


        def pixelizer(image):
            height, width, channel = image.shape
            #Pixel size
            w, h = (32, 32)

            # Resizing giving image to same with pixel size
            temp = cv2.resize(image, (w, h), interpolation=cv2.INTER_LINEAR)

            #Resizing image to original size again
            return cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

        #Pixelizer button event
        def pixelizer_effect():
            self.final_image = pixelizer(self.final_image)
            show_picture(self.final_image)

        def angel(image):
            #I tried this filter on images and it brights the images.
            filter = np.array([[1, 1, 1], 
                               [0, 0, 0], 
                               [1, 1, 1]])/3
            return cv2.filter2D(image, -1, filter)

        def angel_effect():
            self.final_image = angel(self.final_image)
            show_picture(self.final_image)

        def devil(image):
            #I applied a colormap to the image first
            image1 = cv2.applyColorMap(image, cv2.COLORMAP_OCEAN)
            #I found this filter by trying very different numbers. 
            #It is like edge detection filter, but it looks cooler than normal edge detection.
            #Then I merged them with bitwise and.
            filter = np.array([[-1, -2, -3], 
                               [-2, -4, -6], 
                               [4, 5, 8]])*1024
            image2 = cv2.filter2D(image, -1, filter)
            return cv2.bitwise_and(image1, image2)

        #Devil button event
        def devil_effect():
            self.final_image = devil(self.final_image)
            show_picture(self.final_image)
        
        #Event assignments for pictureBox
        self.pictureBox.mousePressEvent = mousePressEvent
        self.pictureBox.mouseMoveEvent = mouseMoveEvent
        self.pictureBox.mouseReleaseEvent = mouseReleaseEvent
        
        #Button events
        
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

        self.incContrastSlider.valueChanged.connect(increase_contrast)
        self.decContrastSlider.valueChanged.connect(decrease_contrast)

        self.rotateButton.clicked.connect(rotate)

        self.button1.clicked.connect(sepia_effect)
        self.button2.clicked.connect(sketch_effect)
        self.button3.clicked.connect(emboss_effect)
        self.button4.clicked.connect(shriveled_paper_effect)
        self.button5.clicked.connect(cartoon_effect)
        self.button6.clicked.connect(daylight_effect)  
        self.button7.clicked.connect(soul_effect)  
        self.button8.clicked.connect(pixelizer_effect)
        self.button9.clicked.connect(angel_effect)
        self.button10.clicked.connect(devil_effect)

        # ----------END----------


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
