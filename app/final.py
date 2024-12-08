from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QDialog, QLabel
from PyQt6 import uic
import random
import os
import sys
import re

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)
        self.btnRegister.clicked.connect(self.show_register)
        self.btnLogin.clicked.connect(self.check_login)
        self.btnforgot.clicked.connect(self.reset)
        self.msg_box = QMessageBox()
    def check_login(self):
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        if self.validate_user(email, password):
            main.show()
            self.close()
        else:
            self.msg_box.setText("Please check your email or password")
            self.msg_box.exec()
    
    def validate_user(self, email, password):
        if not os.path.exists("users.txt"):
                return False
        with open("users.txt", "r") as file:
            for line in file:
                saved_email, saved_password = line.strip().split(",")
                if saved_email == email and saved_password == password:
                    return True
                
    def reset(self):
        self.Forgot_window = Forgot() 
        self.Forgot_window.show()

    def show_register(self):
        register.show()
        self.close()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("signup.ui", self)

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("signup.ui", self)
        self.btnRegister.clicked.connect(self.show_login)
        self.btnRegister.clicked.connect(self.register_user)
        self.btnLogin.clicked.connect(self.show_login)

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("signup.ui", self)
        self.btnRegister.clicked.connect(self.register_user) 
        self.btnLogin.clicked.connect(self.show_login)
        self.msg_box = QMessageBox() 

    def register_user(self):
        email = self.txtEmail.text()
        password = self.txtPass.text()
        diachinha = self.txtdiachinha.text()
        

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                self.msg_box.setText("Email không hợp lệ")
                self.msg_box.exec()

        elif len(password) < 8:
                self.msg_box.setText("Mật khẩu 8 kí tự trở lên")
                self.msg_box.exec()    

        elif not self.checkBox.isChecked():
                self.msg_box.setText("Vui lòng chấp nhận điều khoản")
                self.msg_box.exec() 

        elif email and password and diachinha:
            if self.save_user(email, password):
                self.msg_box.setText("Đăng kí thành công! Hãy đăng nhập")
                self.msg_box.exec()
                login.show()
                self.close()
            else:
                self.msg_box.setText("Tài khoản đã tồn tại")
                self.msg_box.exec() 

        else:
            self.msg_box.setText("Vui lòng điền đầy đủ thông tin")
            self.msg_box.exec()
  
    def save_user(self, email, password):
        if not os.path.exists("users.txt"):
            with open("users.txt","w") as file:
                pass

        with open("users.txt","r") as file:
            for line in file:
                saved_email, _ = line.strip().split(",")
                if email == saved_email:
                    return False
                
        with open("users.txt","a") as file:
            file.write(f"{email},{password}\n")
        return True

    def show_login(self):
        login.show()
        self.close()

    def kiem_tra_click(self):
        if self.checkBox.isChecked():
            self.show_login()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chấp nhận điều khoản")
    
    def show_login(self):
        login.show()
        self.close()

