from math import exp
from PySide6.QtWidgets import *
from views.main import MainWindow
import markdown

class MainWindowForm(QMainWindow, MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        clrButton=self.clearButton
        clrButton.clicked.connect(self.clearButtonAction)
        doButton=self.pushButton
        doButton.clicked.connect(self.pushButtonAction)
        exportHTML=self.actionGuardar_HTML_generado
        exportHTML.triggered.connect(self.saveHTML)
        exportMarkdowm=self.actionGuardar_archivo_markdown
        exportMarkdowm.triggered.connect(self.saveMarkdown)
        translateAction=self.actionConvertir_a_HTML
        translateAction.triggered.connect(self.pushButtonAction)
        clearAction=self.actionLimpiar_texto
        clearAction.triggered.connect(self.clearButtonAction)

    def clearButtonAction(self):
        input=self.markdownInput
        input.clear()
        output=self.htmlInput
        output.setHtml("")

    def pushButtonAction(self):
        input=self.markdownInput.toPlainText()
        output=self.htmlInput
        html=markdown.markdown(input)
        output.setHtml(html)
        output.show()

    def saveHTML(self):
        html=markdown.markdown(self.markdownInput.toPlainText())
        archivo=QFileDialog.getSaveFileName(self, self.actionGuardar_HTML_generado.text(),'untitled.html', 'HTML (*.html)')
        file_name = archivo[0]

        open(file_name, mode="w").write(html)

    def saveMarkdown(self):
        markdown=self.markdownInput.toPlainText()
        archivo=QFileDialog.getSaveFileName(self, self.actionGuardar_archivo_markdown.text(),'untitled.md', 'All Files(*);;Text Files(*.txt);;MarkDown (*.md)')
        file_name = archivo[0]

        open(file_name, mode="w").write(markdown)