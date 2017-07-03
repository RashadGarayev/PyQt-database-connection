# -*-coding: utf-8 -*-
from PyQt4.QtGui import*
from PyQt4.QtCore import*
from socket import gethostbyname, gaierror
from socket import *
from smtplib import SMTPException
from smtplib import SMTP
from json import load
from urllib2 import urlopen
from urllib2 import URLError
import sys,sqlite3,smtplib
import os





class window(QWidget):
        def __init__(self, parent=None):
            super(window, self).__init__(parent)
            self.setWindowTitle(u"Qeydiyyat")
            self.setWindowIcon(QIcon(u"image/qeydiyyat.JPG"))
            self.setGeometry(200,200,600,400)
            self.setFixedSize(600,400)
            self.setStyleSheet("background-color:white;")
            self.short=QShortcut(self)
            self.short.setKey(QKeySequence('Esc'))
            self.short.setContext(Qt.ApplicationShortcut)
            self.short.activated.connect(self.escape)
            #------------------------------------------------
            self.labelicon=QLabel(self)
            photo=QPixmap(u"image/qeydiyyat.JPG")
            self.labelicon.setPixmap(photo)
            self.labelicon.setGeometry(370,10,220,150)
            self.labellogin=QLabel(self)
            photo1=QPixmap(u"image/login1.png")
            self.labellogin.setPixmap(photo1)
            self.labellogin.setGeometry(370,240,220,150)
            self.label=QLabel(self)
            self.label.setText(u"""
    Ad\n
    Soyad\n
    Email*\n
    Şifrə*
    """)
            self.label.setStyleSheet("font-size:12pt;"
                                    "font-family:Courier;")
            self.line_name=QLineEdit(self)
            self.line_name.setToolTip(u"Adınızı yazın")
            self.line_name.setValidator(QRegExpValidator( QRegExp("[A-Za-z]{0,100}")))
            self.line_name.setMaxLength(14)
            self.line_name.move(130,20)
            self.line_surname=QLineEdit(self)
            self.line_surname.setToolTip(u"Soyadınızı yazın")
            self.line_surname.setValidator(QRegExpValidator( QRegExp("[A-Za-z]{0,100}")))
            self.line_surname.setMaxLength(14)
            self.line_surname.move(130,55)
            self.line_email=QLineEdit(self)
            self.line_email.setPlaceholderText("example@xxx.com")
            self.line_email.setValidator(QRegExpValidator( QRegExp("[a-z0-9]+[@]+[a-z]+[.]+[a-z]{0,3}")))
            self.line_email.setMaxLength(30)

            self.line_email.move(130,90)
            self.line_passw=QLineEdit(self)
            self.line_passw.move(130,125)
            self.line_passw.setEchoMode(QLineEdit.Password)
            self.line_passw.setMaxLength(14)
            self.line_passw.setToolTip(u"Maksimum 14 sayda şifrə əlavə edin")
            self.line_passw.setValidator(QRegExpValidator( QRegExp("[A-Za-z0-9_]{0,255}")))
            self.line_passw.cursorPositionChanged.connect(self.activebutton)
            self.checkbox=QCheckBox(u"şifrəni göstər",self)
            self.checkbox.move(270,128)
            self.checkbox.clicked.connect(self.showpassw)
            self.button_ok=QPushButton(u"Qeydiyyat",self)
            self.button_ok.move(130,170)
            self.button_ok.clicked.connect(self.ok)
            self.button_ok.setEnabled(False)
            self.button_no=QPushButton(u"Sil",self)
            self.button_no.move(210,170)
            self.button_no.clicked.connect(self.clear)
            self.label_signup=QLabel(self)
            self.label_signup.setText(u"Daxil ol (Əgər qeydiyatdan keçmisinizsə)")
            self.label_signup.move(40,220)
            self.label_signup.setStyleSheet("font-family:Courier;"
                                            "font-size:10pt;"
                                            "color:green;"
                                            "font:bold;")
            self.label_sign=QLabel(self)
            self.label_sign.setText(u"""
    Email*\n
    Şifrə*
    """)
            self.label_sign.setStyleSheet("font-size:12pt;"
                                        "font-family:Courier;")
            self.label_sign.move(4,240)
            self.line_emailsign=QLineEdit(self)
            self.line_emailsign.move(130,260)
            self.line_emailsign.setPlaceholderText("example@xxx.com")
            self.line_emailsign.setValidator(QRegExpValidator( QRegExp("[a-z0-9]+[@]+[a-z]+[.]+[a-z]{0,3}")))
            self.line_emailsign.setMaxLength(30)

            self.line_passwsign=QLineEdit(self)
            self.line_passwsign.move(130,290)
            self.line_passwsign.setEchoMode(QLineEdit.Password)
            self.line_passwsign.setMaxLength(14)
            self.line_passwsign.setToolTip(u"Maksimum 14 sayda şifrə əlavə edin")
            self.line_passw.setValidator(QRegExpValidator( QRegExp("[A-Za-z0-9_]{0,255}")))
            self.button_login=QPushButton(u"Daxil ol",self)
            self.button_login.move(160,330)
            self.button_login.clicked.connect(self.signup)
            self.checkbox_pass=QCheckBox(u"şifrəni göstər",self)
            self.checkbox_pass.move(272,295)
            self.checkbox_pass.clicked.connect(self.signpassshow)
            self.show()
        def escape(self):
            self.close()
        def signpassshow(self):
            if self.checkbox_pass.isChecked()==True:
                self.line_passwsign.setEchoMode(QLineEdit.Normal)
                self.line_passwsign.setText(self.line_passwsign.text())
            elif self.checkbox_pass.isChecked()==False:
                self.line_passw.setEchoMode(QLineEdit.Password)
                self.line_passwsign.setText(self.line_passwsign.text())

        def clear(self):
            self.line_name.clear()
            self.line_surname.clear()
            self.line_email.clear()
            self.line_passw.clear()

        def ok(self):

            fromaddr='yolserviceltd'
            toaddr=self.line_email.text()
            msg=self.line_passw.text()
            try:
                self.vb=sqlite3.connect("database/registration.db")
                self.crs=self.vb.cursor()
                self.crs.execute("""CREATE TABLE panel(panel_name TEXT,panel_surname TEXT,panel_email,panel_password)""")
                self.crs.execute("""INSERT INTO panel VALUES('{}','{}','{}','{}')""".format(self.line_name.text(),self.line_surname.text(),self.line_email.text(),self.line_passw.text()))
                self.vb.commit()
                v=self.crs.fetchall()
                for i in v:
                    print i
                self.vb.close()
                target="192.168.1.1"
                targetIP=gethostbyname(target)
                ip = load(urlopen('http://httpbin.org/ip'))['origin']

                session=smtplib.SMTP('smtp.gmail.com',587)
                session.ehlo()
                session.starttls()
                session.ehlo()
                session.login(str(fromaddr),'yolserviceltd123')
                session.sendmail(str(fromaddr),str(toaddr),str(msg))
                session.quit()
                self.message=QMessageBox()
                self.message.setWindowTitle("")
                self.message=QMessageBox.question(self,'Title',u'Ehtiyyat üçün şifrəniz,poçt ünvanınıza göndərildi\nQeydiyyat uğurla başa çatdı,Ok düyməsini sıxın',QMessageBox.Ok)






                if self.message==QMessageBox.Ok:
                    pass
                    

                   
            #----------------------------------------------------------------------------------------------------------------------------------------------------------


            except sqlite3.OperationalError:
                self.crs.execute("""INSERT INTO panel VALUES('{}','{}','{}','{}')""".format(self.line_name.text(),
                                                                                            self.line_surname.text(),
                                                                                            self.line_email.text(),
                                                                                            self.line_passw.text()))
                self.vb.commit()
                self.vb.close()
                self.message = QMessageBox()
                self.message.setWindowTitle("No internet connection")
                self.message = QMessageBox.question(self, 'Title',u'Ehtiyyat üçün şifrəniz,poçt ünvanınıza göndərildi\nQeydiyyat uğurla başa çatdı,Ok düyməsini sıxın',QMessageBox.Ok)
             

            except gaierror:
                self.message=QMessageBox()
                self.message.setWindowTitle("No internet connection")
                self.message=QMessageBox.question(self,'Title',u'Şəbəkə bağlantı xətası',QMessageBox.Yes | QMessageBox.No)
                if self.message==QMessageBox.Yes:
                    pass
                else:
                    self.close()
            except URLError, e:
                self.message=QMessageBox()
                self.message.setWindowTitle("No internet connection")
                self.message=QMessageBox.question(self,u'Şəbəkə',u'Şəbəkə bağlantı xətası',QMessageBox.Yes | QMessageBox.No)
                if self.message==QMessageBox.Yes:
                    pass
                else:
                    self.close()
            except smtplib.SMTPException:
                self.message=QMessageBox()
                self.message.setWindowTitle("No internet connection")
                self.message=QMessageBox.question(self,u'Şəbəkə',u'Email ünvanı və ya şəbəkə xətası.\nTəhlükəsizlik üçün seçdiyiniz şifrəni, mütləq emailinizə göndərməliyik.Yenidən yoxlayın')




        def activebutton(self):
            if self.line_name and self.line_surname and self.line_email and self.line_passw>0:
                self.button_ok.setEnabled(True)
            else:
                self.button_ok.setEnabled(False)
        def signup(self):
            try:
                self.vb=sqlite3.connect("database/registration.db")
                self.crs=self.vb.cursor()
                result=self.crs.execute("SELECT panel_email,panel_password FROM panel WHERE panel_email=='{}' AND panel_password =='{}'".format(self.line_emailsign.text(),self.line_passwsign.text()))
                if  len(result.fetchall())>0:
                    
                    os.system("python /home/xaos/Programlar/atelye/main.py")
                                    

                            

                    
                              
                    
                    
                else:
                    self.message=QMessageBox()
                    self.message.setWindowTitle(u"Xəta")
                    self.message=QMessageBox.question(self,u'Xəta',u"Email və ya şifrəniz səhvdir\nyenidən yoxlamaq üçün 'Yes' düyməsini\nçıxış üçün 'No' düyməsini seçin",QMessageBox.Yes | QMessageBox.No)
                    if self.message==QMessageBox.Yes:
                        pass
                    else:
                        self.close()
                        

            except sqlite3.OperationalError:
                self.message=QMessageBox()
                self.message.setWindowTitle(u"Xəta")
                self.message=QMessageBox.question(self,u'Xəta',u'Email və ya şifrəniz səhvdir\nyenidən yoxlamaq üçün Yes düyməsini\nÇıxış üçün No düyməsini seçin',QMessageBox.Yes | QMessageBox.No)
                if self.message==QMessageBox.Yes:
                    pass
                else:
                    self.close()
        def showpassw(self):
            if self.checkbox.isChecked()==True:
                self.line_passw.setEchoMode(QLineEdit.Normal)
                self.line_passw.setText(self.line_passw.text())
            elif self.checkbox.isChecked()==False:
                self.line_passw.setEchoMode(QLineEdit.Password)
                self.line_passw.setText(self.line_passw.text())


if __name__ == '__main__':
    app = QApplication([])
    gui=window()
    app.exec_()




