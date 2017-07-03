# -*-coding: utf-8 -*-
from PyQt4.QtGui import*
from PyQt4.QtCore import*

from PyQt4 import QtSql
import sys,sqlite3,os
class mainprogram(QMainWindow):
        def __init__(self, parent=None):
            super(mainprogram, self).__init__(parent)
            try:
                self.vb=sqlite3.connect("database/carbase.db")
                self.query=self.vb.cursor()
                self.query.execute("""CREATE TABLE panel(panel_marc,panel_number,panel_company ,panel_year,panel_defect,panel_date,panel_info)""")
                self.vb.commit()
                self.vb=QtSql.QSqlDatabase.addDatabase("QSQLITE")
                self.vb.setDatabaseName("database/carbase.db")
                self.query=QtSql.QSqlQuery()
                self.query.exec_("CREATE TABLE panel(panel_marc,panel_number,panel_company ,panel_year,panel_defect,panel_date,panel_info)")
                self.vb.commit()
                self.model = QtSql.QSqlTableModel()
                self.model.setTable('panel')
                self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
                self.model.select()
                self.model.setHeaderData(0,Qt.Horizontal,u"Markası")
                self.model.setHeaderData(1, Qt.Horizontal, u"Nömrə nişanı")
                self.model.setHeaderData(2, Qt.Horizontal, u"Şirkət")
                self.model.setHeaderData(3, Qt.Horizontal, u"Buraxılış ili")
                self.model.setHeaderData(4, Qt.Horizontal, u"Qəzası")
                self.model.setHeaderData(5, Qt.Horizontal, u"Tarix")
                self.model.setHeaderData(6, Qt.Horizontal, u"Əlavə qeydlər")
                self.view = QTableView()
                self.view.setModel(self.model)
                self.view.setWindowTitle("Bazada olanlar")
            except sqlite3.OperationalError:
                self.vb=sqlite3.connect("database/carbase.db")
                self.vb=QtSql.QSqlDatabase.addDatabase("QSQLITE")
                self.vb.setDatabaseName("database/carbase.db")
                self.query=QtSql.QSqlQuery()
                self.query.exec_("CREATE TABLE panel(panel_marc,panel_number,panel_company ,panel_year,panel_defect,panel_date,panel_info)")
                self.vb.commit()
                self.model = QtSql.QSqlTableModel()
                self.model.setTable('panel')
                self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
                self.model.select()
                self.model.setHeaderData(0,Qt.Horizontal,u"Markası")
                self.model.setHeaderData(1, Qt.Horizontal, u"Nömrə nişanı")
                self.model.setHeaderData(2, Qt.Horizontal, u"Şirkət")
                self.model.setHeaderData(3, Qt.Horizontal, u"Buraxılış ili")
                self.model.setHeaderData(4, Qt.Horizontal, u"Qəzası")
                self.model.setHeaderData(5, Qt.Horizontal, u"Tarix")
                self.model.setHeaderData(6, Qt.Horizontal, u"Əlavə qeydlər")
                self.view = QTableView()
                self.view.setModel(self.model)
                self.view.setWindowTitle("Bazada olanlar")
            self.setWindowTitle(u"Service")
            self.setWindowIcon(QIcon(u"image/database2.JPG"))
            self.setGeometry(100,80,1300,800)
            self.setFixedSize(1300,800)
            self.setStyleSheet("background-color:white;")
            self.toolbar=self.addToolBar('')
            self.toolbar.setMovable(False)
            params=QAction(u"Parametrlər",self)
            params.triggered.connect(self.setting)
            about=QAction(u"Haqqımızda",self)
            about.triggered.connect(self.about)
            exit=QAction(u"Çıxış",self)
            exit.triggered.connect(self.exiting)
            self.toolbar.addAction(params)
            
            self.toolbar.addAction(about)
            self.toolbar.addAction(exit)
            #----------------------------------------------
            self.tab=QTabWidget(self)
            self.tab.resize(1300,800)
            self.tab.move(0,30)
            self.tab.setStyleSheet(
                                "border-style: outset;"
                                "border-width:0.5px;"
                                "border-radius: 5px;"
                                "border-color: green;"
                                
                                 )
            self.tab_baza=QWidget()
            self.tab_bazas=QMainWindow()
            self.tab.addTab(self.tab_baza,u"Data")
            self.tab.addTab(self.tab_bazas,u"Baza")
            self.tab_bazas.setStyleSheet("background-color:white;")
            self.tab_video=QMainWindow()
            self.tab.addTab(self.tab_video,u"Video")
            """palette=QPalette()
            palette.setBrush(QPalette.Background,QBrush(QPixmap("image/database1.jpg")))
            self.setPalette(palette)"""

            #---------------------------------------------------------------------
                        
            
            
            
            self.label_table=QLabel(self.tab_baza)
            self.label_table.setText(u"""
    Avtomobil markası\tNömrə nişanı\tŞirkət adı\tBuraxılış ili\t   Qəzası\t Tarix
    """)  
            
            self.label_table.setStyleSheet("color:#000080;"
                                        "font-size:12pt;"
                                        "font-family:Courier;")
            self.label_table.move(10,50)
            #--------------------------------------------------------------------
            self.combo_carname=QComboBox(self.tab_baza)
            self.combo_carname.setGeometry(50,100,170,20)
            self.combo_carname.setToolTip(u"avtomobil adı və ya markasını seçin")
            self.combo_carname.addItems(["--Select--","ACG Cars","ATV","Acura","Alfa Romeo","Aprillia","Audi","Aton Martin","Asia","BMC","BMV","BYD","BAIC","Bentley","Brilliance","Buick","CF","CZ","Cadillac","Can-Am","Changan","Cherry","Chevrolet","Chrysler","Citroen","DAF","Dacia","Daewoo","Dnepr","FAW","FIAT","Ford","Foton","Gem Cars","GMC","Gaz","Howo","Hafei","Hisun","Honda","Hummer","Hyundai","IJ","Ikarus","Iran Kodro","Isuzu","ItalCar","Iveco","JAC","JMC","JEEP","Jonway","Kavz","Kamaz","Kia","Kinroad","KrAz","LADA(Vaz)","Land Rover","Lexus","LuAz","MAN","MAZ","MAZDA","Mercedes","Mitsubishi","Moskvic","Muravey","Neoplan","Nissan","Opel","PAZ","RAF","Scania","Skoda","Tofas","Toyoto","UAZ","URAL","VESPA","Volkswagen","Volvo","Vosxod","Yamaha","Zaz","ZIL","ZX Auto","Other"])
            self.combo_carname.setStyleSheet("color:green;"
                                            "font-size:10pt;"
                                            "font-family:Courier;")
            #--------------------------------------------------------------------
            self.line_carnumber=QLineEdit(self.tab_baza)
            self.line_carnumber.setGeometry(250,100,120,20)
            self.line_carnumber.setToolTip(u"Avtomobil nömrəsi-10-HB-219")
            self.line_carnumber.setStyleSheet("font-size:10pt;"
                                              "font-family:Courier;"
                                              "color:green")
            self.line_carnumber.cursorPositionChanged.connect(self.activation)


            #-------------------------------------------------------------
            self.line_company=QLineEdit(self.tab_baza)
            self.line_company.setGeometry(400,100,150,20)
            self.line_company.setToolTip(u"Hansı şirkətin tərkibindədir")
            self.line_company.setStyleSheet("font-size:10pt;"
                                              "font-family:Courier;"
                                              "color:green")
            #----------------------------------------------------------------------
            self.combo_caryear=QComboBox(self.tab_baza)
            self.combo_caryear.setGeometry(570,100,130,20)
            self.combo_caryear.setToolTip(u"Avtomobilin buraxılış ili")
            self.combo_caryear.addItem("--Select--")
            for i in range(1980,2018):

                self.combo_caryear.addItem(str(i))
            self.combo_caryear.setStyleSheet("font-size:10pt;"
                                            "color:black;"
                                            "font-family:Courier;")
            #----------------------------------------------------------
            self.combo_cardefect=QComboBox(self.tab_baza)
            self.combo_cardefect.setGeometry(750,100,100,20)
            self.combo_cardefect.addItems(["--Select--",u"Qəzalı",u"Qəzasız"])
            self.combo_cardefect.setStyleSheet("font-size:10pt;"
                                                "color:green;"
                                                "font-family:Courier;")
            #-----------------------------------------------
            self.line_date=QLineEdit(self.tab_baza)
            self.line_date.setGeometry(900,100,130,20)
            self.line_date.setStyleSheet("color:green;"
                                        "font-size:10pt;") 
            self.line_date.setInputMask("99.99.9999") 
            self.line_date.setToolTip(u"Tarixi,gün.ay.il uyğunluqla yazın")
            #--------------------------------------------------------------
            self.frame=QFrame(self.tab_baza)
            self.frame.setGeometry(45,150,985,40)
            self.frame.setStyleSheet("background-color:gray;")
            self.button_apply=QPushButton(u"Təchiz et",self.frame)
            self.button_apply.setGeometry(705,10,100,25)
            self.button_apply.setToolTip(u"Verilənləri bazaya əlavə etmək üçün yuxarıdakı qutuları doldurun")  
            self.button_apply.setEnabled(False) 
            self.button_apply.setStyleSheet("background-color:green;"
                                            "color:black;")
            self.button_apply.clicked.connect(self.applying)  
            self.button_delete=QPushButton(u"Sil",self.frame)
            self.button_delete.setGeometry(855,10,100,25)  
            self.button_delete.clicked.connect(self.deleting)             
            #------------------------------------------------------------------------------


            
            #-------------Button-baza------------------------
            self.button_adrow=QPushButton(u"Sütun əlavə et",self.tab_bazas)
            self.button_adrow.setGeometry(20,570,150,25)
            self.button_adrow.clicked.connect(self.addingrow)
            self.button_delrow=QPushButton(u"Sütun sil",self.tab_bazas)
            self.button_delrow.setGeometry(180,570,150,25)
            self.button_delrow.clicked.connect(self.delrow)
            #-------Button-print---------------------------
            self.button_print=QPushButton(u"Çap et",self.tab_bazas)
            self.button_print.setGeometry(340,570,100,25)
            self.button_print.clicked.connect(self.printer)
            #-----------------------------------------------
            self.button_reload=QPushButton(u"Yenilə",self.tab_bazas)
            self.button_reload.setGeometry(450,570,100,25)
            self.button_reload.clicked.connect(self.reload)
            #-----------------------------------------------
            self.view=QTableView(self.tab_bazas)
            self.view.setGeometry(10,50,1150,500)
            self.view.setModel(self.model)
            self.view.horizontalHeader().setResizeMode(QHeaderView.Stretch)
            self.view.setStyleSheet("selection-background-color:#84C1FF;"
                                    "color:black;"
                                    "selection-color:#0069D2;"
                                    "border-color:blue;")
            
            """
            for row in range(0,2000):
                combo=QComboBox()
                v=self.view.model().index(row,4)
                self.view.setIndexWidget(v,combo)
            """


            
            self.show()
        def setting(self):
            self.setw=QWidget()
            self.setw.setWindowTitle(u"Parametrlər")
            self.setw.setGeometry(200,300,220,100)
            self.setw.setFixedSize(220,100)
            self.tab_param=QTabWidget(self.setw)
            self.tab_param.resize(220,100)
            self.tab_param.setStyleSheet(
                                "border-style: outset;"
                                "border-width:0.5px;"
                                "border-radius: 5px;"
                                "border-color: white;"
                                
                                 )
            self.tab_font=QWidget()
            self.tab_color=QWidget()
            self.tab_bgcolor=QWidget()
            self.tab_param.addTab(self.tab_font,u"Font")
            self.tab_param.addTab(self.tab_color,u"Yazı rəngi")
            self.tab_param.addTab(self.tab_bgcolor,u"Arxa Plan rəngi")
            #--------------------------------------------------------
            self.button=QPushButton(self.tab_font)
            self.button.setText("Font")
            self.button.setGeometry(40,40,120,25)
            self.button.setStyleSheet("background-color:green;"
                                      "color:black;")
            self.button.clicked.connect(self.basefont)
            self.button=QPushButton(self.tab_color)
            self.button.setText(u"Yazı rəngi")
            self.button.setGeometry(40,40,120,25)
            self.button.setStyleSheet("background-color:green;"
                                      "color:black;")
            self.button.clicked.connect(self.basecolor)
            self.button=QPushButton(self.tab_bgcolor)
            self.button.setText(u"Arxa plan rəngi")
            self.button.setGeometry(40,40,120,25)
            self.button.setStyleSheet("background-color:green;"
                                      "color:black;")
            self.button.clicked.connect(self.basebgcolor)
            self.setw.show()
        def basebgcolor(self):
            color=QColorDialog.getColor()
            self.view.setStyleSheet("background-color:%s"%color.name())
        def basecolor(self):
            color=QColorDialog.getColor()
            self.view.setStyleSheet("color:%s"%color.name())
        def basefont(self):
            font,ok=QFontDialog.getFont()
            if ok:
                self.view.setFont(font)
        def reload(self):
		
            
            os.system("python main.py")
            self.close()

        
        def about(self):
            self.about_widget=QWidget()
            self.about_widget.setWindowIcon(QIcon("image/about-us.JPG"))
            self.about_widget.setWindowTitle(u"Haqqımızda")
            self.about_widget.setGeometry(200,200,600,600)
            self.about_widget.setFixedSize(600,600)
            self.label=QLabel(self.about_widget)
            self.label.setText(u"""
        Versiya    1.0
        Müəllif    Rəşad Qarayev
        Əlaqə      pythonaz@yahoo.com
        © 2016     Techazweb 

        """ )
            self.label.setStyleSheet("font-family:Courier;"
                                     "font-size:10pt;"
                                     "color:green;")
            self.labelicon=QLabel(self.about_widget)
            photo=QPixmap(u"image/database2.JPG")
            self.labelicon.setPixmap(photo)
            self.labelicon.setGeometry(200,200,350,350)
            self.labellink=QLabel(self.about_widget)
            self.labellink.setText("Blog  <A href='www.techazweb.wordpress.com'>   techazweb  </a>")
            self.labellink.move(65,90)
            self.labellink.linkActivated.connect(self.clickme)
            self.about_widget.show()
        def clickme(self,event=None):
            import webbrowser
            webbrowser.open_new(r"https://techazweb.wordpress.com")

        
        def printer(self):
            printer=QPrinter()
            self.prt=QPrintDialog(printer,self.tab_baza)
            self.prt.exec_()
            self.view.render(printer)

        def colour(self,index):
            colo=QColorDialog.getColor()
            self.view.setBackground((Qt.QBrush(Qt.QColor("yellow"))))
            
        def addingrow(self):
            self.model.insertRow(self.model.rowCount())
        def delrow(self):
            self.model.removeRow(self.view.currentIndex().row())
            
        def exiting(self):
            self.close()
        def activation(self):
            if len(self.line_carnumber.text())>3:
                self.button_apply.setEnabled(True)
            elif len(self.line_carnumber.text())<0:
                self.button_apply.setEnabled(False)
        def applying(self,index):
            try:
                self.vb=sqlite3.connect("database/carbase.db")
                self.query=self.vb.cursor()
                self.query.execute("""CREATE TABLE panel(panel_marc,panel_number,panel_company ,panel_year,panel_defect,panel_date,panel_info)""")
                self.query.execute(u"""INSERT INTO panel VALUES('{}','{}','{}','{}','{}','{}','')""".format(self.combo_carname.currentText(),self.line_carnumber.text(),unicode(self.line_company.text()),self.combo_caryear.currentText(),self.combo_cardefect.currentText(),self.line_date.text()))
                self.vb.commit()
                self.message = QMessageBox()
                self.message.setWindowTitle("No internet connection")
                self.message = QMessageBox.question(self, u'Məlumat',u'Verilənlər bazaya əlavə olundu',QMessageBox.Ok)
                if self.message==QMessageBox.Ok:
                    pass
            except sqlite3.OperationalError:
                self.vb=sqlite3.connect("database/carbase.db")
                self.query=self.vb.cursor()
                self.query.execute(u"""INSERT INTO panel VALUES('{}','{}','{}','{}','{}','{}','')""".format(self.combo_carname.currentText(),self.line_carnumber.text(),unicode(self.line_company.text()),self.combo_caryear.currentText(),self.combo_cardefect.currentText(),self.line_date.text()))
                self.vb.commit()
                self.message = QMessageBox()
                self.message.setWindowTitle("No internet connection")
                self.message = QMessageBox.question(self, u'Məlumat',u'Verilənlər bazaya əlavə olundu',QMessageBox.Ok)
                if self.message==QMessageBox.Ok:
                    pass

        def deleting(self):
            self.combo_carname.setCurrentIndex(0)
            self.line_carnumber.clear()
            self.line_company.clear()
            self.combo_caryear.setCurrentIndex(0)
            self.combo_cardefect.setCurrentIndex(0)
            self.line_date.clear()
        
            
                    
if __name__ == '__main__':
    app = QApplication([])
    gui=mainprogram()
    app.exec_() 