class Support(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Support.ui", self)
        self.btnSent.clicked.connect(self.kiem_tra)

    def kiem_tra(self):
        email = self.txtEmail.text()
        if not email:
            QMessageBox.warning(self, "Lỗi", "Thiếu email")
        else:
            QMessageBox.information(self, "Thông báo", "Đã gửi")

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main3.ui", self)
        self.Support1main.clicked.connect(self.show_support)
        self.Support2main.clicked.connect(self.show_support)
        self.login_window =Login()
        self.register_window = Register()
        self.dog_window = Dog()
        self.cat_window = Cat()
        self.toy_window = Toy()
        self.spa_window = Spa()
        self.btnRegister2.clicked.connect(self.login)
        self.btnRegister3.clicked.connect(self.register)
        self.pushButton_23.clicked.connect(self.dog)
        self.pushButton_18.clicked.connect(self.cat)
        self.pushButton_17.clicked.connect(self.toy)
        self.pushButton_21.clicked.connect(self.toy)
        self.pushButton_15.clicked.connect(self.spa)
        self.pushButton_22.clicked.connect(self.spa)
    
    def spa(self):
        self.spa_window.show()
        self.close()

    def dog(self):
        self.dog_window.show()
        self.close()

    def cat(self):
        self.cat_window.show()
        self.close()

    def toy(self):
        self.toy_window.show()
        self.close()
    
    def register(self):
        self.register_window.show()
        self.close()

    def login(self):
        self.login_window.show()
        self.close()

    def show_support(self):
        self.support_window = Support() 
        self.support_window.show()
        self.close()

class Forgot(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("resetpass.ui", self)
        self.login_window =Login()
        self.register_window = Register()
        self.support_window = Support()
        self.btnreset.clicked.connect(self.quen_mk)
        self.btnRegister2.clicked.connect(self.login)
        self.btnRegister3.clicked.connect(self.register)
        self.btnRegister.clicked.connect(self.show_support)

    def show_support(self):
        self.support_window.show()
        self.close()
       
    def register(self):
        self.register_window.show()
        self.close()

    def login(self):
        self.login_window.show()
        self.close()

    def quen_mk(self):
        email = self.txtEmail.text()
        self.forgot2_window = Forgot2() 
        if not email:
            QMessageBox.warning(self, "Lỗi", "Mail không tồn tại")
        else:
            QMessageBox.information(self, "Thông báo", "Đã gửi") and self.forgot2_window.show() and self.close()

class Forgot2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("resetpass2.ui", self)
        self.btnreset.clicked.connect(self.quen_mk)
        self.login_window =Login()
        self.register_window = Register()
        self.support_window = Support()
        self.btnRegister2.clicked.connect(self.login)
        self.btnRegister3.clicked.connect(self.register)
        self.btnRegister.clicked.connect(self.show_support)

    def show_support(self):
        self.support_window.show()
        self.close()
    
    def register(self):
        self.register_window.show()
        self.close()

    def login(self):
        self.login_window.show()
        self.close()

    def quen_mk(self):
        email = 1000
        self.success_window = Forgot3() 
        if not email:
            QMessageBox.warning(self, "Lỗi", "Vui lòng thử lại")
        else:
            QMessageBox.information(self, "Thông báo", " Vui lòng đặt mật khẩu mới") and self.success_window.show() and self.close()

class Forgot3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_window = Login()
        uic.loadUi("success.ui", self)
        self.btnreset.clicked.connect(self.show_login)
        self.login_window =Login()
        self.register_window = Register()
        self.btnRegister2.clicked.connect(self.login)
        self.btnRegister3.clicked.connect(self.register)
        self.support_window = Support()
        self.btnRegister.clicked.connect(self.show_support)
        if not email:
            QMessageBox.warning(self, "Lỗi", "Không được để trống")
        else:
            QMessageBox.information(self, "Thông báo", "Đổi mật khẩu thành công") and self.login_window.show() and self.close()

    def show_support(self):
        self.support_window.show()
        self.close()
    
    def register(self):
        self.register_window.show()
        self.close()

    def login(self):
        self.login_window.show()
        self.close()

    def show_login(self):
        self.login_window.show()
        self.close()

class Dog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_window = Login()
        uic.loadUi("cho.ui", self)
        self.pushButton_11.clicked.connect(self.nextpage)
        self.pushButton_10.clicked.connect(self.previouspage)
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton_3.clicked.connect(self.confirm)
        self.pushButton_4.clicked.connect(self.confirm)
        self.pushButton_5.clicked.connect(self.confirm)
        self.pushButton_6.clicked.connect(self.confirm)
        self.pushButton_7.clicked.connect(self.confirm)
        self.pushButton_8.clicked.connect(self.confirm)

    def confirm(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setText("Bạn có chắc chắn muốn mua không?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        repr = msg_box.exec()
        if repr == QMessageBox.StandardButton.Yes:
            code = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
            QMessageBox.information(self, "Thông báo", f"Bạn đã đặt hàng thành công!\n Mã của bạn: {code}\n Hãy đưa mã này cho nhân viên hoặc giao hàng")
        else:
            QMessageBox.information(self, "Thông báo", "Bạn đã huỷ đặt hàng")

    def previouspage(self):
        self.main_window = Main()
        self.main_window.show()
        self.close()

    def nextpage(self):
        self.dog2_window = Dog2()
        self.dog2_window.show()
        self.close()

class Dog2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("cho - Copy.ui", self)
        self.pushButton_10.clicked.connect(self.nextpage)
        self.pushButton_11.clicked.connect(self.previouspage)
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton_3.clicked.connect(self.confirm)
        self.pushButton_4.clicked.connect(self.confirm)
        self.pushButton_5.clicked.connect(self.confirm)
        self.pushButton_6.clicked.connect(self.confirm)
        self.pushButton_7.clicked.connect(self.confirm)
        self.pushButton_8.clicked.connect(self.confirm)

    def confirm(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setText("Bạn có chắc chắn muốn mua không?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        repr = msg_box.exec()
        if repr == QMessageBox.StandardButton.Yes:
            code = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
            QMessageBox.information(self, "Thông báo", f"Bạn đã đặt hàng thành công!\n Mã của bạn: {code}\n Hãy đưa mã này cho nhân viên hoặc giao hàng")
        else:
            QMessageBox.information(self, "Thông báo", "Bạn đã huỷ đặt hàng")

    def previouspage(self):
        self.dog_window = Dog()
        self.dog_window.show()
        self.close()

    def nextpage(self):
        self.dog3_window = Dog3()
        self.dog3_window.show()
        self.close()

class Dog3(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("cho - Copy - Copy.ui", self)   
        self.pushButton_11.clicked.connect(self.previouspage)
        self.pushButton_1.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton_3.clicked.connect(self.confirm)
        self.pushButton_4.clicked.connect(self.confirm)
        self.pushButton_5.clicked.connect(self.confirm)
        self.pushButton_6.clicked.connect(self.confirm)
        self.pushButton_7.clicked.connect(self.confirm)
        self.pushButton_8.clicked.connect(self.confirm)

    def confirm(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setText("Bạn có chắc chắn muốn mua không?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        repr = msg_box.exec()
        if repr == QMessageBox.StandardButton.Yes:
            code = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
            QMessageBox.information(self, "Thông báo", f"Bạn đã đặt hàng thành công!\n Mã của bạn: {code}\n Hãy đưa mã này cho nhân viên hoặc giao hàng")
        else:
            QMessageBox.information(self, "Thông báo", "Bạn đã huỷ đặt hàng")

    def previouspage(self):
        self.dog_window = Dog2()
        self.dog_window.show()
        self.close()

class Cat(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("meo.ui", self)
        self.pushButton_11.clicked.connect(self.nextpage)
        self.pushButton_10.clicked.connect(self.previouspage)
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton_3.clicked.connect(self.confirm)
        self.pushButton_4.clicked.connect(self.confirm)
        self.pushButton_5.clicked.connect(self.confirm)
        self.pushButton_6.clicked.connect(self.confirm)
        self.pushButton_7.clicked.connect(self.confirm)
        self.pushButton_8.clicked.connect(self.confirm)

    def confirm(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setText("Bạn có chắc chắn muốn mua không?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        repr = msg_box.exec()
        if repr == QMessageBox.StandardButton.Yes:
            code = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
            QMessageBox.information(self, "Thông báo", f"Bạn đã đặt hàng thành công!\n Mã của bạn: {code}\n Hãy đưa mã này cho nhân viên hoặc giao hàng")
        else:
            QMessageBox.information(self, "Thông báo", "Bạn đã huỷ đặt hàng")

    def previouspage(self):
        self.main_window = Main()
        self.main_window.show()
        self.close()

    def nextpage(self):
        self.cat2_window = Cat2()
        self.cat2_window.show()
        self.close()

class Cat2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("meo - Copy.ui", self)
        self.pushButton_11.clicked.connect(self.nextpage)
        self.pushButton_10.clicked.connect(self.previouspage)
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton_3.clicked.connect(self.confirm)
        self.pushButton_4.clicked.connect(self.confirm)
        self.pushButton_5.clicked.connect(self.confirm)
        self.pushButton_6.clicked.connect(self.confirm)
        self.pushButton_7.clicked.connect(self.confirm)
        self.pushButton_8.clicked.connect(self.confirm)

    def confirm(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setText("Bạn có chắc chắn muốn mua không?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        repr = msg_box.exec()
        if repr == QMessageBox.StandardButton.Yes:
            code = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
            QMessageBox.information(self, "Thông báo", f"Bạn đã đặt hàng thành công!\n Mã của bạn: {code}\n Hãy đưa mã này cho nhân viên hoặc giao hàng")
        else:
            QMessageBox.information(self, "Thông báo", "Bạn đã huỷ đặt hàng")

    def previouspage(self):
        self.cat_window = Cat()
        self.cat_window.show()
        self.close()

    def nextpage(self):
        self.Cat_window = Cat3()
        self.Cat_window.show()
        self.close()

class Cat3(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("meo - Copy - Copy.ui", self)
        self.pushButton_10.clicked.connect(self.previouspage)
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton_3.clicked.connect(self.confirm)
        self.pushButton_4.clicked.connect(self.confirm)
        self.pushButton_5.clicked.connect(self.confirm)
        self.pushButton_6.clicked.connect(self.confirm)
        self.pushButton_7.clicked.connect(self.confirm)
        self.pushButton_8.clicked.connect(self.confirm)

    def confirm(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setText("Bạn có chắc chắn muốn mua không?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        repr = msg_box.exec()
        if repr == QMessageBox.StandardButton.Yes:
            code = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
            QMessageBox.information(self, "Thông báo", f"Bạn đã đặt hàng thành công!\n Mã của bạn: {code}\n Hãy đưa mã này cho nhân viên hoặc giao hàng")
        else:
            QMessageBox.information(self, "Thông báo", "Bạn đã huỷ đặt hàng")

    def previouspage(self):
        self.main_window = Cat2()
        self.main_window.show()
        self.close()
    
    def nextpage(self):
        self.Cat_window = Cat3()
        self.Cat_window.show()
        self.close()

class Toy(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("do dung.ui", self)
        self.pushButton_9.clicked.connect(self.nextpage)
        self.pushButton_10.clicked.connect(self.previouspage)
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton_3.clicked.connect(self.confirm)
        self.pushButton_4.clicked.connect(self.confirm)
        self.pushButton_5.clicked.connect(self.confirm)
        self.pushButton_6.clicked.connect(self.confirm)
        self.pushButton_7.clicked.connect(self.confirm)
        self.pushButton_8.clicked.connect(self.confirm)

    def confirm(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setText("Bạn có chắc chắn muốn mua không?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        repr = msg_box.exec()
        if repr == QMessageBox.StandardButton.Yes:
            code = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
            QMessageBox.information(self, "Thông báo", f"Bạn đã đặt hàng thành công!\n Mã của bạn: {code}\n Hãy đưa mã này cho nhân viên hoặc giao hàng")
        else:
            QMessageBox.information(self, "Thông báo", "Bạn đã huỷ đặt hàng")

    def previouspage(self):
        self.main_window = Main()
        self.main_window.show()
        self.close()

    def nextpage(self):
        self.toy2_window = Toy2()
        self.toy2_window.show()
        self.close()

class Toy2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("do dung - Copy.ui", self)
        self.pushButton_9.clicked.connect(self.nextpage)
        self.pushButton_10.clicked.connect(self.previouspage)
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton_3.clicked.connect(self.confirm)
        self.pushButton_4.clicked.connect(self.confirm)
        self.pushButton_5.clicked.connect(self.confirm)
        self.pushButton_6.clicked.connect(self.confirm)
        self.pushButton_7.clicked.connect(self.confirm)
        self.pushButton_8.clicked.connect(self.confirm)

    def confirm(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setText("Bạn có chắc chắn muốn mua không?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        repr = msg_box.exec()
        if repr == QMessageBox.StandardButton.Yes:
            code = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
            QMessageBox.information(self, "Thông báo", f"Bạn đã đặt hàng thành công!\n Mã của bạn: {code}\n Hãy đưa mã này cho nhân viên hoặc giao hàng")
        else:
            QMessageBox.information(self, "Thông báo", "Bạn đã huỷ đặt hàng")

    def previouspage(self):
        self.toy_window = Toy()
        self.toy_window.show()
        self.close()

    def nextpage(self):
        self.toy3_window = Toy3()
        self.toy3_window.show()
        self.close()

class Toy3(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("do dung - Copy - Copy.ui", self)
        self.pushButton_9.clicked.connect(self.nextpage)
        self.pushButton_10.clicked.connect(self.previouspage)
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton_3.clicked.connect(self.confirm)
        self.pushButton_4.clicked.connect(self.confirm)
        self.pushButton_5.clicked.connect(self.confirm)
        self.pushButton_6.clicked.connect(self.confirm)
        self.pushButton_7.clicked.connect(self.confirm)
        self.pushButton_8.clicked.connect(self.confirm)

    def confirm(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setText("Bạn có chắc chắn muốn mua không?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        repr = msg_box.exec()
        if repr == QMessageBox.StandardButton.Yes:
            code = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
            QMessageBox.information(self, "Thông báo", f"Bạn đã đặt hàng thành công!\n Mã của bạn: {code}\n Hãy đưa mã này cho nhân viên hoặc giao hàng")
        else:
            QMessageBox.information(self, "Thông báo", "Bạn đã huỷ đặt hàng") 

    def previouspage(self):
        self.toy_window = Toy2()
        self.toy_window.show()
        self.close()

    def nextpage(self):
        self.toy4_window = Toy4()
        self.toy4_window.show()
        self.close()

class Toy4(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("do dung - Copy - Copy - Copy.ui", self)
        self.pushButton_9.clicked.connect(self.previouspage)
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton_3.clicked.connect(self.confirm)
        self.pushButton_4.clicked.connect(self.confirm)
        self.pushButton_5.clicked.connect(self.confirm)
        self.pushButton_6.clicked.connect(self.confirm)
        self.pushButton_7.clicked.connect(self.confirm)
        self.pushButton_8.clicked.connect(self.confirm)

    def confirm(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setText("Bạn có chắc chắn muốn mua không?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        repr = msg_box.exec()
        if repr == QMessageBox.StandardButton.Yes:
            code = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
            QMessageBox.information(self, "Thông báo", f"Bạn đã đặt hàng thành công!\n Mã của bạn: {code}\n Hãy đưa mã này cho nhân viên hoặc giao hàng")
        else:
            QMessageBox.information(self, "Thông báo", "Bạn đã huỷ đặt hàng")

    def previouspage(self):
        self.toy3_window = Toy3()
        self.toy3_window.show()
        self.close()

class Spa(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("spa.ui", self)
        self.pushButton_11.clicked.connect(self.mainmenu)
        self.pushButton.clicked.connect(self.confirm)
        self.pushButton_2.clicked.connect(self.confirm)
        self.pushButton_3.clicked.connect(self.confirm)
        self.pushButton_4.clicked.connect(self.confirm)
        self.pushButton_5.clicked.connect(self.confirm)
        self.pushButton_6.clicked.connect(self.confirm)
        self.pushButton_7.clicked.connect(self.confirm)
        self.pushButton_8.clicked.connect(self.confirm)

    def confirm(self):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Question)
        msg_box.setWindowTitle("Xác nhận")
        msg_box.setText("Bạn có chắc chắn muốn sử dụng dịch vụ này không?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        repr = msg_box.exec()
        if repr == QMessageBox.StandardButton.Yes:
            code = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
            QMessageBox.information(self, "Thông báo", f"Bạn đã đặt hàng thành công!\n Mã mua hàng của bạn: {code}\n Hãy đưa mã này cho nhân viên để sử dụng dịch vụ Spa của bạn đã đặt")
        else:
            QMessageBox.information(self, "Thông báo", "Bạn đã huỷ đặt hàng")

    def mainmenu(self):
        self.main_window = Main()
        self.main_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    register = Register()
    main = Main()
    login.show()
    app.exec()