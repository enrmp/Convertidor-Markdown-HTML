# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget, QSystemTrayIcon)

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(929, 685)
        icon = QIcon()
        icon.addFile(u"icon_app.png", QSize(), QIcon.Normal, QIcon.Off)

        tray=QSystemTrayIcon()
        tray.setIcon(icon)
        tray.setVisible(True)

        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color:#fff;")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.actionGuardar_archivo_markdown = QAction(MainWindow)
        self.actionGuardar_archivo_markdown.setObjectName(u"actionGuardar_archivo_markdown")
        self.actionGuardar_HTML_generado = QAction(MainWindow)
        self.actionGuardar_HTML_generado.setObjectName(u"actionGuardar_HTML_generado")
        self.actionChangeLanguage = QAction(MainWindow)
        self.actionChangeLanguage.setObjectName(u"actionChangeLanguage")
        self.actionChangeLanguage.setCheckable(False)
        self.actionEspa_ol = QAction(MainWindow)
        self.actionEspa_ol.setObjectName(u"actionEspa_ol")
        self.actionEspa_ol.setCheckable(False)
        self.actionEspa_ol.setChecked(False)
        self.actionCopiar = QAction(MainWindow)
        self.actionCopiar.setObjectName(u"actionCopiar")
        self.actionCortar = QAction(MainWindow)
        self.actionCortar.setObjectName(u"actionCortar")
        self.actionPegar = QAction(MainWindow)
        self.actionPegar.setObjectName(u"actionPegar")
        self.actionDeshacer = QAction(MainWindow)
        self.actionDeshacer.setObjectName(u"actionDeshacer")
        self.actionRehacer = QAction(MainWindow)
        self.actionRehacer.setObjectName(u"actionRehacer")
        self.actionConvertir_a_HTML = QAction(MainWindow)
        self.actionConvertir_a_HTML.setObjectName(u"actionConvertir_a_HTML")
        self.actionLimpiar_texto = QAction(MainWindow)
        self.actionLimpiar_texto.setObjectName(u"actionLimpiar_texto")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.centralWidget = QFrame(self.centralwidget)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setFrameShape(QFrame.StyledPanel)
        self.centralWidget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.backgroundFrame = QFrame(self.centralWidget)
        self.backgroundFrame.setObjectName(u"backgroundFrame")
        self.backgroundFrame.setStyleSheet(u"background-color:#fff;")
        self.backgroundFrame.setFrameShape(QFrame.StyledPanel)
        self.backgroundFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.backgroundFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contentFrame = QFrame(self.backgroundFrame)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setFrameShape(QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.contentFrame)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setEnabled(True)
        self.topBar.setMaximumSize(QSize(16777215, 60))
        self.topBar.setStyleSheet(u"background-color:#fff;")
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.topBar)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.titleFrame = QFrame(self.topBar)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.titleFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.titleFrame)
        self.title.setObjectName(u"title")
        palette = QPalette()
        brush = QBrush(QColor(34, 34, 34, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.title.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Akzidenz-Grotesk BQ Extended"])
        font.setPointSize(12)
        font.setBold(False)
        self.title.setFont(font)
        self.title.setToolTipDuration(-2)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet(u"color:#222; text-transform:uppercase;")
        self.title.setScaledContents(False)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.title)


        self.verticalLayout_5.addWidget(self.titleFrame)


        self.verticalLayout_4.addWidget(self.topBar)

        self.translatorFrame = QFrame(self.contentFrame)
        self.translatorFrame.setObjectName(u"translatorFrame")
        self.translatorFrame.setStyleSheet(u"border-top:.5px solid #222;background-color:#f4f4f4;")
        self.translatorFrame.setFrameShape(QFrame.NoFrame)
        self.translatorFrame.setFrameShadow(QFrame.Raised)
        self.translatorFrame.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.translatorFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.markdownFrame = QFrame(self.translatorFrame)
        self.markdownFrame.setObjectName(u"markdownFrame")
        self.markdownFrame.setStyleSheet(u"border:none;\n"
"border-right: .5px solid #222; border-bottom: .5px solid #222; ")
        self.markdownFrame.setFrameShape(QFrame.NoFrame)
        self.markdownFrame.setFrameShadow(QFrame.Plain)
        self.markdownFrame.setLineWidth(0)
        self.markdownInput = QPlainTextEdit(self.markdownFrame)
        self.markdownInput.setObjectName(u"markdownInput")
        self.markdownInput.setGeometry(QRect(11, 12, 256, 192))
        font1 = QFont()
        font1.setFamilies([u"Helvetica Neue LT Pro"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.markdownInput.setFont(font1)
        self.markdownInput.setStyleSheet(u"border:none;")
        self.markdownInput.setLineWidth(0)

        self.horizontalLayout.addWidget(self.markdownFrame)

        self.HTMLFrame = QFrame(self.translatorFrame)
        self.HTMLFrame.setObjectName(u"HTMLFrame")
        self.HTMLFrame.setStyleSheet(u"border:none; border-bottom:.5px solid #222;")
        self.HTMLFrame.setFrameShape(QFrame.NoFrame)
        self.HTMLFrame.setFrameShadow(QFrame.Raised)
        self.HTMLFrame.setLineWidth(0)
        self.gridLayout_3 = QGridLayout(self.HTMLFrame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.htmlInput = QWebEngineView(self.HTMLFrame)
        self.htmlInput.setObjectName(u"htmlInput")
        self.htmlInput.setStyleSheet(u"border:none;")

        self.gridLayout_3.addWidget(self.htmlInput, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.HTMLFrame)


        self.verticalLayout_4.addWidget(self.translatorFrame)

        self.buttonsFrame = QFrame(self.contentFrame)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setMaximumSize(QSize(16777215, 50))
        self.buttonsFrame.setFrameShape(QFrame.NoFrame)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.buttonsFrame.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.translateButtonFrame = QFrame(self.buttonsFrame)
        self.translateButtonFrame.setObjectName(u"translateButtonFrame")
        self.translateButtonFrame.setMinimumSize(QSize(0, 50))
        self.translateButtonFrame.setMaximumSize(QSize(16777215, 50))
        self.translateButtonFrame.setStyleSheet(u" border-right: .5px solid #222 !important;")
        self.translateButtonFrame.setFrameShape(QFrame.NoFrame)
        self.translateButtonFrame.setFrameShadow(QFrame.Raised)
        self.translateButtonFrame.setLineWidth(0)
        self.gridLayout = QGridLayout(self.translateButtonFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.translateButtonFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setFamilies([u"Akzidenz-Grotesk BQ Extended"])
        self.pushButton.setFont(font2)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setFocusPolicy(Qt.NoFocus)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton {\n"
"background-color: #fff !important;\n"
"border:none;\n"
"border-right:.5px solid #222;\n"
"border-bottom:.5px solid #222;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"background-color: #373737;  \n"
"color: #fff;\n"
"border:none; \n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"background-color: #111;  \n"
"color: #fff;\n"
"border:none;   \n"
"\n"
"}")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setFlat(False)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.translateButtonFrame)

        self.clearButtonFrame = QFrame(self.buttonsFrame)
        self.clearButtonFrame.setObjectName(u"clearButtonFrame")
        self.clearButtonFrame.setMinimumSize(QSize(0, 50))
        self.clearButtonFrame.setStyleSheet(u"")
        self.clearButtonFrame.setFrameShape(QFrame.NoFrame)
        self.clearButtonFrame.setFrameShadow(QFrame.Plain)
        self.clearButtonFrame.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.clearButtonFrame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.clearButton = QPushButton(self.clearButtonFrame)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setMaximumSize(QSize(16777215, 50))
        self.clearButton.setFont(font2)
        self.clearButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.clearButton.setMouseTracking(True)
        self.clearButton.setFocusPolicy(Qt.NoFocus)
        self.clearButton.setAutoFillBackground(False)
        self.clearButton.setStyleSheet(u"QPushButton#clearButton {\n"
"background-color: #fff !important;\n"
"border:none;\n"
"border-bottom:.5px solid #222;\n"
"}\n"
"\n"
"QPushButton#clearButton:hover {\n"
"background-color: #373737;  \n"
"color: #fff;\n"
"border:none; \n"
"\n"
"}\n"
"\n"
"QPushButton#clearButton:pressed {\n"
"background-color: #111;  \n"
"color: #fff;\n"
"border:none;   \n"
"\n"
"}")
        self.clearButton.setCheckable(False)
        self.clearButton.setAutoDefault(True)
        self.clearButton.setFlat(False)

        self.gridLayout_2.addWidget(self.clearButton, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.clearButtonFrame)


        self.verticalLayout_4.addWidget(self.buttonsFrame)


        self.verticalLayout_3.addWidget(self.contentFrame)


        self.verticalLayout_2.addWidget(self.backgroundFrame)


        self.gridLayout_4.addWidget(self.centralWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 929, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuEdici_n = QMenu(self.menubar)
        self.menuEdici_n.setObjectName(u"menuEdici_n")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEdici_n.menuAction())
        self.menuArchivo.addAction(self.actionGuardar_archivo_markdown)
        self.menuArchivo.addAction(self.actionGuardar_HTML_generado)
        self.menuEdici_n.addAction(self.actionDeshacer)
        self.menuEdici_n.addAction(self.actionRehacer)
        self.menuEdici_n.addSeparator()
        self.menuEdici_n.addAction(self.actionCortar)
        self.menuEdici_n.addAction(self.actionCopiar)
        self.menuEdici_n.addAction(self.actionPegar)
        self.menuEdici_n.addSeparator()
        self.menuEdici_n.addAction(self.actionConvertir_a_HTML)
        self.menuEdici_n.addAction(self.actionLimpiar_texto)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)
        self.clearButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Conversor de Markdown a HTML", None))
        self.actionGuardar_archivo_markdown.setText(QCoreApplication.translate("MainWindow", u"Guardar archivo markdown", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar_archivo_markdown.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar_HTML_generado.setText(QCoreApplication.translate("MainWindow", u"Guardar HTML generado", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar_HTML_generado.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actionChangeLanguage.setText(QCoreApplication.translate("MainWindow", u"Ingl\u00e9s", None))
        self.actionEspa_ol.setText(QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.actionCopiar.setText(QCoreApplication.translate("MainWindow", u"Copiar", None))
#if QT_CONFIG(shortcut)
        self.actionCopiar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionCortar.setText(QCoreApplication.translate("MainWindow", u"Cortar", None))
#if QT_CONFIG(shortcut)
        self.actionCortar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionPegar.setText(QCoreApplication.translate("MainWindow", u"Pegar", None))
#if QT_CONFIG(shortcut)
        self.actionPegar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionDeshacer.setText(QCoreApplication.translate("MainWindow", u"Deshacer", None))
#if QT_CONFIG(shortcut)
        self.actionDeshacer.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRehacer.setText(QCoreApplication.translate("MainWindow", u"Rehacer", None))
#if QT_CONFIG(shortcut)
        self.actionRehacer.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Y", None))
#endif // QT_CONFIG(shortcut)
        self.actionConvertir_a_HTML.setText(QCoreApplication.translate("MainWindow", u"Convertir a HTML", None))
#if QT_CONFIG(shortcut)
        self.actionConvertir_a_HTML.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionLimpiar_texto.setText(QCoreApplication.translate("MainWindow", u"Limpiar texto", None))
#if QT_CONFIG(shortcut)
        self.actionLimpiar_texto.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.title.setText(QCoreApplication.translate("MainWindow", u"Conversor de Markdown a HTML", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Pulsa para traducir tu markdown a HTML", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"TRADUCIR A HTML", None))
#if QT_CONFIG(tooltip)
        self.clearButton.setToolTip(QCoreApplication.translate("MainWindow", u"Pulsa para borrar el texto", None))
#endif // QT_CONFIG(tooltip)
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR TEXTO", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuEdici_n.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
    # retranslateUi

