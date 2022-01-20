import sys

from PyQt5 import QtWidgets

from rr_light.gui import Ui_MainWindow
from rr_light.reflection_refraction import (
    calc_ref_plot,
    calculate_refr_angl,
    check_invalid_alfa,
    check_invalid_index_of_refr,
    matplotlib_graph,
)


def get_vars(my_app) -> tuple[float, float, float]:
    """Getting the variables from the user.

    :param self: self
    :return: Angle of incidence.
    :return: Index of refraction of the first medium
    :return: Index of refraction of the second medium
    """

    alfa = float(my_app.lineEdit.text())
    check_invalid_alfa(alfa)

    n1 = float(my_app.lineEdit_2.text())
    n2 = float(my_app.lineEdit_3.text())
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

    def _get_vars(self) -> tuple[float, float, float]:
        """Getting the variables from the user.

        :return: Angle of incidence.
        :return: Index of refraction of the first medium.
        :return: Index of refraction of the second medium.
        """

        alfa = float(self.lineEdit.text())
        check_invalid_alfa(alfa)
        n1 = float(self.lineEdit_2.text())
        n2 = float(self.lineEdit_3.text())
        check_invalid_index_of_refr(n1, n2)

        return alfa, n1, n2
    
    def _html_format(self, symbol: int, value: float) -> str:

        font_size = 16
    
        angle_sym = "&#8738;"
        _greek_sym = ""
        alfa_sym = "&#945;"
        beta_sym = "&#946;"
        alfa_prim_sym = "&#945;&#8242;"

        if symbol == 1:
            _greek_sym == alfa_sym
        if symbol == 2:
            _greek_sym == beta_sym
        if symbol == 3:
            _greek_sym == alfa_prim_sym 

        open_paragraph = '<html><head/><body><p>'
        ang = f'<span style="font-size:{font_size}pt;">{angle_sym}</span>'
        greek_symb = f'<span style="font-size:{font_size}pt;\">{_greek_sym} = {value}</span>'
        close_paragraph = '</p></body></html>'

        return open_paragraph + ang + greek_symb + close_paragraph

    def click_button(self):
        """The function for what the button when clicked will do."""

        try:
            alfa, n1, n2 = self._get_vars()
        except ValueError as e:
            self.label_5.setText("")
            self.label_6.setText(str(e))
            self.label_7.setText("")
            print(str(e))
            return

        alfa, alfa_prim, beta = calculate_refr_angl(alfa, n1, n2)
        alfa_text = self._html_format(1, alfa)
        alfa_prim_text = self._html_format(2, alfa_prim)
        beta_text = self._html_format(3, beta)

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
