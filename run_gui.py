from rr_light.reflection_refraction import *
from gui import * 
import sys

def get_vars(self) -> tuple[float,float,float]:
    '''Getting the variables from the user.
    
    :return: Angle of incidence.
    :return: Index of refraction of the first medium
    :return: Index of refraction of the second medium
    '''
    
    alfa = float(self.lineEdit.text())
    check_invalid_alfa(alfa)

    n1 = float(self.lineEdit_2.text())
    n2 = float(self.lineEdit_3.text())
    check_invalid_index_of_refr(n1, n2)

    return alfa, n1, n2

class MyApp(Ui_MainWindow):
    def __init__ (self, window):
        self.setupUi (window)
        # direct the signal to a method of the app
        self.pushButton.clicked.connect(self.clickButton)
    
    def clickButton (self):
        try:
            alfa, n1, n2 = get_vars(self)
        except ValueError as a:
            print(str(a))
            exit(1)

        alfa, n1, n2 = get_vars(self)
        alfa, alfa_prim, beta = calculate_refr_angl(alfa, n1, n2)

        alfa_text = "<html><head/><body><p><span style=\" font-size:16pt;\">∢</span><span style=\" font-family:\'Symbol\'; font-size:16pt;\">a = %s</span></p></body></html>"%alfa
        alfa_prim_text = "<html><head/><body><p><span style=\" font-size:16pt;\">∢</span><span style=\" font-family:\'Symbol\'; font-size:16pt;\">a</span><span style=\" font-family:\'Nimbus Roman No9 L\',\'Times New Roman\',\'Times\',\'serif\'; font-size:16pt;\">′</span><span style=\" font-family:\'Symbol\'; font-size:16pt;\"> = %s</span></p></body></html>"%alfa_prim
        beta_text = "<html><head/><body><p><span style=\" font-size:16pt;\">∢</span><span style=\" font-family:\'Symbol\'; font-size:16pt;\">b = %s</span></p></body></html>"%beta

        self.label_5.setText(alfa_text)
        self.label_6.setText(alfa_prim_text)
        self.label_7.setText(beta_text)
        
        # Old
        # self.label_5.setText(f"alfa = {alfa}")
        # self.label_6.setText(f"alfa_prim = {alfa_prim}")
        # self.label_7.setText(f"beta = {beta}")
        
        p1, p2, p3 = calc_ref_plot(alfa, beta)
        matplotlib_graph(p1, p2, p3, n1, n2)

app = QtWidgets. QApplication(sys.argv)
MainWindow = QtWidgets. QMainWindow()

# Create an instance of the app 
ui = MyApp(MainWindow)

# show the window and start the app 
MainWindow.show() 
app.exec_()