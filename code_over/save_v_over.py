from code_raw.save_v import Ui_MainWindow_Save_v
from googletrans import Translator
import time
from utils.file import read_v, save_v
from PyQt6 import QtCore
translate = Translator()

class Ui_MainWindow_Save_v_over(Ui_MainWindow_Save_v):
    def setupUi(self, MainWindow_Save_v):
        super().setupUi(MainWindow_Save_v)
        self.last_time = time.time()
        self.pushButton_add.clicked.connect(self.save)
        self.lineEdit_input.returnPressed.connect(self.save)


    def save(self):
        if time.time()-self.last_time<0.5:
            return
        self.last_time = time.time()
        text = self.lineEdit_input.text()
        if text is None or len(text)<=0:
            return
        text = text.lower()
        while text.find("  ")>=0:
            text = text.replace("  "," ")
        while text.endswith(" "):
            text = text[:-2]
        while text.startswith(" "):
            text = text[1:]
        _text  = ""
        for c in text:
            if  c!=" " and c!="'" and c!="-" and (c<"a" or c>"z"):
                continue
            _text+=c
        text = _text
        result = translate.translate(text, src='en', dest='vi')
        result = str(result.text)
      
        self.plainTextEdit_output.setPlainText(result)
        save_v(en = text,vn=result)
        data = read_v(text)
        self.plainTextEdit_output.setPlainText(f"{text}: {data.get('vn')} - {data.get('count')}")
        self.lineEdit_input.setText("")
            
        
        

        