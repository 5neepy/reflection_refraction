import sys
from gui import Ui_MainWindow
from PyQt5 import QtWidgets
from rr_light.reflection_refraction import (
    calc_ref_plot,
    calculate_refr_angl,
    check_invalid_alfa,
    check_invalid_index_of_refr,
    matplotlib_graph,
)


def get_vars(self) -> tuple[float, float, float]:
    """Getting the variables from the user.

    :param self: self
    :return: Angle of incidence.
    :return: Index of refraction of the first medium
    :return: Index of refraction of the second medium
    """

    alfa = float(self.lineEdit.text())
    check_invalid_alfa(alfa)

    n1 = float(self.lineEdit_2.text())
    n2 = float(self.lineEdit_3.text())
    check_invalid_index_of_refr(n1, n2)

    return alfa, n1, n2


class MyApp(Ui_MainWindow):
    """This is class for the Qt5 app.

    :param Ui_MainWindow: The window that is going to pop up
    """

    def __init__(self, window):
        self.setupUi(window)
        # direct the signal to a method of the app
        self.pushButton.clicked.connect(self.click_button)

    def click_button(self):
        """The function for what the button when clicked will do."""

        try:
            alfa, n1, n2 = get_vars(self)
        except ValueError as a:
            print(str(a))
            exit(1)

        alfa, n1, n2 = get_vars(self)
        alfa, alfa_prim, beta = calculate_refr_angl(alfa, n1, n2)

        alfa_text = (
            '<html><head/><body><p><span style=" font-size:16pt;">∢</span><span style=" ',
            "font-family:'Symbol'; font-size:16pt;\">a = %s</span></p></body></html>"
            % alfa,
        )
        alfa_prim_text = (
            '<html><head/><body><p><span style=" font-size:16pt;">∢</span><span style=" ',
            "font-family:'Symbol'; font-size:16pt;\">a</span><span style=\" font-family:'Nimbus ",
            "Roman No9 L','Times New Roman','Times','serif'; font-size:16pt;\">′</span>",
            "<span style=\" font-family:'Symbol'; font-size:16pt;\"> = %s</span></p></body></html>"
            % alfa_prim,
        )
        beta_text = (
            '<html><head/><body><p><span style=" font-size:16pt;">∢</span><span style=" '
            "font-family:'Symbol'; font-size:16pt;\">b = %s</span></p></body></html>"
            % beta
        )

        self.label_5.setText(alfa_text)
        self.label_6.setText(alfa_prim_text)
        self.label_7.setText(beta_text)

        p1, p2, p3 = calc_ref_plot(alfa, beta)
        matplotlib_graph(p1, p2, p3, n1, n2)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

# Create an instance of the app
ui = MyApp(MainWindow)

# show the window and start the app
MainWindow.show()
app.exec_()
